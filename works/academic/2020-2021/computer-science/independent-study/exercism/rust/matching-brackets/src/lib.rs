const BRACKETS: &'static [char] = &['[', '{', '(', ')', '}', ']'];

pub fn brackets(x: &char) -> bool {
	BRACKETS.contains(x)
}

pub fn brackets_are_balanced(string: &str) -> bool {
	let mut nest: Vec<char> = Vec::new();
	string.chars().filter(brackets).for_each(|x| {
		let item = match nest.last() {
			Some(val) => val,
			None => &' ',
		};
		match x {
			')' if item == &'(' => {
				nest.pop();
			}
			']' if item == &'[' => {
				nest.pop();
			}
			'}' if item == &'{' => {
				nest.pop();
			}
			_ => {
				nest.push(x);
			}
		};
	});
	nest.len() == 0
}
