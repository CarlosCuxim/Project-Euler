// By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
// the the 6th prime is 13.
//
// What is the 10001st prime number?

use std::io;

fn main() {
    println!("Type a integer");
    let mut n = String::new();
    io::stdin().read_line(&mut n).expect("Failed reading line");
    let n: u64 = n.trim().parse().expect("The input was not a number");

    let nth_prime = nth_prime(n);

    println!("The {n}-th prime is {nth_prime}");
}

fn is_prime(n: u64) -> bool {
    let limit: u64 = (n as f64).sqrt() as u64 + 1;
    for p in 2..limit {
        if n % p == 0 {
            return false;
        }
    }
    true
}

fn nth_prime(n: u64) -> u64 {
    let mut i: u64 = 1;
    let mut p: u64 = 2;
    while i < n {
        p += 1;
        if is_prime(p) {
            i += 1;
        }
    }
    p
}
