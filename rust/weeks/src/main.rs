fn main() {
    // adding necessary librarys
    use std::io::{stdin};
    // input var
    let mut days = String::new();
    // parsing input to char
    stdin().read_line(&mut days).expect("Failed to parse days");
    // parsing input to a int
    let days: i32 = days.trim().parse().expect("Not an integer");
    // calculating weeks
    let weeks = days / 7;
    // printing the output
    println!("{}",weeks);
}
 
