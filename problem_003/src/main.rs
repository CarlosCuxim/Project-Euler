// [[ Problem #3 ]]
// The prime factors of 13195 are 5, 7, 13 and 29.
//
// What is the largest prime factor of the number 600851475143?

fn main() {
    let n: u64 = 600851475143;
    let p = largest_prime_factor(n);
    println!("The largest prime factor of {n} is {p}");
}

fn largest_prime_factor(mut n: u64) -> u64 {
    let mut p: u64 = 2;
    while n > 1 {
        if n % p == 0 {
            n /= p;
        } else {
            p += 1;
        }
    }
    p
}
