pub fn primes_up_to(n: u32) -> Vec<u32> {
	if n <= 1 {
		return vec![];
	}

	let mut field: Vec<bool> = vec![true; (n - 1) as usize];
	for i in 2..=(n as f32).sqrt() as u32 {
		if field[(i - 2) as usize] {
			let mut pointer = i.pow(2);
			while pointer <= n {
				field[(pointer - 2) as usize] = false;
				pointer += i;
			}
		}
	}
	(2..=n)
		.filter(|x| field[(*x - 2) as usize])
		.collect::<Vec<u32>>()
}
