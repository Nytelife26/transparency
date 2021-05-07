use std::fmt::{Debug, Display, Formatter, Result};

#[derive(PartialEq, Eq, PartialOrd, Ord)]
pub struct Clock {
	hours: i32,
	minutes: i32,
}

impl Clock {
	pub fn new(hours: i32, minutes: i32) -> Self {
		let mut mins = minutes + hours * 60;
		if mins < 0 {
			mins = (-1440 * mins) + mins
		}
		Clock {
			hours: (mins / 60) % 24,
			minutes: mins % 60,
		}
	}

	pub fn add_minutes(&self, minutes: i32) -> Self {
		Clock::new(self.hours, self.minutes + minutes)
	}
}

impl Display for Clock {
	fn fmt(&self, f: &mut Formatter<'_>) -> Result {
		write!(f, "{:02}:{:02}", self.hours, self.minutes)
	}
}

impl Debug for Clock {
	fn fmt(&self, f: &mut Formatter<'_>) -> Result {
		write!(f, "{:02}:{:02}", self.hours, self.minutes)
	}
}

impl From<Clock> for String {
	fn from(clock: Clock) -> Self {
		format!("{:02}:{:02}", clock.hours, clock.minutes)
	}
}
