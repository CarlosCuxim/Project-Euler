// [[ Project Euler #1 ]]
// If we list all the natural numbers below 10 that are multiples of 3 or 5,
// we get 3, 5, 6 and 9. The sum of these multiples is 23.
//
// Find the sum of all the multiples of 3 or 5 below 1000.

use std::io;

fn main() {
    let limit: u64 = loop {
        // User input number string
        println!("Select the limit: ");
        let mut limit = String::new();

        io::stdin()
            .read_line(&mut limit)
            .expect("Failed to read line");
        match limit.trim().parse() {
            Ok(num) => break num,
            Err(_) => {
                println!("The input was not a number, please try again...");
                continue;
            }
        };
    };

    let sum3: u64 = sum_multiples_below(3, limit);
    let sum5: u64 = sum_multiples_below(5, limit);
    let sum15: u64 = sum_multiples_below(15, limit);
    let answer: u64 = sum3 + sum5 - sum15;

    println!("The sum of numbers below {limit} that are multiples of 5 and 3 is {answer}")
}

fn sum_multiples_below(n: u64, limit: u64) -> u64 {
    let mut sum: u64 = 0;
    for a in 1..limit {
        if a % n == 0 {
            sum += a;
        }
    }
    sum
}
