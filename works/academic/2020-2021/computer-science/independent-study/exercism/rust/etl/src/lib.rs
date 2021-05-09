use std::collections::BTreeMap;

pub fn transform(h: &BTreeMap<i32, Vec<char>>) -> BTreeMap<char, i32> {
	let mut result: BTreeMap<char, i32> = BTreeMap::new();
	h.iter().for_each(|(x, y)| {
		for chr in y {
			result.insert(chr.to_ascii_lowercase(), *x);
		}
	});
	result
}
