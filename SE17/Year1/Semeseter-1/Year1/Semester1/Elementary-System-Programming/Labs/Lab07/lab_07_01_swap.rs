// lab1_swap.rs
// Lab 1: Generic Container Swapper

fn swap_elements<T>(a: Vec<T>, b: Vec<T>) -> (Vec<T>, Vec<T>) {
    (b, a)
}

fn main() {
    // Example 1
    let vec1 = vec![1, 2, 3];
    let vec2 = vec![4, 5, 6];
    let (out1, out2) = swap_elements(vec1, vec2);
    println!("{:?} {:?}", out1, out2); // [4, 5, 6] [1, 2, 3]

    // Example 2
    let v3 = vec!["a", "b", "c"];
    let v4 = vec!["x", "y", "z"];
    let (o3, o4) = swap_elements(v3, v4);
    println!("{:?} {:?}", o3, o4); // ["x","y","z"] ["a","b","c"]

    // Example 3
    let v5 = vec![1.1, 2.2, 3.3];
    let v6 = vec![4.4, 5.5, 6.6];
    let (o5, o6) = swap_elements(v5, v6);
    println!("{:?} {:?}", o5, o6); // [4.4, 5.5, 6.6] [1.1, 2.2, 3.3]
}
