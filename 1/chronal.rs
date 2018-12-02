use std::io;
use std::io::prelude::*;

fn main () {
    let stdin = io::stdin();

    let total: i32 = stdin.lock().lines().into_iter()
        .map(|r| r.unwrap())
        .map(|s| s.parse::<i32>().unwrap())
        .sum();
    println!("{}", total);
}
