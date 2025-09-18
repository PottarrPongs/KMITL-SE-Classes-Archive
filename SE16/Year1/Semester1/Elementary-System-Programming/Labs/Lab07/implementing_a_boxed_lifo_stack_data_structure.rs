use std::fmt;

// Define the BoxedStack struct
struct BoxedStack {
    data: Box<Vec<i32>>,  // Boxed vector to hold stack elements on the heap
}

impl BoxedStack {
    // Creates a new, empty BoxedStack
    fn new() -> Self {
        BoxedStack {
            data: Box::new(Vec::new())
        }
    }

    // Adds a new integer to the top of the stack
    fn push(&mut self, value: i32) {
        (*self.data).push(value);
    }

    // Removes and returns the top element of the stack
    fn pop(&mut self) -> Option<i32> {
        if (*self.data).len() > 0 {
            println!("Popped {} from the stack",&(*self.data)[(*self.data).len()-1]);
            Some((*self.data).pop()?)
        } else {
            None
        }
    }

    // Returns a reference to the top element of the stack without removing it
    fn peek(&self) -> Option<&i32> {
        let vec_len = (*self.data).len();
        if vec_len > 0 {
            Some(&(*self.data)[vec_len-1])
        } else {
            None
        }
    
    }

    // Returns true if the stack is empty, false otherwise
    fn is_empty(&self) -> bool {
        if (*self.data).is_empty() {
            true
        } else {
            false
        }
    }

    // Prints the contents of the stack from top to bottom
    fn print_stack(&self) {
        println!("Stack contents: {:?}", (*self.data));
    }
}

// Implementing the Debug trait for BoxedStack
impl fmt::Debug for BoxedStack {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        f.debug_struct("BoxedStack").field("data", &self.data).finish()
    }
}

fn main() {
    // Create a new BoxedStack
    let mut stack = BoxedStack::new();

    // Push a few integers onto the stack
    println!("Pushing 10 onto the stack.");
    stack.push(10);
    println!("Pushing 20 onto the stack.");
    stack.push(20);
    println!("Pushing 30 onto the stack.");
    stack.push(30);

    // Print the stack contents
    stack.print_stack();

    // Peek at the top element and print it
    stack.peek();

    // Pop elements off the stack one by one, printing the stack contents after each pop
    stack.pop();
    stack.print_stack();
    stack.pop();
    stack.print_stack();
    stack.pop();
    stack.print_stack();

    // Check if the stack is empty and print the result
    println!("Is the stack empty? {}", stack.is_empty());
}
