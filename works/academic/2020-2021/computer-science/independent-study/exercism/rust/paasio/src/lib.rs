use std::io::{Read, Result, Write};

pub struct ReadStats<R> {
	io: R,
	bytes: usize,
	calls: usize,
}

impl<R: Read> ReadStats<R> {
	pub fn new(wrapped: R) -> ReadStats<R> {
		ReadStats {
			io: wrapped,
			bytes: 0usize,
			calls: 0usize,
		}
	}

	pub fn get_ref(&self) -> &R {
		&self.io
	}

	pub fn bytes_through(&self) -> usize {
		self.bytes
	}

	pub fn reads(&self) -> usize {
		self.calls
	}
}

impl<R: Read> Read for ReadStats<R> {
	fn read(&mut self, buf: &mut [u8]) -> Result<usize> {
		let result = self.io.read(buf)?;
		self.calls += 1;
		self.bytes += result;
		Ok(result)
	}
}

pub struct WriteStats<W> {
	io: W,
	bytes: usize,
	calls: usize,
}

impl<W: Write> WriteStats<W> {
	pub fn new(wrapped: W) -> WriteStats<W> {
		WriteStats {
			io: wrapped,
			bytes: 0usize,
			calls: 0usize,
		}
	}

	pub fn get_ref(&self) -> &W {
		&self.io
	}

	pub fn bytes_through(&self) -> usize {
		self.bytes
	}

	pub fn writes(&self) -> usize {
		self.calls
	}
}

impl<W: Write> Write for WriteStats<W> {
	fn write(&mut self, buf: &[u8]) -> Result<usize> {
		let mut idx = 0;
		while idx < buf.len() {
			let written = self.io.write(&buf[idx..])?;
			self.calls += 1usize;
			idx += written;
		}
		self.bytes += idx;
		Ok(idx)
	}

	fn flush(&mut self) -> Result<()> {
		self.io.flush()
	}
}
