use std::fmt::{self, Display, Formatter};

#[derive(Clone, PartialEq, Debug)]
pub enum LogLevel {
	Info,
	Warning,
	Error,
	Debug,
}

impl Display for LogLevel {
	fn fmt(&self, f: &mut Formatter<'_>) -> fmt::Result {
		match self {
			LogLevel::Info => f.pad("INFO"),
			LogLevel::Warning => f.pad("WARNING"),
			LogLevel::Error => f.pad("ERROR"),
			LogLevel::Debug => f.pad("DEBUG"),
		}
	}
}

pub fn log(level: LogLevel, message: &str) -> String {
	format!("[{}]: {}", level, message)
}

macro_rules! impl_logfn {
	($fn_ident:ident, $variant:expr) => {
		pub fn $fn_ident(message: &str) -> String {
			crate::log($variant, message)
		}
	}
}

impl_logfn!(info, LogLevel::Info);
impl_logfn!(warn, LogLevel::Warning);
impl_logfn!(error, LogLevel::Error);
impl_logfn!(debug, LogLevel::Debug);
