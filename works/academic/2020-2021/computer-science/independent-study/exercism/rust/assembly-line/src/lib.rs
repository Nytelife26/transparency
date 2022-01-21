pub enum Speed {
	Off,
	Min,
	Med,
	Max,
}

impl From<u8> for Speed {
	fn from(n: u8) -> Self {
		match n {
			0 => Speed::Off,
			1..=4 => Speed::Min,
			5..=9 => Speed::Med,
			_ => Speed::Max
		}
	}
}

impl From<Speed> for f64 {
	fn from(speed: Speed) -> Self {
		match speed {
			Speed::Min => 1.0,
			Speed::Med => 0.9,
			Speed::Max => 0.77,
			_ => 0.0,
		}
	}
}

pub fn production_rate_per_hour(speed: u8) -> f64 {
	speed as f64 * 221.0 * f64::from(Speed::from(speed))
}

pub fn working_items_per_minute(speed: u8) -> u32 {
	production_rate_per_hour(speed) as u32 / 60
}
