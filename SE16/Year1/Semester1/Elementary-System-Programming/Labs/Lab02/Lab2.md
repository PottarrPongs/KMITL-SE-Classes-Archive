# Rust Lab 2 (10/07/2024)

## 1. Write a Rust Program that:

1. Prompts the user to enter two names: one for Player 1 and one for Player 2.
2. Prints the names in two different formatted patterns: one vertical and one horizontal, using loops to print the border of asterisks.

### Example:
If the user inputs the names "Mike" for Player 1 and "Leo" for Player 2, the output should be:

Vertical Pattern:
```
******************
*                *
* Player 1: Mike *
*                *
******************
*                *
* Player 1: Leo  *
*                *
******************
```


Horizontal Pattern:
```
**********************************
*                *               *
* Player 1: MIke * Player 2: Leo *
*                *               *
**********************************
```

### Hint:

Read string:

```rust
io::stdin().read_line(&mut playerl).expect("Fai1ed to read");
```

Length of string:

```rust
player.len()
```

<hr>

## 2. Write a Rust program that simulates a simple employee data processing system:

1. Prompts the user to enter the salaries of 5 employees and stores them in an array.
2. Prompts the user to enter employee details as a tuple consisting of the employee's name age and salary.
3. Prints the all employee details in a formatted message. Name: <name> Age: <age> Salary: <salarp
4. Prints the total salary, average salary, employee with the highest salary and employee with oldest.

### Example:
Output should be:
```
Employee 1: Name = "Alice", Age = 30, Salary = 30000
Employee 2: Name = "Bob", Age = 41, Salary = 45000
Employee 3: Name = "Charlie", Age = 38, Salary = 50000
Employee 4: Name = "Diana", Age = 43, Salary = 35000
The employee with the highest salary is: Charlie with a salary of 50000
The oldest employee is: Diana, 43 years old
```

<hr>

Author: Pottarrพงศ์  
Source: KMITL SE Rust Lab