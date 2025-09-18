// Lab 2: Weather Data Analysis

// Define a type alias for clarity.
type WeatherData = (f64, u32, bool);

// 1. Find the consecutive 3 days with the highest average temperature. 
fn warmest_period(data: &[WeatherData]) -> &[WeatherData] {
    data.windows(3)
        .max_by(|a, b| {
            let avg_a = (a[0].0 + a[1].0 + a[2].0) / 3.0;
            let avg_b = (b[0].0 + b[1].0 + b[2].0) / 3.0;
            avg_a.partial_cmp(&avg_b).unwrap()
        })
        .unwrap_or(&[])
}

// 2. Find the 0-based index of the day with the lowest temperature. 
fn coldest_day(data: &[WeatherData]) -> usize {
    data.iter()
        .enumerate()
        .min_by(|(_, a), (_, b)| a.0.partial_cmp(&b.0).unwrap())
        .map(|(index, _)| index)
        .unwrap_or(0)
}

// 3. Predict rain based on a formula. 
fn predict_rain(day_data: &WeatherData) -> bool {
    0.005 * (day_data.1 as f64) + 0.02 * day_data.0 - 1.0 > 0.5
}

// 4. Count the total number of days where it rained. 
fn count_rainy_days(data: &[WeatherData]) -> usize {
    data.iter().filter(|&&day| day.2).count()
}

fn main() {
    // Provided weather data. [cite: 35]
    let weather_data: Vec<WeatherData> = vec![
        (25.0, 65, false), (26.2, 70, false), (24.8, 62, false), (23.5, 78, true), (22.1, 82, true),
        (20.7, 85, true), (21.3, 80, true), (22.8, 73, false), (24.0, 68, false), (25.5, 60, false),
        (27.1, 55, false), (28.3, 52, false), (27.9, 58, false), (26.6, 64, false), (25.2, 70, true),
        (23.8, 75, true), (22.4, 80, true), (21.0, 83, true), (20.5, 86, true), (21.8, 82, true),
        (23.2, 77, false), (24.5, 70, false), (25.8, 63, false), (26.4, 58, false), (27.0, 53, false),
        (26.7, 56, false), (25.3, 62, false), (24.9, 68, true), (23.1, 74, true), (21.7, 79, true)
    ];

    println!("\n--- Lab 2 Output ---");

    // Expected Output formatting. [cite: 36, 37, 38, 39]
    println!("Warmest 3-day period: {:?}", warmest_period(&weather_data));
    println!("Coldest day: {}", coldest_day(&weather_data));
    println!("Number of rainy days: {}", count_rainy_days(&weather_data));
    println!("Will it rain on the first day? {}", predict_rain(&weather_data[0]));
}