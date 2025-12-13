use std::env;
use std::fs::File;
use std::io::{self, Write, Read, BufRead, BufReader};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    println!("Enter multiple lines of text (end with an empty line):");
    
    let mut user_input = String::new();
    let stdin = io::stdin();
    
    // Read multiple lines until empty line
    loop {
        let mut line = String::new();
        stdin.read_line(&mut line)?;
        
        // Check if line is empty (just newline)
        if line.trim().is_empty() {
            break;
        }
        
        user_input.push_str(&line);
    }
    
    // Create file with system info and user input
    let mut file = File::create("output.txt")?;
    
    // Get OS information
    let os = env::consts::OS;
    
    // Get user information (try both USER and USERNAME)
    let user = env::var("USER").or_else(|_| env::var("USERNAME"))
        .unwrap_or_else(|_| "Unknown".to_string());
    
    // Write system values at the top of file
    writeln!(file, "OS: {}", os)?;
    writeln!(file, "User: {}", user)?;
    
    // Append user input
    file.write_all(user_input.as_bytes())?;
    
    // Re-open and display file contents in uppercase
    let mut file = File::open("output.txt")?;
    let reader = BufReader::new(file);
    
    println!("\nFile contents in uppercase:");
    for line in reader.lines() {
        let line = line?;
        println!("{}", line.to_uppercase());
    }
    
    Ok(())
}
