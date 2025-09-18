# Rust Lab 3 (17/07/2024)

## 1. Warehouse Inventory Management

Develop a Rust program to manage inventory in a warehouse. The system  should track products using tuples (ID. name, quantity) and store them in a vector.

#### Requirements

1.1  Product Representation: Each product is represented by a tuple: (u32, String, u32) for (ID, name, quantity).
1.2 Inventory Management:
- Use a vector to store the list of products in the warehouse.
- Implement the following functionalities:
1. Add a new product (ensure unique ID).
2. Update the stock quantity of an existing product.
3. Remove a product by its ID.
4. List all products in the inventory
5. Exit program

1.3 User Interaction: Create a
driven interface where users can select operations (e.g., 1 for add, 2 for update, etc.).

1.4 Bonus Points (Optional): Input validation: Implement robust error handling for invalid user inputs (e.g., 
non-numeric input, invalid product IDs).
1.5 Example Menu:
``` 
Warehouse Inventory Management:
1. Add New Product
2. Update Stock Quantity
3. Remove Product
4. List All Products
5. Exit
```

### Hints:

vector of tuple:
```rust
let mut warehouse: Vec<(u32, String, u32)> = Vec::new();
```

#### Choice input:

```rust
io::stdin().read_line(&mut choice).expect("Failed to read line");
let choice: u32 = match choice.trim().parse() {
    Ok(num) => num,
    Err(_) {
        println!("lnvalid input. Please enter a number.");
        0
    }
```

#### ld check and adding:

```rust
let mut id_exists = false;
for (existing_id, _, _) in &warehouse { // Iterate through the warehouse
    if *existing_id == id { // Check if the ID already exists
        id_exists = true;
        break; // Exit the loop early if found
    }
}
if id_exists {
    println!("Product ID already exists.");
    continue;
} else {
    warehouse.push((id, name, quantity));
    println!("Product added successfully.");
}
```

#### Item removal:

```rust
let mut 1 = 0; //Index for iteration
while 1 < warehouse.len() {
    if warehouse[i].0 == id { // Check if ID matches at current index
        warehouse.remove(i);
        println!("Product removed successfully.");
        break; // Exit loop after removal
    } else {
        i += 1; // Move to the next index
    }
}
```

#### String input:

```rust
let mut name = String::new();
io::stdin().read_line(&mut name).expect("Failed to read line");
let name = name.trim().to_string();
```

---

Author: Pottarrพงศ์  
Source: KMITL SE Rust Lab
