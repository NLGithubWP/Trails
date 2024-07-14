use std::sync::{Arc, Mutex};
use std::thread;
use std::time::{Duration, Instant};
use sysinfo::{System, SystemExt, ProcessExt};

pub fn start_memory_monitoring(interval: Duration, memory_log: Arc<Mutex<Vec<(String, f64, u64)>>>, label: String, start_time: Instant) {
    let pid = std::process::id() as i32;
    let mut system = System::new_all();

    thread::spawn(move || {
        loop {
            system.refresh_all();
            if let Some(process) = system.process(pid) {
                let memory_usage = process.memory();
                let timestamp = start_time.elapsed().as_secs_f64(); // Use the same Instant to get elapsed time
                let mut log = memory_log.lock().unwrap();
                log.push((label.clone(), timestamp, memory_usage));
            }
            thread::sleep(interval);
        }
    });
}


pub fn log_memory_usage(memory_log: &Arc<Mutex<Vec<(String, f64, u64)>>>, start_time: Instant, label: &str) {
    let pid = std::process::id() as i32;
    let mut system = System::new_all();
    system.refresh_all();
    if let Some(process) = system.process(pid) {
        let memory_usage = process.memory();
        let timestamp = start_time.elapsed().as_secs_f64();
        let mut log = memory_log.lock().unwrap();
        log.push((label.to_string(), timestamp, memory_usage));
    }
}
