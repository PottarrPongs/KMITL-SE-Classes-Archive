use std::fmt;
use std::ops::Add;

#[derive(Debug, Copy, Clone)]
struct Vector2D {
    x: f32,
    y: f32,
}

impl Add for Vector2D {
    type Output = Self;

    fn add(self, rhs: Self) -> Self::Output {
        Self {
            x: self.x + rhs.x,
            y: self.y + rhs.y,
        }
    }
}

impl fmt::Display for Vector2D {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "({}, {})", self.x, self.y)
    }
}

fn main() {
    let v1 = Vector2D { x: 5.0, y: 2.0 };
    let v2 = Vector2D { x: -1.0, y: 3.0 };

    let v3 = v1 + v2; // uses Add

    println!("Vector 1: {}", v1);    // uses Display
    println!("Vector 2: {}", v2);
    println!("v1 + v2 = {}", v3);
    println!("Debug format: {:?}", v3); // uses derived Debug
}
