use std::env;
use std::process;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let args: Vec<String> = env::args().collect();
    
    // Check if exactly 3 arguments are passed (excluding program name)
    if args.len() != 4 {
        eprintln!("Error: Exactly 3 arguments are required (number1 operator number2). You provided {}.", args.len() - 1);
        process::exit(1);
    }
    
    // Parse first number
    let num1: f64 = match args[1].parse() {
        Ok(n) => n,
        Err(_) => {
            eprintln!("Error: '{}' is not a valid number.", args[1]);
            process::exit(1);
        }
    };
    
    // Get operator
    let operator = &args[2];
    
    // Parse second number
    let num2: f64 = match args[3].parse() {
        Ok(n) => n,
        Err(_) => {
            eprintln!("Error: '{}' is not a valid number.", args[3]);
            process::exit(1);
        }
    };
    
    // Validate operator and perform calculation
    let result = match operator.as_str() {
        "+" => num1 + num2,
        "-" => num1 - num2,
        "*" => num1 * num2,
        "/" => {
            if num2 == 0.0 {
                eprintln!("Error: Division by zero.");
                process::exit(1);
            }
            num1 / num2
        }
        _ => {
            eprintln!("Error: Unsupported operator '{}'. Supported operators: +, -, *, /", operator);
            process::exit(1);
        }
    };
    
    println!("{} {} {} = {}", num1, operator, num2, result);
    
    Ok(())
}