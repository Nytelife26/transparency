pub fn raindrops(n: u32) -> String {
	let mut result = String::new();
	let mut pushfactor = |f: u32, s: &str| if n % f == 0 { result.push_str(s) };

	pushfactor(3, "Pling");
	pushfactor(5, "Plang");
	pushfactor(7, "Plong");

	if result.is_empty() {
		n.to_string()
	} else {
		result
	}
}
