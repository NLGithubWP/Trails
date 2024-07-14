use std::sync::{Arc, Mutex};
use std::thread;
use std::time::{Duration, Instant};
use sysinfo::{System, SystemExt, ProcessExt};

pub fn start_memory_monitoring(interval: Duration,
                               memory_log: &mut Vec<(String, f64, u64)>,
                               label: &str,
                               start_time: Instant) {
    let pid = std::process::id() as i32;
    let mut system = System::new_all();

    let label = label.to_string(); // Move label into the closure
    let start_time = start_time; // Move start_time into the closure
    let mut memory_log = memory_log.clone(); // Clone the memory_log to move it into the closure

    thread::spawn(move || {
        loop {
            system.refresh_memory();
            if let Some(process) = system.process(pid) {
                let memory_usage = process.memory();
                let timestamp = start_time.elapsed().as_secs_f64();
                memory_log.push((label.clone(), timestamp, memory_usage));
            }
            thread::sleep(interval);
        }
    });
}


pub fn log_memory_usage(memory_log: &mut Vec<(String, f64, u64)>,
                        start_time: Instant, label: &str, pid: i32) {
    let mut system = System::new_all();
    system.refresh_memory();
    if let Some(process) = system.process(pid) {
        let memory_usage = process.memory();
        let timestamp = start_time.elapsed().as_secs_f64();
        memory_log.push((label.to_string(), timestamp, memory_usage));
    }
}
