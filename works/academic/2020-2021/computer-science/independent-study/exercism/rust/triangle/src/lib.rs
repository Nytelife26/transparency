pub struct Triangle {
	a: u64,
	b: u64,
	c: u64,
}

impl Triangle {
	pub fn build(sides: [u64; 3]) -> Option<Triangle> {
		if sides.iter().any(|x| *x == 0)
			|| !sides.windows(2).all(|x| {
				let n: u64 = x.iter().sum();
				sides.iter().all(|i| n >= *i)
			}) {
			return None;
		}
		Some(Triangle {
			a: sides[0usize],
			b: sides[1usize],
			c: sides[2usize],
		})
	}

	pub fn is_equilateral(&self) -> bool {
		self.a == self.b && self.b == self.c
	}

	pub fn is_scalene(&self) -> bool {
		self.a != self.b && self.b != self.c && self.a != self.c
	}

	pub fn is_isosceles(&self) -> bool {
		self.a == self.b || self.b == self.c || self.a == self.c
	}
}
