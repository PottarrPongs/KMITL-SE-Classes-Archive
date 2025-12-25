use rand::Rng;
use std::io::{self, Write};

#[derive(Debug)]
struct Player {
    hp: i32,
    stamina: i32,
    power: i32,
    gold: i32,
}

#[derive(Debug)]
struct Enemy {
    name: &'static str,
    hp: i32,
    power: i32,
    reward: i32,
}

impl Enemy {
    fn new(name: &'static str, hp: i32, power: i32, reward: i32) -> Self {
        Enemy { name, hp, power, reward }
    }
}

#[derive(Debug)]
enum Encounter {
    Nothing, // 25%
    Meat,    // 20%
    Water,   // 20%
    Herb,    // 15%
    Enemy,   // 20%
}

fn get_random_encounter() -> Encounter {
    let roll = rand::thread_rng().gen_range(0..100);
    match roll {
        0..=24 => Encounter::Nothing,
        25..=44 => Encounter::Meat,
        45..=64 => Encounter::Water,
        65..=79 => Encounter::Herb,
        _ => Encounter::Enemy,
    }
}

fn get_random_enemy() -> Enemy {
    let roll = rand::thread_rng().gen_range(0..100);
    match roll {
        0..=59 => Enemy::new("Rat", 10, 2, 10),     // 60%
        60..=89 => Enemy::new("Wolf", 20, 5, 20),   // 30%
        _ => Enemy::new("Boar", 30, 10, 30),        // 10%
    }
}

fn get_direction() -> Option<String> {
    let mut input = String::new();
    print!("Enter direction (N/S/E/W) or Q to quit: ");
    io::stdout().flush().unwrap();
    io::stdin().read_line(&mut input).ok()?;
    let trimmed = input.trim().to_uppercase();
    match trimmed.as_str() {
        "N" | "S" | "E" | "W" | "Q" => Some(trimmed),
        _ => None,
    }
}

fn main() {
    let mut player = Player {
        hp: 100,
        stamina: 50,
        power: 10,
        gold: 0,
    };

    println!("Welcome to the Adventure Game!");

    while player.hp > 0 && player.stamina > 0 && player.gold < 100 {
        println!("\nPlayer status: HP: {}, Stamina: {}, Power: {}, Gold: {}",
                 player.hp, player.stamina, player.power, player.gold);

        let dir = get_direction();
        match dir.as_deref() {
            Some("Q") => {
                println!("You quit the game. Goodbye!");
                return;
            }
            Some(_) => {},
            None => {
                println!("Invalid input. Use N/S/E/W or Q.");
                continue;
            }
        }

        player.stamina -= 1;
        println!("You walk...");

        match get_random_encounter() {
            Encounter::Nothing => println!("Nothing happens."),
            Encounter::Meat => {
                player.hp += 5;
                if player.hp > 100 {
                    player.hp = 100;
                }
                println!("You found meat! +5 HP.");
            },
            Encounter::Water => {
                player.stamina += 3;
                println!("You found water! +3 stamina.");
            },
            Encounter::Herb => {
                player.power += 1;
                println!("You found an herb! +1 power.");
            },
            Encounter::Enemy => {
                let mut enemy = get_random_enemy();
                println!("An enemy appears! It's a {}!", enemy.name);

                while enemy.hp > 0 && player.hp > 0 {
                    // Player attacks
                    enemy.hp -= player.power;
                    println!("You hit the {} for {} damage!", enemy.name, player.power);

                    if enemy.hp <= 0 {
                        println!("You defeated the {} and gained {} gold!", enemy.name, enemy.reward);
                        player.gold += enemy.reward;
                        break;
                    }

                    // Enemy attacks
                    player.hp -= enemy.power;
                    println!("The {} hits back for {} damage!", enemy.name, enemy.power);

                    if player.hp <= 0 {
                        println!("You were defeated by the {}!", enemy.name);
                        break;
                    }
                }

            },
        }
    }

    if player.gold >= 100 {
        println!("\n🎉 Congratulations! You collected enough gold and won the game!");
    } else if player.hp <= 0 {
        println!("\n💀 Game over! You died.");
    } else {
        println!("\n💤 Game over! You ran out of stamina.");
    }
}
