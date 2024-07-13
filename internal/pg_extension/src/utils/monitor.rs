use std::sync::{Arc, Mutex};
use std::thread;
use std::time::{Duration, Instant};
use sysinfo::{System, SystemExt, ProcessExt};

fn start_memory_monitoring(interval: Duration, memory_log: Arc<Mutex<Vec<(f64, u64)>>>) {
    let pid = std::process::id() as i32;
    let mut system = System::new_all();

    thread::spawn(move || {
        loop {
            system.refresh_all();
            if let Some(process) = system.process(pid) {
                let memory_usage = process.memory();
                let timestamp = Instant::now().elapsed().as_secs_f64();
                let mut log = memory_log.lock().unwrap();
                log.push((timestamp, memory_usage));
            }
            thread::sleep(interval);
        }
    });
}


