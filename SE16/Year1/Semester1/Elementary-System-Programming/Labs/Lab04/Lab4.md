# Rust Lab 4 (24/07/2024)

## 1. Matrices Multiplication

Write a Rust function that multiplies a 2x3 matrix by a 3x3 matrix. The function should accept two matrices as inputs: the first matrix A is of size 2x3, and the second matrix B is of size 3x3. The function should return a 2x3 matrix that is the result of the matrix multiplication.

-   The function should correctly compute the matrix multiplication. Recall that matrix multiplication is defined such that if C = A \* B, then is the dot product of the i-th row of A and the j-th column of B.

-   Use nested loops to iterate through rows of A and columns of B to compute the entries of the resulting matrix C.

### Example:

#### Input:

```rust
fn multiply_matrices(a: [[i32; 3]; 2], b: &[[i32; 3; 3]) ->[[i32; 3]; 2]
```

---

## 2. Matrices Multiplication

Create a Rust program that generates and displays Pascal's Triangle using recursive functions.

### Requirements

-   Prompt the user to enter a number 'n' between 1 and 9 (inclusive).
-   Validate the input and re-prompt if the input is invalid.

### Pascal Triangle Generation:

-   Implement a recursive function 'pascal(row, col)' that calculates the value at any given position in Pascal's Triangle.
-   The function should return 1 for the edges of the triangle and use recursion for inner values.

### Triangle Display:

-   Create a function 'print_pascal_row(n, row)' that prints a single row of the triangle.
-   Implement proper spacing for alignment of the triangle.
-   Each number should be displayed with a width of 4 characters for readability.

### Main Program:

-   In the main function, get user input and display the result.
-   Include appropriate comments to explain your logic.

### Constrainst:

-   Use only the standard Rust library.
    Do not use any additional data structures to store the triangle values.

### Example Output:

For input n = 5, the output should look similar to this:

```
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
```

#### Hint:

```rust
fn main() {
    //Get input from user
    let n: usize = loop {
        println!("Enter a number between 1 and 9:");
        let mut input = String::new();
        io::stdin().read_line(&mut input).expect("Failed to read line");
        match input.trim().parse() {
            Ok(num) if (1..=9).contains(&num) => break num,
            _ => println!("Please enter a valid number between 1 and 9.");
        };
    };
    //Print pascal triangle
    for row in 0..n {
        //Your code here
    }
}
```

---

Author: Pottarrพงศ์  
Source: KMITL SE Rust Lab
