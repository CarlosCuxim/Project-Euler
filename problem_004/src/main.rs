// [[ Problem 4 ]]
// A palindromic number reads the same both ways. The largest palindrome made
// from the product of two 2-digit numbers is 9009 = 91 * 99.
//
// Find the largest palindrome made from the product of two 3-digit numbers.

use std::io;

fn main() {
    let digits: u32 = loop {
        println!("Select the numner of digits");
        let mut input = String::new();

        io::stdin()
            .read_line(&mut input)
            .expect("Failed to read line");

        match input.trim().parse() {
            Ok(num) => break num,
            Err(_) => {
                println!("The input was not a number, try again");
                continue;
            }
        }
    };

    let ans = largest_palindrome(digits);

    println!("The largest palindrome with {digits}-digits is {ans}");
}

fn reverse_number(mut n: u64) -> u64 {
    let mut ans: u64 = 0;
    while n > 0 {
        let r = n % 10;

        ans = 10 * ans + r;
        n /= 10;
    }
    ans
}

fn largest_palindrome(d: u32) -> u64 {
    let mut largest = 0;
    let a = u64::pow(10, d - 1);
    let b = u64::pow(10, d);
    for i in a..b {
        for j in a..b {
            let prod = i * j;
            if (prod == reverse_number(prod)) && prod > largest {
                largest = prod;
            }
        }
    }
    largest
}
