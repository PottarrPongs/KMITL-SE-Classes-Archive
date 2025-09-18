// Lab 3: Generic Data Analysis Tool

// 1) Trait for simple analysis
trait SimpleAnalyzable {
    fn mean(&self) -> f64;
}

// 2) Implement SimpleAnalyzable for Vec<f64>
impl SimpleAnalyzable for Vec<f64> {
    fn mean(&self) -> f64 {
        if self.is_empty() {
            return 0.0; // avoid division by zero, simple and student-friendly
        }
        let sum: f64 = self.iter().sum();
        sum / self.len() as f64
    }
}

// 3) Simple dataset struct
#[derive(Debug)]
struct SimpleDataSet {
    data: Vec<f64>,
}

impl SimpleDataSet {
    fn new(data: Vec<f64>) -> Self {
        SimpleDataSet { data }
    }

    // 4) Filter into a NEW dataset using a closure predicate
    fn filter<F>(&self, predicate: F) -> Self
    where
        F: Fn(&f64) -> bool,
    {
        let filtered_data: Vec<f64> = self.data.iter().copied().filter(predicate).collect();
        SimpleDataSet::new(filtered_data)
    }
}

// 5) Implement SimpleAnalyzable for SimpleDataSet (delegate to inner Vec<f64>)
impl SimpleAnalyzable for SimpleDataSet {
    fn mean(&self) -> f64 {
        self.data.mean()
    }
}

fn main() {
    println!("=== Lab 3: Generic Data Analysis Tool ===");

    // Case 1: Vec<f64>
    let v = vec![1.0, 2.0, 3.0, 4.0, 5.0];
    println!("Vec: {:?}, mean = {}", v, v.mean()); // expected: 3.0

    // Case 2: SimpleDataSet (same data)
    let data = SimpleDataSet::new(vec![1.0, 2.0, 3.0, 4.0, 5.0]);
    println!("Data: {:?}, mean = {}", data, data.mean()); // expected: 3.0

    // Case 3: Filter (> 2.5) then mean
    let filtered = data.filter(|&x| x > 2.5); // keeps [3.0, 4.0, 5.0]
    println!("Filtered data (> 2.5): {:?}", filtered);
    println!("Filtered mean: {}", filtered.mean()); // expected: 4.0

    // Case 4: Empty dataset
    let empty_data = SimpleDataSet::new(vec![]);
    println!("Empty dataset: {:?}, mean = {}", empty_data, empty_data.mean()); // expected: 0.0
}
