// use std::ptr;

fn factorial(n: i32) -> i32 {

    if n == 0 {
        println!("Calculating factorial({})", n);
        println!("Value: {} Address: {:p}", n, &n);
        1 
    } else {
        println!("Calculating factorial({})", n);
        println!("Value: {} Address: {:p}", n, &n);
        n * factorial(n-1)
    }
}

fn main() {
    let answer = factorial(5);
    println!("Factorial value: {}", answer);
}