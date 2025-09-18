use std::io;

fn main() {

    let mut employees: [(String, u8, f32); 5] = [
        (String::new(), 0, 0.0),
        (String::new(), 0, 0.0),
        (String::new(), 0, 0.0),
        (String::new(), 0, 0.0),
        (String::new(), 0, 0.0)
    ];


    let mut input = String::new();
    for i in 0..5 {
        println!("Please enter employee {} name: ", i+1);
        io::stdin().read_line(&mut input).expect("Failed to read.");
        employees[i].0 = input.trim().to_string();
        input.clear();
        println!("Please enter employee {} age: ", i+1);
        io::stdin().read_line(&mut input).expect("Failed to read.");
        employees[i].1 = input.trim().to_string().parse().expect("Invalid Age");
        input.clear();
        println!("Please enter employee {} salary: ", i+1);
        io::stdin().read_line(&mut input).expect("Failed to read.");
        employees[i].2 = input.trim().to_string().parse().expect("Invalid Salary");
        input.clear();
    }

    println!("{:?}", employees);
    
    let mut oldest = 0;
    let mut emp_oldest = 0;
    let mut highest_sal = 0.0;
    let mut emp_highest_sal = 0;
    
    for i in 0..5 {
        println!("Employee {}: Name = {}, Age = {}, Salary = {}.", i+1, employees[i].0, employees[i].1, employees[i].2);
        if employees[i].1 > employees[emp_oldest].1 {
            oldest = employees[i].1;
            emp_oldest = i;
        }
        if employees[i].2 > employees[emp_highest_sal].2 {
            highest_sal = employees[i].2;
            emp_highest_sal = i;
        }
    }

    println!("The employee with the highest salary is {}. With the value of salary of {} THB.", employees[emp_highest_sal].0, highest_sal);
    println!("The oldest employee is {} with the age of {} years old.", employees[emp_oldest].0, oldest);
    
}