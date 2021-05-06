pub fn is_armstrong_number(num: u32) -> bool {
	let length = ((num as f32).log10() + 1f32).floor() as u32;
	num == (0..length).fold(0, |a, b| a + (num / 10u32.pow(b) % 10).pow(length))
}
