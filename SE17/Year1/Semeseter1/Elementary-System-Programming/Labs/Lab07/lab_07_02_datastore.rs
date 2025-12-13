// Lab 2: Generic Data Storage System

// Generic struct to hold items of type T
#[derive(Debug)]
struct DataStore<T> {
    items: Vec<T>,
}

impl<T> DataStore<T> {
    // Create a new empty DataStore
    fn new() -> Self {
        DataStore { items: Vec::new() }
    }

    // Add an item to the store
    fn add_item(&mut self, item: T) {
        self.items.push(item);
    }

    // Remove item at index and return it
    fn remove_item(&mut self, index: usize) -> Option<T> {
        if index < self.items.len() {
            Some(self.items.remove(index))
        } else {
            None
        }
    }

    // Get reference to item at index
    fn get_item(&self, index: usize) -> Option<&T> {
        self.items.get(index)
    }

    // Find first item matching predicate
    fn find_item<F>(&self, predicate: F) -> Option<&T>
    where
        F: Fn(&T) -> bool,
    {
        self.items.iter().find(|item| predicate(item))
    }

    // Get number of items
    fn len(&self) -> usize {
        self.items.len()
    }

    // Check if store is empty
    fn is_empty(&self) -> bool {
        self.items.is_empty()
    }
}

// Enum for different data types
#[derive(Debug)]
enum DataType<T> {
    Number(T),
    Text(String),
    Boolean(bool),
}

// Implement display formatting for DataType
impl<T: std::fmt::Display> std::fmt::Display for DataType<T> {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        match self {
            DataType::Number(n) => write!(f, "Number({})", n),
            DataType::Text(s) => write!(f, "Text(\"{}\")", s),
            DataType::Boolean(b) => write!(f, "Boolean({})", b),
        }
    }
}

fn main() {
    // ================================
    // A) DataStore<DataType<i32>>
    // ================================
    let mut store_a = DataStore::<DataType<i32>>::new();

    // 1) Create + add
    store_a.add_item(DataType::Number(42));
    store_a.add_item(DataType::Number(7));
    store_a.add_item(DataType::Number(128));
    store_a.add_item(DataType::Text("Rust".to_string()));
    store_a.add_item(DataType::Boolean(true));

    // 2) Print count
    println!("[A] len={}, empty={}", store_a.len(), store_a.is_empty());

    // 3) Get by index
    match store_a.get_item(0) {
        Some(item) => println!("[A] get(0): {}", item),
        None => println!("[A] get(0): None"),
    }
    match store_a.get_item(99) {
        Some(item) => println!("[A] get(99): {}", item),
        None => println!("[A] get(99): None"),
    }

    // 4) Find by closure: first number > 100
    let found_a = store_a.find_item(|x| {
        if let DataType::Number(n) = x { *n > 100 } else { false }
    });
    match found_a {
        Some(item) => println!("[A] find(>100): {}", item),
        None => println!("[A] find(>100): None"),
    }

    // 5) Remove index 1 (should remove Number(7))
    println!("[A] remove(1): {:?}", store_a.remove_item(1));

    // 6) List all
    for (i, it) in store_a.items.iter().enumerate() {
        println!("[A] {i}: {}", it);
    }

    // ================================
    // B) DataStore<DataType<f64>>
    // ================================
    let mut store_b = DataStore::<DataType<f64>>::new();

    // 1) Create + add
    store_b.add_item(DataType::Number(3.14));
    store_b.add_item(DataType::Number(2.71));
    store_b.add_item(DataType::Text("pi".to_string()));
    store_b.add_item(DataType::Boolean(false));

    // 2) Get + Find
    match store_b.get_item(0) {
        Some(item) => println!("[B] get(0): {}", item),
        None => println!("[B] get(0): None"),
    }
    let found_b = store_b.find_item(|x| {
        if let DataType::Number(v) = x { *v >= 3.0 } else { false }
    });
    match found_b {
        Some(item) => println!("[B] find(>=3.0): {}", item),
        None => println!("[B] find(>=3.0): None"),
    }

    // 3) Remove tail
    if store_b.len() > 0 {
        println!("[B] remove(last): {:?}", store_b.remove_item(store_b.len() - 1));
    } else {
        println!("[B] remove(last): None (empty store)");
    }

    // 4) List all
    for (i, it) in store_b.items.iter().enumerate() {
        println!("[B] {i}: {}", it);
    }

    // ================================
    // C) DataStore<String>
    // ================================
    let mut s = String::from("Hello");
    s.push_str(" World");
    s.push('!');
    let s2 = format!("{} from Rust", s); // s is still usable if needed

    let mut store_c = DataStore::<String>::new();

    // 1) Create + add with String methods
    store_c.add_item(s2);
    store_c.add_item("functional".to_string());
    store_c.add_item("generics".to_string());

    // 2) Get + Find
    match store_c.get_item(0) {
        Some(item) => println!("[C] get(0): {:?}", item),
        None => println!("[C] get(0): None"),
    }
    let found_c = store_c.find_item(|t| t.contains("Rust"));
    match found_c {
        Some(item) => println!("[C] find(contains 'Rust'): {:?}", item),
        None => println!("[C] find(contains 'Rust'): None"),
    }

    // 3) Remove + modify + re-add
    if let Some(taken) = store_c.remove_item(0) {
        let modified = taken.replace("World", "โลก").to_uppercase();
        store_c.add_item(modified);
    } else {
        println!("[C] remove(0): None");
    }

    // 4) List all
    for (i, it) in store_c.items.iter().enumerate() {
        println!("[C] {i}: {:?}", it);
    }
}
