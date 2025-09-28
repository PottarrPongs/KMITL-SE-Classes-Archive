use std::env;
use std::process;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let args: Vec<String> = env::args().collect();
    
    // Check if exactly 3 arguments are passed (excluding program name)
    // args[0] is the program name, so we need args.len() == 4
    if args.len() != 4 {
        eprintln!("Error: Exactly 3 arguments are required. You provided {}.", args.len() - 1);
        process::exit(1);
    }
    
    // Print each argument on a single line
    println!("Arguments provided: {}, {}, {}", args[1], args[2], args[3]);
    
    Ok(())
}