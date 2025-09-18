fn swap_elements<T>(a: Vec<T>, b: Vec<T>) -> (Vec<T>, Vec<T>) {
    let vec_a: Vec<T> = Vec::from(a);
    let vec_b: Vec<T> = Vec::from(b);

    (vec_b, vec_a)
}

fn main() {
    let vec1 = vec![1,2,3];
    let vec2 = vec![4,5,6];
    let result = swap_elements(vec1, vec2);
    println!("{:?} {:?}", result.0, result.1);
}