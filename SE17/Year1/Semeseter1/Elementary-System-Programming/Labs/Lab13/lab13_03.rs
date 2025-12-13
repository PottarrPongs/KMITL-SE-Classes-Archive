// Lab 3 — Destructuring & @ bindings
// Run: rustc p3_destructure.rs -o p3_destructure && ./p3_destructure

fn quadrant(p: (i32,i32)) -> &'static str {
    match p {
        // Use tuple destructuring + at-binding/range/guards
        (x @ 1..=i32::MAX, y) if y > 0 => "I",
        (x @ i32::MIN..=-1, y) if y > 0 => { let _ = x; "II" },
        (x @ i32::MIN..=-1, y) if y < 0 => { let _ = x; "III" },
        (x @ 1..=i32::MAX, y) if y < 0 => { let _ = x; "IV" },
        _ => "axis",
    }
}

enum Token { Number(i64), Ident(String), Symbol(char) }

fn classify(t: Token) -> &'static str {
    match t {
        Token::Number(n @ 0..=9) => {
            let _keep = n; // demonstrate keeping matched value
            "small-int"
        }
        Token::Number(_) => "big-int",
        Token::Ident(s) if s.len() > 8 => "ident-long",
        Token::Ident(_) => "ident",
        Token::Symbol(_) => "symbol",
    }
}

fn main() {
    // Fixed list (order matters)
    let pts: Vec<(i32,i32)> = vec![(3,4),(-5,0),(-1,7),(-2,-3),(6,-4),(0,0),(0,9),(8,0)];
    for (x,y) in &pts {
        println!("quadrant({},{})={}", x, y, quadrant((*x,*y)));
    }

    // Token demo lines (order fixed)
    println!("classify(Number(7))={}", classify(Token::Number(7)));
    println!("classify(Number(42))={}", classify(Token::Number(42)));
    println!("classify(Ident(abcdefghijk))={}", classify(Token::Ident("abcdefghijk".to_string())));
    println!("classify(Symbol(+))={}", classify(Token::Symbol('+')));

    // Self-tests
    let covered = quadrant((1,1))=="I"
        && quadrant((-1,1))=="II"
        && quadrant((-1,-1))=="III"
        && quadrant((1,-1))=="IV"
        && quadrant((0,2))=="axis";
    let small_vs_big = classify(Token::Number(9))=="small-int" && classify(Token::Number(10))=="big-int";
    let ident_long = classify(Token::Ident("abcdefghij".to_string()))=="ident-long";
    let symbol = classify(Token::Symbol('#'))=="symbol";

    println!("TEST: all-quadrants-and-axis-covered -> {}", if covered {"PASS"} else {"FAIL"});
    println!("TEST: small-vs-big-int -> {}", if small_vs_big {"PASS"} else {"FAIL"});
    println!("TEST: ident-long -> {}", if ident_long {"PASS"} else {"FAIL"});
    println!("TEST: symbol -> {}", if symbol {"PASS"} else {"FAIL"});
}
