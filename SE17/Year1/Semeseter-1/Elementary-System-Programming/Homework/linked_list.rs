use std::{fmt::Debug};

// Stack implement in Linked List
#[derive(Clone, Debug)]
enum Node {
    Cons(i32, Box<Node>),
    Nil
}

struct BoxStack {
    top: Node
}

impl Debug for BoxStack {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        f.debug_struct("BoxStack")
            .field("Top", &self.top)
            .finish()
    }
}

impl BoxStack {
    fn new() -> Self {
        BoxStack {
            top: Node::Nil
        }
    }
    fn push(&mut self, value: i32) {
        match &self.top {
            Node::Nil => {
                self.top = Node::Cons(value, Box::new(Node::Nil));
            }
            Node::Cons(x,y) => {
                let x = *x;
                self.top = Node::Cons(value, Box::new(Node::Cons(x, y.clone())));
            }
        }
    }
    fn pop(&mut self) -> Option<i32> {
        match &self.top {
            Node::Nil => None,
            Node::Cons(x, y) => {
                let x = *x;
                self.top = *y.clone();
                Some(x)
            }
        }
    }
    fn peek(&self) -> Option<&i32> {
        match &self.top {
            Node::Nil => None,
            Node::Cons(x, _) => Some(x)
        }
    }
    fn is_empty(&self) -> bool {
        match self.top {
            Node::Nil => true,
            Node::Cons(_,_) => false,
        }
    }
    fn print_stack(&self) {
        print!("Stack contents: ");
        self.print_stack_helper(&self.top);
        println!()
    }
    fn print_stack_helper(&self, prev: &Node) {
        match prev {
            Node::Nil => print!("Nil"),
            Node::Cons(x, y) => {
                print!("{x} -> ");
                self.print_stack_helper(y);
            }
        }
    }
}

fn main() {
    let mut stack = BoxStack::new();
    println!("Pushing 10 onto the stack.");
    stack.push(10);
    println!("Pushing 20 onto the stack.");
    stack.push(20);
    println!("Pushing 30 onto the stack.");
    stack.push(30);
    stack.print_stack();
    let temp = match stack.peek() {
        None => "Nil",
        Some(x) => &(x.to_string())
    };
    println!("Top of the stack: {}", temp);
    let temp = match stack.pop() {
        None => "Nil",
        Some(x) => &(x.to_string())
    };
    println!("Popped {} from the stack.", temp);
    stack.print_stack();
    let temp = match stack.pop() {
        None => "Nil",
        Some(x) => &(x.to_string())
    };
    println!("Popped {} from the stack.", temp);
    stack.print_stack();
    let temp = match stack.pop() {
        None => "Nil",
        Some(x) => &(x.to_string())
    };
    println!("Popped {} from the stack.", temp);
    stack.print_stack();
    println!("Is thr stack empty? {}", stack.is_empty());
}
