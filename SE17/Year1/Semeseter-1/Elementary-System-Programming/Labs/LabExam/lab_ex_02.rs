use std::env;
use std::fs;
use std::process;

fn main() {
    let args: Vec<String> = env::args().collect();
    
    // Check if file path is provided
    if args.len() < 2 {
        eprintln!("Error: Missing file path argument.");
        eprintln!("Usage: program <file_path> [flag]");
        eprintln!("Flags: -w (word count), -l (line count)");
        process::exit(1);
    }
    
    let file_path = &args[1];
    
    // Parse optional flag
    let flag = if args.len() >= 3 {
        Some(args[2].as_str())
    } else {
        None
    };
    
    // Validate flag
    if let Some(f) = flag {
        if f != "-w" && f != "-l" {
            eprintln!("Error: Invalid flag '{}'. Use -w for word count or -l for line count.", f);
            process::exit(1);
        }
    }
    
    // Read file content
    let content = match fs::read_to_string(file_path) {
        Ok(content) => content,
        Err(_) => {
            eprintln!("Error: File not found: {}", file_path);
            process::exit(1);
        }
    };
    
    // Count lines and words
    let line_count = content.lines().count();
    let word_count = content.split_whitespace().count();
    
    // Output based on flag
    match flag {
        Some("-w") => {
            println!("Words: {}", word_count);
        }
        Some("-l") => {
            println!("Lines: {}", line_count);
        }
        _ => {
            println!("Lines: {}", line_count);
            println!("Words: {}", word_count);
        }
    }
}
