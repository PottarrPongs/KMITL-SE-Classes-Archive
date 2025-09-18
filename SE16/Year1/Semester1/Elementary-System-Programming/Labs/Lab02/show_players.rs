use std::io;

fn show_players(player1: String, player2: String) {

    let p1_len = player1.len();
    let p2_len = player2.len();


    //Show Players Vertical Variables
    let long_player_len;
    if p1_len > p2_len{
        long_player_len = p1_len;
    } else {
        long_player_len = p2_len;
    }
    let vert_len = 14 + long_player_len;

    //Show Players Horizontal Variables
    let longest_len = 27 + p1_len + p2_len;


    println!("Show Player Vertical: ");
    println!("");

    //Top Border
    for _i in 1..vert_len {
        print!("*");
    }
    println!("");
    
    //Player1 Top Blank
    print!("*");
    for _i in 1..vert_len  - 2  {
        print!(" ");
    }
    print!("*");
    println!("");
    
    //Player1 Name
    print!("* Player1: ");
    print!("{}", player1);
    for _i in 1..long_player_len - p1_len {
        print!(" ");
    }
    print!(" *");
    println!("");
    
    //Player1 Bottom Blank
    print!("*");
    for _i in 1..vert_len - 2 {
        print!(" ");
    }
    print!("*");
    println!("");
    
    //Middle Border
    for _i in 1..vert_len {
        print!("*");
    }
    println!("");
    
    //Player2 Top Blank
    print!("*");
    for _i in 1..vert_len - 2 {
        print!(" ");
    }
    print!("*");
    println!("");   
    
    //Player2 Name
    print!("* Player2: ");
    print!("{}", player2);
    for _i in 1..long_player_len - p2_len + 1 {
        print!(" ");
    }
    print!(" *");
    println!("");
    
    //Player2 Bottom Blank
    print!("*");
    for _i in 1..vert_len - 2 {
        print!(" ");
    }
    print!("*");
    println!("");
    
    //Bottom Border
    for _i in 1..vert_len {
        print!("*");
    }
    println!("");
    
    println!("");

    println!("Show Player Horizontal: ");
    println!("");
    
    //Top Border
    for _i in 1..longest_len - 1 {
        print!("*");
    }
    println!("");
    
    //Top Blank
    print!("*");
    for _i in 1..12 + p1_len {
        print!(" ");
    }
    print!("*");
    for _i in 1..12 + p2_len {
        print!(" ");
    }
    print!("*");
    println!("");
    
    //Player2 Names
    print!("* Player1: {} * Player2: {} *", player1, player2);
    println!("");
    
    //Bottom Blank
    print!("*");
    for _i in 1..12 + p1_len {
        print!(" ");
    }
    print!("*");
    for _i in 1..12 + p2_len {
        print!(" ");
    }
    print!("*");
    println!("");
    
    //Bottom Border
    for _i in 1..longest_len - 1 {
        print!("*");
    }
    println!("");
    
    
}




fn main() {
    let mut input = String::new();
    println!("Please input player1 name: ");
    io::stdin().read_line(&mut input).expect("Failed to read.");
    let player1 = input.trim().to_string();
    input.clear();
    println!("Please input player2 name: ");
    io::stdin().read_line(&mut input).expect("Failed to read.");
    let player2 = input.trim().to_string();
    input.clear();

    println!("");
    
    show_players(player1, player2);
}