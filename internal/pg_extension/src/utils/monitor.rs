use std::sync::{Arc, Mutex};
use std::thread;
use std::time::{Duration, Instant};
use sysinfo::{System, SystemExt, ProcessExt};

// pub fn start_memory_monitoring(interval: Duration, memory_log: &mut Vec<(String, f64, u64)>, label: &str, start_time: Instant) {
//     let pid = std::process::id() as i32;
//     let mut system = System::new_all();
//
//     thread::spawn(move || {
//         loop {
//             system.refresh_all();
//             if let Some(process) = system.process(pid) {
//                 let memory_usage = process.memory();
//                 let timestamp = start_time.elapsed().as_secs_f64(); // Use the same Instant to get elapsed time
//                 memory_log.push((label.to_string(), timestamp, memory_usage)); // Append directly to the vector
//             }
//             thread::sleep(interval);
//         }
//     });
// }


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


pub fn print_memory_usage(start_time: Instant, label: &str, pid: i32) {
    let mut system = System::new_all();
    system.refresh_memory();
    if let Some(process) = system.process(pid) {
        let memory_usage = process.memory();
        let timestamp = start_time.elapsed().as_secs_f64();
        // Log to PostgreSQL server log and print to client
        pgx::elog!(
            pgx::PgLogLevel::NOTICE,
            "{}, Second {}, MB {} ",
            label.to_string(),
            timestamp.to_string(),
            memory_usage.to_string()
    );
    }
}