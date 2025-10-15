use std::thread;

fn main() {
    // Create a vector to store thread handles
    let mut handles = Vec::new();
    
    // Spawn 5 threads
    for i in 0..5 {
        let handle = thread::spawn(move || {
            let result = i * i;
            println!("Thread {} calculated: {}² = {}", i, i, result);
            result // Return the result
        });
        handles.push(handle);
    }
    
    // Collect results from all threads
    let mut results = Vec::new();
    for handle in handles {
        let result = handle.join().unwrap();
        results.push(result);
    }
    
    // Calculate sum
    let sum: i32 = results.iter().sum();
    
    println!("\nSum of all results: {}", sum);
    println!("All threads completed!");
}
