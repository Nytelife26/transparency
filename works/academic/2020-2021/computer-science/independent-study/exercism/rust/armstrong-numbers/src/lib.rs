pub fn is_armstrong_number(num: u32) -> bool {
	let digits = num.to_string().chars().collect::<Vec<char>>();
	let length = digits.len() as u32;

	num == digits.iter().fold(0, |a, b| {
		a + str::parse::<u32>(&b.to_string()).unwrap().pow(length)
	})
}
