// [[ Problem #6 ]]
// The sum of the squares of the first ten natural numbers is,
// 1² + 2² + ... + 10² = 385.
// The square of the first ten natural numbers is,
// (1 + 2 + ... + 10)² = 55² = 3025.
// Hence the difference between the sum of the squares of the first ten natural
// numbers and the square of the sum is 3025 - 385 = 2640.
//
// Find the difference between hte sum of the squares of the first one hundred
// natural numbers and the square of the sum.

use std::io;

fn main() {
    println!("Type the limit");
    let mut limit = String::new();
    io::stdin()
        .read_line(&mut limit)
        .expect("Failed to read line");
    let limit: u64 = limit.trim().parse().expect("The input was not a number");

    let sq_sum = square(sum_range(1, limit));
    let sum_sq = sum_squares_range(1, limit);
    let diff = sq_sum - sum_sq;

    println!(
        "The difference between the squqres of 1 to {limit} and the square of the sum is {diff}"
    )
}

fn square(n: u64) -> u64 {
    n * n
}

fn sum_range(a: u64, b: u64) -> u64 {
    let mut sum: u64 = 0;
    for i in a..b + 1 {
        sum += i;
    }
    sum
}

fn sum_squares_range(a: u64, b: u64) -> u64 {
    let mut sum: u64 = 0;
    for i in a..b + 1 {
        sum += square(i);
    }
    sum
}
