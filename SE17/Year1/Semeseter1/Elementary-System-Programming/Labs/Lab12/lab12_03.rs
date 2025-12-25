use std::env;
use std::fs;
use std::process;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let args: Vec<String> = env::args().collect();
    
    // Check if file path argument is provided
    if args.len() != 2 {
        eprintln!("Error: Missing file path argument.");
        process::exit(1);
    }
    
    let file_path = &args[1];
    
    // Read file contents
    let contents = match fs::read_to_string(file_path) {
        Ok(content) => content,
        Err(_) => {
            eprintln!("Error: File not found or unreadable: {}", file_path);
            process::exit(1);
        }
    };
    
    // Count lines
    let lines = if contents.is_empty() {
        0
    } else {
        contents.lines().count()
    };
    
    // Count words
    let words = contents
        .split_whitespace()
        .count();
    
    // Count characters
    let characters = contents.len();
    
    // Display results
    println!("File: {}", file_path);
    println!("Lines: {}", lines);
    println!("Words: {}", words);
    println!("Characters: {}", characters);
    
    Ok(())
}