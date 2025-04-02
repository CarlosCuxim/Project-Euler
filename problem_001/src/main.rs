// [[ Project Euler #1 ]]
// If we list all the natural numbers below 10 that are multiples of 3 or 5,
// we get 3, 5, 6 and 9. The sum of these multiples is 23.
//
// Find the sum of all the multiples of 3 or 5 below 1000.

fn main() {
    let limit: i64 = 1000;
    let sum3: i64 = sum_multiples_below(3, limit);
    let sum5: i64 = sum_multiples_below(5, limit);
    let sum15: i64 = sum_multiples_below(15, limit);
    let answer: i64 = sum3 + sum5 - sum15;

    println!("The sum of numbers below {limit} that are multiples of 5 and 3 is {answer}")
}

fn sum_multiples_below(n: i64, limit: i64) -> i64 {
    let mut sum: i64 = 0;
    for a in 1..limit {
        if a % n == 0 {
            sum += a;
        }
    }
    sum
}
