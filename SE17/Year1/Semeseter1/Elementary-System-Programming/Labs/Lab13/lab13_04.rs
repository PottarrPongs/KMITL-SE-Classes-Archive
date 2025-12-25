// Lab 4 — let else, while let, if let
// Run: rustc p4_lets.rs -o p4_lets && ./p4_lets

fn first_hex_digit(maybe: Option<String>) -> Result<u32, String> {
    let Some(s) = maybe else { return Err("none".into()); };
    if s.is_empty() {
        return Err("empty".into());
    }
    let c = s.chars().next().unwrap();
    let val = match c {
        '0'..='9' => (c as u32) - ('0' as u32),
        'a'..='f' => 10 + (c as u32 - 'a' as u32),
        'A'..='F' => 10 + (c as u32 - 'A' as u32),
        _ => return Err("not-hex".into()),
    };
    Ok(val)
}

fn pop_all(s: &mut String) -> Vec<char> {
    let mut out = Vec::new();
    while let Some(ch) = s.pop() {
        out.push(ch);
    }
    out
}

fn parse_u8(s: &str) -> Option<u8> {
    s.parse::<u8>().ok()
}

fn print_parse_u8(s: &str) {
    if let Some(n) = parse_u8(s) {
        println!("parse_u8: n={}", n);
    }
}

fn fmt_char_vec_no_spaces(v: &Vec<char>) -> String {
    // Format as "['3','2','1','c','b','a']" (no spaces)
    let mut out = String::from("[");
    for (i, ch) in v.iter().enumerate() {
        if i > 0 { out.push(','); }
        out.push('\''); out.push(*ch); out.push('\'');
    }
    out.push(']');
    out
}

fn main() {
    // Fixed calls and exact prints
    println!("first_hex(Some(\"BEEF\"))={:?}", first_hex_digit(Some("BEEF".to_string())));
    println!("first_hex(Some(\"\"))={:?}", first_hex_digit(Some("".to_string())));
    println!("first_hex(None)={:?}", first_hex_digit(None));

    let mut s = "abc123".to_string();
    let popped = pop_all(&mut s);
    println!("pop_all(\"abc123\")={}", fmt_char_vec_no_spaces(&popped));
    println!("after_pop=\"{}\"", s);

    print_parse_u8("42"); // prints
    print_parse_u8("x");  // prints nothing

    // Self-tests
    let t_hex = first_hex_digit(Some("BEEF".into())) == Ok(11);
    let t_empty = first_hex_digit(Some("".into())) == Err("empty".into());
    let t_none = first_hex_digit(None) == Err("none".into());
    let t_not_hex = first_hex_digit(Some("Z".into())) == Err("not-hex".into());

    let mut s2 = "z9".to_string();
    let _ = pop_all(&mut s2);
    let t_pop_empty = s2.is_empty();

    println!("TEST: hex-BEEF-11 -> {}", if t_hex {"PASS"} else {"FAIL"});
    println!("TEST: empty/none/not-hex -> {}", if t_empty && t_none && t_not_hex {"PASS"} else {"FAIL"});
    println!("TEST: pop_all-empties -> {}", if t_pop_empty {"PASS"} else {"FAIL"});
}
