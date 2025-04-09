// [[ Problem #8 ]]
// The four adjacent digits in the 1000-digit number that have the greatest
// product are 9 * 9 * 8 * 9 = 5832.
//
// ...
//
// Find the thirteen adjacent digits in the 100-digit number that have the
// greatest product. What is the value of this product?

use std::fs;
use std::io;

fn main() {
    println!("Type a number:");
    let mut input = String::new();
    io::stdin()
        .read_line(&mut input)
        .expect("Failed to read the line");
    let n: usize = input.trim().parse().expect("The input was not a number");

    let vector = file_to_vector("files/number.txt");
    let prod = max_prod_adyacent(&vector, n);

    println!("The max prod of {n}-digits is {prod}");
}

fn file_to_vector(file_path: &str) -> Vec<u32> {
    let string_number = fs::read_to_string(file_path).expect("The file couldn't be readed");

    let mut vector: Vec<u32> = Vec::new();
    for c in string_number.chars() {
        if c != '\n' {
            let digit = c.to_digit(10).expect("The character was not a digit");
            vector.push(digit);
        }
    }
    vector
}

fn max_prod_adyacent(vector: &[u32], n: usize) -> u64 {
    let mut max_prod: u64 = 1;
    for i in 0..vector.len() - n + 1 {
        let mut curr_prod: u64 = 1;
        for j in 0..n {
            curr_prod *= u64::from(vector[i + j]);
        }
        if curr_prod > max_prod {
            max_prod = curr_prod;
        }
    }
    max_prod
}
