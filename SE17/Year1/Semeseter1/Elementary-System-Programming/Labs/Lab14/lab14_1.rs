use std::fmt::Debug;

trait ShapeProperties {
    fn area(&self) -> f64;
    fn perimeter(&self) -> f64;
}

#[derive(Debug)]
struct Rectangle {
    width: f64,
    height: f64,
}

#[derive(Debug)]
struct Circle {
    radius: f64,
}

impl ShapeProperties for Rectangle {
    fn area(&self) -> f64 {
        self.width * self.height
    }
    fn perimeter(&self) -> f64 {
        2.0 * (self.width + self.height)
    }
}

impl ShapeProperties for Circle {
    fn area(&self) -> f64 {
        std::f64::consts::PI * self.radius * self.radius
    }
    fn perimeter(&self) -> f64 {
        2.0 * std::f64::consts::PI * self.radius
    }
}

fn print_details<T>(shape: &T)
where
    T: ShapeProperties + Debug,
{
    println!("Shape: {:?}", shape);
    println!("Area: {}", shape.area());
    println!("Perimeter: {}", shape.perimeter());
}

fn main() {
    let rect = Rectangle { width: 10.0, height: 5.0 };
    let circle = Circle { radius: 7.5 };

    println!("--- Rectangle ---");
    print_details(&rect);

    println!("\n--- Circle ---");
    print_details(&circle);
}
