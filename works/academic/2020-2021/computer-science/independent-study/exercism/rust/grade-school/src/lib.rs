use std::collections::BTreeMap;

#[derive(Default)]
pub struct School {
	students: BTreeMap<u32, Vec<String>>,
}

impl School {
	pub fn new() -> School {
		School::default()
	}

	pub fn add(&mut self, grade: u32, student: &str) {
		self.students.insert(
			grade,
			match self.students.get(&grade) {
				Some(students) => {
					let mut updated = students.to_owned();
					updated.push(student.to_string());
					updated.sort();
					updated
				}
				None => vec![student.to_string()],
			},
		);
	}

	pub fn grades(&self) -> Vec<u32> {
		self.students.keys().map(|x| *x).collect()
	}

	pub fn grade(&self, grade: u32) -> Vec<String> {
		match self.students.get(&grade) {
			Some(students) => students.to_owned(),
			None => Vec::new(),
		}
	}
}
