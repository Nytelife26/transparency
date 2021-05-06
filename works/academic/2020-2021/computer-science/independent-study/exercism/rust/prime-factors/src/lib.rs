pub fn factors(n: u64) -> Vec<u64> {
	let mut divisor: u64 = 2;
	let mut factors: Vec<u64> = Vec::new();
	let mut counter: u64 = n.clone();
	while counter > 1 {
		if counter % divisor == 0 {
			factors.push(divisor);
			counter /= divisor;
			continue;
		}
		divisor += 1;
	}
	factors
}
