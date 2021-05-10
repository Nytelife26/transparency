#[derive(Debug)]
pub struct ChessPosition {
	x: i32,
	y: i32,
}

#[derive(Debug)]
pub struct Queen {
	pos: ChessPosition,
}

impl ChessPosition {
	pub fn new(rank: i32, file: i32) -> Option<Self> {
		if rank < 0 || file < 0 || rank >= 8 || file >= 8 {
			return None;
		}
		Some(ChessPosition { x: rank, y: file })
	}
}

impl Queen {
	pub fn new(position: ChessPosition) -> Self {
		Queen { pos: position }
	}

	pub fn can_attack(&self, other: &Queen) -> bool {
		self.pos.x == other.pos.x // same rank
			|| self.pos.y == other.pos.y // same file
			|| (self.pos.x - other.pos.x).abs() // diagonal
				== (self.pos.y - other.pos.y).abs()
	}
}
