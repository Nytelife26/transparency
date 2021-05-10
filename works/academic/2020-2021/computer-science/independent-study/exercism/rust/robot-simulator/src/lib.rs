#[derive(PartialEq, Debug)]
pub enum Direction {
	North,
	East,
	South,
	West,
}

pub struct Robot {
	location: [i32; 2],
	direction: Direction,
}

impl Robot {
	pub fn new(x: i32, y: i32, d: Direction) -> Self {
		Robot {
			location: [x, y],
			direction: d,
		}
	}

	pub fn turn_right(mut self) -> Self {
		self.direction = match self.direction {
			Direction::North => Direction::East,
			Direction::East => Direction::South,
			Direction::South => Direction::West,
			Direction::West => Direction::North,
		};
		self
	}

	pub fn turn_left(mut self) -> Self {
		self.direction = match self.direction {
			Direction::North => Direction::West,
			Direction::West => Direction::South,
			Direction::South => Direction::East,
			Direction::East => Direction::North,
		};
		self
	}

	pub fn advance(mut self) -> Self {
		let loc = self.position();
		self.location = match self.direction {
			Direction::North => [loc.0, loc.1 + 1],
			Direction::East => [loc.0 + 1, loc.1],
			Direction::South => [loc.0, loc.1 - 1],
			Direction::West => [loc.0 - 1, loc.1],
		};
		self
	}

	pub fn instructions(mut self, instructions: &str) -> Self {
		for op in instructions.to_uppercase().chars() {
			self = match op {
				'R' => self.turn_right(),
				'L' => self.turn_left(),
				'A' => self.advance(),
				_ => self,
			};
		}
		self
	}

	pub fn position(&self) -> (i32, i32) {
		(self.location[0], self.location[1])
	}

	pub fn direction(&self) -> &Direction {
		&self.direction
	}
}
