use std::fs::{self, File};
use std::io::{self, BufRead, Write};
use std::path::Path;
use std::process::exit;

fn main() {
    let mut file_name: Option<String> = None;  // Use Option to track if a file is open
    let mut file_content: Vec<String> = Vec::new();
    loop {
        println!("\nMenu:");
        println!("open <filename>");
        println!("add <line content>");
        println!("delete <line_number>");
        println!("display");
        println!("write");
        println!("exit");
        
        let mut choice = String::new();
        io::stdin().read_line(&mut choice).expect("Failed to read line");
        let choice = choice.trim();
        
        let mut commands: Vec<&str> = Vec::new();
        
        for part in choice.split_whitespace() {
            commands.push(part);
        }
        
        let lead_command = commands[0];
        
        commands.remove(0);
        let keywords: String  = commands.join(" ");
        
        
        // println!("|{}|", keywords);
        match lead_command {
            "open" => {
                file_name = open_file(&mut file_content, keywords);  // Update file_name
            }
            "display" => {
                if file_name.is_none() {
                    println!("No file open. Please open a file first.");
                } else {
                    display_content(&file_content);
                }
            }
            "add" => {
                if file_name.is_none() {
                    println!("No file open. Please open a file first.");
                } else {
                    add_line(&mut file_content, keywords);
                }
            }
            "delete" => {
                if file_name.is_none() {
                    println!("No file open. Please open a file first.");
                    } else if keywords == "" {
                            println!("No line insert.")
                    } else {
                        delete_line(&mut file_content, keywords);
                    }
                }
                "write" => {
                    if let Some(ref file) = file_name {
                        write_file(file, &file_content);
                    } else {
                        println!("No file open. Please open a file first.");
                    }
                }
                "exit" => {
                    println!("Exiting...");
                    exit(0);
                }
                _ => {
                    println!("Invalid choice. Please select an option from the menu.");
                }
            }
            
            commands.clear();
        }
    }
    
    fn open_file(file_content: &mut Vec<String>, x: String) -> Option<String> {
        // println!("Enter the file name to open:");
        // let mut file_name = String::new();
        // io::stdin().read_line(&mut file_name).expect("Failed to read line");
        // let file_name = file_name.trim().to_string();
        let file_name = x;
    if Path::new(&file_name).exists() {
        let file = File::open(&file_name).expect("Unable to open file");
        let reader = io::BufReader::new(file);
        file_content.clear();
        for line in reader.lines() {
            file_content.push(line.expect("Unable to read line"));
        }
        println!("File opened successfully.");
        Some(file_name)  // Return the file name
    } else {
        println!("File does not exist. Do you want to create a new file? (y/n)");
        let mut create_new = String::new();
        io::stdin().read_line(&mut create_new).expect("Failed to read line");
        if create_new.trim().eq_ignore_ascii_case("y") {
            file_content.clear();
            println!("New file created. You can now add lines and save the file.");
            Some(file_name)  // Return the new file name
        } else {
            println!("File not opened.");
            None  // No file name, return None
        }
    }
}

fn display_content(file_content: &[String]) {
    if file_content.is_empty() {
        println!("File is empty.");
    } else {
        println!("File content:");
        for (index, line) in file_content.iter().enumerate() {
            println!("{}: {}", index + 1, line);
        }
    }
}

fn add_line(file_content: &mut Vec<String>, x: String) {
    // println!("Enter the line to add:");
    // let mut new_line = String::new();
    let new_line = x;
    // io::stdin().read_line(&mut new_line).expect("Failed to read line");
    file_content.push(new_line.trim().to_string());
    println!("Line added.");
}

fn delete_line(file_content: &mut Vec<String>, x: String) {
    display_content(file_content);
    // println!("Enter the line number to delete:");
    // let mut line_number = String::new();
    let line_number = x;
    // io::stdin().read_line(&mut line_number).expect("Failed to read line");
    let line_number: usize = line_number.trim().parse().expect("Please enter a valid number");

    if line_number > 0 && line_number <= file_content.len() {
        file_content.remove(line_number - 1);
        println!("Line deleted.");
    } else {
        println!("Invalid line number.");
    }
}

fn write_file(file_name: &str, file_content: &[String]) {
    let mut file = File::create(file_name).expect("Unable to create file");
    for line in file_content {
        writeln!(file, "{}", line).expect("Unable to write line");
    }
    println!("File written successfully.");
}
