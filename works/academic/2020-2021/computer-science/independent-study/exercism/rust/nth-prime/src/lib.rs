pub fn nth(n: u32) -> u32 {
	if n == 0 { return 2; }
	if n == 1 { return 3; }
	let n = (n + 1) as f32;
	let nlog = n.ln();
	let lower = (n * (nlog + nlog.ln()) - n) as u32;
	let n = n as u32;
	let count: u32 = (7..=lower).filter(is_prime).count() as u32 + 3;
	let mut remaining = n - count;
	let mut field = Vec::new();
	for i in (lower as u32).. {
		if remaining == 0 { break; }
		if is_prime(&i) {
			field.push(i);
			remaining -= 1;
		}
	}
	return *field.last().unwrap();
}

fn is_prime(n: &u32) -> bool {
	if ((n - 1) % 6 == 0) || ((n + 1) % 6 == 0) {
		!(2..(*n as f32).sqrt() as u32 + 1)
			.any(|test| n % test == 0)
	} else {
		false
	}
}
