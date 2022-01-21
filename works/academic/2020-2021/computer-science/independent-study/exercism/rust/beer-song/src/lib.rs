pub fn verse(n: u32) -> String {
	let bottom = if n > 0 {
		format!(
			"Take {x} down and pass it around",
			x = if n > 1 { "one" } else { "it" }
		)
	} else {
		"Go to the store and buy some more".to_owned()
	};
	let remaining = if n > 1 {
		(n - 1).to_string()
	} else if n == 1 {
		"no more".to_owned()
	} else {
		"99".to_owned()
	};
	let lower;
	let upper;
	if n == 0 {
		lower = "no more".to_owned();
		upper = "No more".to_owned();
	} else {
		lower = n.to_string();
		upper = n.to_string();
	}
	format!(
		"{a} bottle{b} of beer on the wall, {c} bottle{b} of beer.\n{d}, {e} bottle{f} of beer on the wall.\n",
		a=upper,
		b=pluralize(n),
		c=lower,
		d=bottom,
		e=remaining,
		f=pluralize(if n >= 1 { n - 1 } else { 99 })
	)
}

pub fn pluralize(n: u32) -> &'static str {
	if n != 1 {
		"s"
	} else {
		""
	}
}

pub fn sing(start: u32, end: u32) -> String {
	let mut result = String::new();
	for n in (end..=start).rev() {
		result.push_str(&format!(
			"{a}{b}",
			a = verse(n),
			b = if n != end { "\n" } else { "" }
		));
	}
	result
}
