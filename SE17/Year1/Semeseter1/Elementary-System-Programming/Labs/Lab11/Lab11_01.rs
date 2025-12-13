// Lab 1: Creating Custom Iterators

// 1. Create a struct named Fibonacci with fields for the current and next numbers.
// Hint: Use u64 for fields to avoid overflow in early terms. [cite: 21]
struct Fibonacci {
    current: u64,
    next: u64,
}

// 3. Implement a constructor (new()) for Fibonacci that initializes with 0 and 1. 
impl Fibonacci {
    fn new() -> Fibonacci {
        Fibonacci { current: 0, next: 1 }
    }
}

// 2. Implement the Iterator trait for Fibonacci. [cite: 12]
impl Iterator for Fibonacci {
    type Item = u64;

    // The next() method should return the current Fibonacci number [cite: 13]
    // and update the state to generate the next number. [cite: 14]
    fn next(&mut self) -> Option<Self::Item> {
        let new_next = self.current + self.next;
        let current_val = self.current;
        
        self.current = self.next;
        self.next = new_next;
        
        Some(current_val)
    }
}

fn main() {
    println!("--- Lab 1 Output ---");
    // 4. In the main function, use the iterator to print the first 10 Fibonacci numbers. [cite: 17]
    // Format as "Fibonacci N: value", using 1-based indexing for N. [cite: 18]
    let fib = Fibonacci::new();
    for (i, val) in fib.take(10).enumerate() {
        println!("Fibonacci {}: {}", i + 1, val);
    }
}