use std::io;

fn pascal(row: u8, col: u8) -> u8{
    if col == 0{
        1
    } else if col == row {
        1
    } else {
        pascal(row-1, col-1) + pascal(row-1, col)
    }
}

fn print_pascal(rows: u8, cols: u8) {
        for _j in 0..cols-rows {
            print!("  ");
        }
        for col in 0..=rows {
            let ans = pascal(rows as u8, col as u8);
            print!("{:<4}", ans);
        }
        println!("");
}

fn main() {
    let n: usize = loop {
        println!("Enter from 1 to 9: ");
        let mut input = String::new();
        io::stdin().read_line(&mut input).expect("Failed to read.");
        match input.trim().parse() {
            Ok(num) if (1..=9).contains(&num) => break num,
            _ => {
                println!("Please enter from 1 to 9 only.");
            }
        };
    };
    println!("");

    for m in 0..n {
        print_pascal(m as u8, n as u8);
    }
}