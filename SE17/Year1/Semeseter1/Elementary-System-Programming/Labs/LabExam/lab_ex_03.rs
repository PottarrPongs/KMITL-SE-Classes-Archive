// Define PowerSource trait
trait PowerSource {
    fn fuel(&self) -> String;
    fn max_range(&self) -> i32;
}

// Define Terrain trait
trait Terrain {
    fn surface(&self) -> String;
}

// Define CargoCapacity trait with default implementation
trait CargoCapacity {
    fn max_load(&self) -> i32;
    
    fn can_carry(&self, weight: i32) -> bool {
        weight <= self.max_load()
    }
}

// Define structs
struct ElectricCar {
    battery_kwh: i32,
}

struct MountainBike;

struct CargoDrone {
    payload_kg: i32,
}

// Implement PowerSource for ElectricCar
impl PowerSource for ElectricCar {
    fn fuel(&self) -> String {
        String::from("rechargeable battery")
    }
    
    fn max_range(&self) -> i32 {
        self.battery_kwh * 5
    }
}

// Implement Terrain for ElectricCar
impl Terrain for ElectricCar {
    fn surface(&self) -> String {
        String::from("paved roads and highways")
    }
}

// Implement CargoCapacity for ElectricCar
impl CargoCapacity for ElectricCar {
    fn max_load(&self) -> i32 {
        400
    }
}

// Implement PowerSource for MountainBike
impl PowerSource for MountainBike {
    fn fuel(&self) -> String {
        String::from("human pedaling")
    }
    
    fn max_range(&self) -> i32 {
        50
    }
}

// Implement Terrain for MountainBike
impl Terrain for MountainBike {
    fn surface(&self) -> String {
        String::from("rough trails and off-road paths")
    }
}

// Implement PowerSource for CargoDrone
impl PowerSource for CargoDrone {
    fn fuel(&self) -> String {
        String::from("lithium battery")
    }
    
    fn max_range(&self) -> i32 {
        30
    }
}

// Implement Terrain for CargoDrone
impl Terrain for CargoDrone {
    fn surface(&self) -> String {
        String::from("air routes and urban areas")
    }
}

// Implement CargoCapacity for CargoDrone
impl CargoCapacity for CargoDrone {
    fn max_load(&self) -> i32 {
        self.payload_kg
    }
}

// Generic function to describe vehicle
fn describe_vehicle<T: PowerSource + Terrain>(vehicle: &T) {
    println!("Power source: {}", vehicle.fuel());
    println!("Max range: {} km", vehicle.max_range());
    println!("Best terrain: {}", vehicle.surface());
}

// Generic function to check cargo capacity
fn check_cargo<T: CargoCapacity>(vehicle: &T, weight: i32) {
    let can_carry = vehicle.can_carry(weight);
    println!("{} kg: {}", weight, if can_carry { "Yes" } else { "No" });
}

fn main() {
    // Create instances
    let electric_car = ElectricCar { battery_kwh: 75 };
    let mountain_bike = MountainBike;
    let cargo_drone = CargoDrone { payload_kg: 25 };
    
    // Describe all vehicles
    println!("Electric Car:");
    describe_vehicle(&electric_car);
    println!();
    
    println!("Mountain Bike:");
    describe_vehicle(&mountain_bike);
    println!();
    
    println!("Cargo Drone:");
    describe_vehicle(&cargo_drone);
    println!();
    
    // Check cargo capacity
    println!("Cargo Check:");
    print!("Electric Car can carry ");
    check_cargo(&electric_car, 350);
    
    print!("Cargo Drone can carry ");
    check_cargo(&cargo_drone, 30);
}