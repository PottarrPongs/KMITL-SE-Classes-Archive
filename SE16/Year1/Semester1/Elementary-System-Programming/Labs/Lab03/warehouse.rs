use std::io;

fn main() {
    println!("Welcome to the warehouse!");
    println!("Action list: ");
    println!("1 => Add product");
    println!("2 => Update product");
    println!("3 => Remove product");
    println!("4 => List all products");
    println!("5 => Exit the warehouse");

    
    let mut warehouse: Vec<(u32, String, u32)> = Vec::new();
    loop {
        let mut choice: String = String::new();
        println!("Enter an action code: ");
        io::stdin().read_line(&mut choice).expect("Failed to read.");
        
        let choice: u32 = match choice.trim().to_string().parse() {
            Ok(num) => num,
            Err(_) => {
                println!("Invalid action.");
                0
            }
        };

        match choice {

            1 =>{
                println!("You chose ADD.");
                
                let mut input: String = String::new();
                
                println!("Enter product ID");
                io::stdin().read_line(&mut input).expect("Failed to read.");
                let id: u32 = match input.trim().parse() {
                    Ok(num) => num,
                    Err(_) => {
                        println!("Please enter number only.");
                        continue;
                    }
                };
                input.clear();
                println!("Enter product name");
                io::stdin().read_line(&mut input).expect("Failed to read.");
                let name: String = input.trim().to_string();
                input.clear();
                println!("Enter product added");
                io::stdin().read_line(&mut input).expect("Failed to read.");
                let quantity: u32 = match input.trim().parse() {
                    Ok(num) => num,
                    Err(_) => {
                        println!("Please enter number only.");
                        continue;
                    }
                };
                input.clear();

                let mut id_exists = false;
                for (existing_id, _, _) in &warehouse {
                    if *existing_id == id {
                        id_exists = true;
                        break;
                    }
                }
                
                if id_exists {
                    println!("Product ID already exists.");
                    continue;
                } else {
                    warehouse.push((id, name, quantity));
                    println!("Product added successfully.");
                }
            }

            2 => {
                println!("You chose UPDATE.");
                
                let mut input: String = String::new();
                
                println!("Enter product ID");
                io::stdin().read_line(&mut input).expect("Failed to read.");
                let id: u32 = match input.trim().parse() {
                    Ok(num) => num,
                    Err(_) => {
                        println!("Please enter number only.");
                        continue;
                    }
                };
                input.clear();
                println!("Enter product added");
                io::stdin().read_line(&mut input).expect("Failed to read.");
                let quantity: u32 = match input.trim().parse() {
                    Ok(num) => num,
                    Err(_) => {
                        println!("Please enter number only.");
                        continue;
                    }
                };
                input.clear();
                if warehouse.len() == 0 {
                    println!("Nothing to update.");
                }
                for i in 0..warehouse.len() {
                    if warehouse[i].0 == id {
                        let _ = warehouse[i].2 == quantity;
                    }
                }
                
            }

            3 => {
                println!("You chose REMOVE.");
                
                let mut input: String = String::new();
                
                println!("Enter product ID:");
                io::stdin().read_line(&mut input).expect("Failed to read.");
                let id: u32 = match input.trim().parse() {
                    Ok(num) => num,
                    Err(_) => {
                        println!("Please enter number only.");
                        continue;
                    }
                };
                input.clear();
                if warehouse.len() == 0 {
                    println!("Nothing to remove.");
                }
                for i in 0..warehouse.len() {
                    
                    if warehouse[i].0 == id {
                        warehouse.remove(i);
                        println!("Product removed successfully");
                        break;
                    } else {
                        println!("No prduct with this ID found.");
                    }
                }

            }

            4 => {
                println!("You chose LIST.");
                if warehouse.len() == 0 {
                    println!("Nothing in the stock.");
                }
                for item in 0..warehouse.len() {
                    println!("ID: {}, Name: {}, Quantity: {}", warehouse[item].0, warehouse[item].1, warehouse[item].2);
                    continue;
                }               
            }

            5 => {
                println!("You chose EXIT.");
                break;
    
            }

            other_number => {
                println!("Number {} is not for action.", other_number);
            }
        }

    }
    
}