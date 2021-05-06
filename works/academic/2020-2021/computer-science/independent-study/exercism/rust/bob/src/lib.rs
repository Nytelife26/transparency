fn alpha(x: &char) -> bool {
	x.is_alphabetic()
}

pub fn reply(message: &str) -> &str {
	let msg = message.trim();

	// if length is zero, we can skip the rest for speed
	if msg.len() == 0 {
		return "Fine. Be that way!";
	}

	let question = msg.ends_with("?");
	let yelling =
		msg.to_uppercase() == msg && msg.chars().filter(alpha).count() > 0;

	match msg {
		_ if question && yelling => "Calm down, I know what I'm doing!",
		_ if yelling => "Whoa, chill out!",
		_ if question => "Sure.",
		_ => "Whatever.",
	}
}
