// [[ Problem #9 ]]
// A Pythagorean triplet is a set of three natural numbers, a < b < c$, for
// which, a² + b² = c².
// For example, 3² + 4² = 9 + 16 = 25 = 5².
// There exists exactly one Pythagorean triplet for which a + b + c = 1000.
// Find the product abc.

fn main() {
    let s: u64 = 1000;
    let s_float = s as f64;

    let bound_a = ((3f64 / 2.).sqrt() - 1.) * s_float;
    let bound_a = bound_a as u64 + 1;
    let bound_b = (s_float * (s_float - 2.)) / (2. * (s_float + 1.));
    let bound_b = bound_b as u64 + 1;

    for a in 1..bound_a {
        for b in a + 1..bound_b {
            let c = s - a - b;
            if is_pyth(a, b, c) {
                let prod = a * b * c;
                println!("{a}*{b}*{c} = {prod}");
            }
        }
    }
}

fn is_pyth(a: u64, b: u64, c: u64) -> bool {
    a * a + b * b == c * c
}
