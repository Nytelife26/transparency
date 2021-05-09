const DELIMS: [char; 2] = ['-', '_'];

fn uppercase(c: &char) -> bool {
	c.is_uppercase()
}

fn delims(c: char) -> bool {
	c.is_whitespace() || DELIMS.contains(&c)
}

fn divide_upper_sequences(s: &str) -> String {
	s.chars()
		.take(1)
		.chain(s.chars().skip_while(uppercase).filter(uppercase))
		.collect::<String>()
}

pub fn abbreviate(phrase: &str) -> String {
	phrase
		.split(delims)
		.map(divide_upper_sequences)
		.collect::<String>()
		.to_uppercase()
}
