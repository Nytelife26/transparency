pub fn brackets_are_balanced(string: &str) -> bool {
	let mut nest: Vec<char> = Vec::new();
	for x in string.chars() {
		match x {
			'[' | '{' | '(' => nest.push(x),
			']' => if nest.pop() != Some('[') { return false; },
			'}' => if nest.pop() != Some('{') { return false; },
			')' => if nest.pop() != Some('(') { return false; },
			_ => (),
		};
	}
	nest.is_empty()
}
