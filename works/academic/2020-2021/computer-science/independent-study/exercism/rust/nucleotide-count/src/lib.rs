use std::collections::HashMap;

const RNA: [char; 4] = ['A', 'C', 'G', 'T'];

pub fn count(nucleotide: char, dna: &str) -> Result<usize, char> {
	if !RNA.contains(&nucleotide) {
		return Err(nucleotide);
	}
	let mut count = 0usize;
	for chr in dna.chars() {
		if nucleotide == chr {
			count += 1usize;
		} else if !RNA.contains(&chr) {
			return Err(chr);
		}
	}
	Ok(count)
}

pub fn nucleotide_counts(dna: &str) -> Result<HashMap<char, usize>, char> {
	let mut result = HashMap::with_capacity(4);
	RNA.iter().for_each(|x| {
		result.insert(*x, 0usize);
	});
	for chr in dna.chars() {
		if !RNA.contains(&chr) {
			return Err(chr);
		}
		result.insert(chr, result[&chr] + 1usize);
	}
	Ok(result)
}
