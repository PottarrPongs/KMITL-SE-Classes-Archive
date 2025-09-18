fn mult(a: [[i32; 3]; 2], b: [[i32; 3]; 3]) -> [[i32; 3]; 2] {
    let mut c: [[i32; 3]; 2] = [[0, 0, 0], [0, 0, 0]];
    for i in 0..a.len() {
        let mut arr: [i32; 3] = [0, 0, 0];
        for j in 0..a[0].len() {
            let mut result = 0;
            for l in 0..b[0].len() {
                let value = a[i][l] * b[l][j];
                result += value;
            }
            arr[j] = result;
        }
        c[i] = arr;
    }
    return c;
}

fn main() {
    let a: [[i32; 3]; 2] = [[1, 2, 3], [4, 5, 6]];
    let b: [[i32; 3]; 3] = [[7, 8, 9], [10, 11, 12], [13, 14, 15]];
    // let mut c:[[i32; 3]; 2] = [[0,0,0,],[0,0,0]];

    let c = mult(a, b);

    for h in 0..c.len() {
        println!("{:?}", c[h]);
    }
}
