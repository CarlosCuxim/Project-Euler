// 2520 is the smallest number that can be divided by each of the numbers from 1
// to 10 without any remainder.
//
// What is the smallest positive number that is evenly divisible by all of the
// numbers from 1 to 20

use std::io;

fn main() {
    println!("Select a limit");
    let mut limit = String::new();

    io::stdin()
        .read_line(&mut limit)
        .expect("Failed reading line");

    let limit: u64 = limit.trim().parse().expect("Failed to convert to a number");

    let r_lcm = lcm_for_range(1, limit);

    println!("The mcm for 1 to {limit} is {r_lcm}")
}

fn gcd(mut a: u64, mut b: u64) -> u64 {
    let mut r;
    while b > 0 {
        r = a % b;
        a = b;
        b = r;
    }
    a
}

fn lcm(a: u64, b: u64) -> u64 {
    a * b / gcd(a, b)
}

fn lcm_for_range(a: u64, b: u64) -> u64 {
    let mut r_lcm: u64 = 1;
    for i in a..b + 1 {
        r_lcm = lcm(r_lcm, i);
    }
    r_lcm
}
