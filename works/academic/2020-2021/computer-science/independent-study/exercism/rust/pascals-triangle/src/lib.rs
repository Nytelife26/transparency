use std::cmp::min;

pub struct PascalsTriangle {
	rows: u32,
}

pub fn factorial(n: u32) -> u32 {
	let mut result = 1;
	for i in 1..=n {
		result *= i;
	}
	result
}

pub fn choose(n: u32, k: u32) -> u32 {
	factorial(n) / (factorial(k) * factorial(n - k))
}

impl PascalsTriangle {
	pub fn new(row_count: u32) -> Self {
		PascalsTriangle { rows: row_count }
	}

	pub fn rows(&self) -> Vec<Vec<u32>> {
		let mut result: Vec<Vec<u32>> = Vec::new();
		if self.rows == 0 {
			return result;
		}

		result.extend((0..min(self.rows, 5)).map(|n| self.row_11pow(n)));
		result.extend((5..self.rows).map(|n| self.row_nchoosek(n)));
		result
	}

	fn row_11pow(&self, n: u32) -> Vec<u32> {
		// for every row, k, where k < 5, the row is 11^k's split digits
		let rowsig = 11u32.pow(n);
		(0..=n)
			.map(|k| rowsig / 10u32.pow(k) % 10)
			.collect::<Vec<u32>>()
	}

	fn row_nchoosek(&self, n: u32) -> Vec<u32> {
		// for every row, k, where k >= 5, we use n choose k
		(0..=n).map(|k| choose(n, k)).collect::<Vec<u32>>()
	}
}
