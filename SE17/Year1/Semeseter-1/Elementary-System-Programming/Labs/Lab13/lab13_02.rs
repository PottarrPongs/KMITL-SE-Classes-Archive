// Lab 2 — Command Handler (match, ranges, guard, constant)
// Run: rustc p2_cmd.rs -o p2_cmd && ./p2_cmd

const QUIT: char = 'q';

fn handle(key: char) -> &'static str {
    match key {
        QUIT => "quit",
        'a' | 's' | 'w' | 'd' => "move",
        '0'..='9' => "digit",
        k if k.is_lowercase() => "lowercase",
        _ => "_other",
    }
}

fn main() {
    // Prepared inputs (fixed order)
    let keys = ['q','a','7','x','%','9','A','d'];
    for k in keys {
        println!("handle('{}') => {}", k, handle(k));
    }

    // Self-tests
    let t_quit = handle('q') == "quit";
    // NOTE: .iter() yields &char on some toolchains; deref to pass char to handle()
    let t_move = ['a','s','w','d'].iter().all(|&k| handle(k) == "move");
    let t_digit = handle('7') == "digit" && handle('9') == "digit";
    let t_lower = handle('x') == "lowercase";

    println!("TEST: quit-constant -> {}", if t_quit {"PASS"} else {"FAIL"});
    println!("TEST: wasd-move -> {}", if t_move {"PASS"} else {"FAIL"});
    println!("TEST: digit-7-and-9 -> {}", if t_digit {"PASS"} else {"FAIL"});
    println!("TEST: lowercase-x -> {}", if t_lower {"PASS"} else {"FAIL"});
}
