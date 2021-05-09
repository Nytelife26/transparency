// there is REALLY no need for an object oriented approach here.
// so for those that just want a simple elegant solution, here:
pub fn convert(dna: char) -> Result<char, char> {
	match dna {
		'G' => Ok('C'),
		'C' => Ok('G'),
		'T' => Ok('A'),
		'A' => Ok('U'),
		_ => Err(dna),
	}
}

pub fn dna_to_rna(dna: &str) -> Result<String, char> {
	dna.chars().map(convert).collect()
}

// OOP variant:
const DNA_NUCLEOTIDES: [char; 4] = ['G', 'C', 'T', 'A'];
const RNA_NUCLEOTIDES: [char; 4] = ['C', 'G', 'A', 'U'];

#[derive(Debug, PartialEq)]
pub struct Dna {
	sequence: String,
}

#[derive(Debug, PartialEq)]
pub struct Rna {
	sequence: String,
}

impl Dna {
	pub fn new(dna: &str) -> Result<Dna, usize> {
		for (pos, chr) in dna.char_indices() {
			if !DNA_NUCLEOTIDES.contains(&chr) {
				return Err(pos);
			}
		}
		Ok(Dna {
			sequence: dna.to_string(),
		})
	}

	pub fn into_rna(self) -> Rna {
		Rna {
			sequence: self
				.sequence
				.chars()
				.map(|x| {
					RNA_NUCLEOTIDES
						[DNA_NUCLEOTIDES.iter().position(|i| *i == x).unwrap()]
				})
				.collect(),
		}
	}
}

impl Rna {
	pub fn new(rna: &str) -> Result<Rna, usize> {
		for (pos, chr) in rna.char_indices() {
			if !RNA_NUCLEOTIDES.contains(&chr) {
				return Err(pos);
			}
		}
		Ok(Rna {
			sequence: rna.to_string(),
		})
	}
}
