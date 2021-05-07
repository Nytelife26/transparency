use std::collections::HashMap;

macro_rules! attributes {
	() => {
		pub fn with_attrs(mut self, attrs: &[(&str, &str)]) -> Self {
			self.attrs = attrs
				.iter()
				.map(|x| (x.0.to_string(), x.1.to_string()))
				.collect::<HashMap<String, String>>();
			self
		}

		pub fn get_attr(&self, key: &str) -> Option<&str> {
			match self.attrs.get(key) {
				Some(value) => Some(value.as_str()),
				None => None,
			}
		}
	};
}

#[derive(Default)]
pub struct Graph {
	pub nodes: Vec<Node>,
	pub edges: Vec<Edge>,
	pub attrs: HashMap<String, String>,
}

impl Graph {
	pub fn new() -> Self {
		Self::default()
	}

	pub fn with_nodes(mut self, nodes: &Vec<Node>) -> Self {
		self.nodes = nodes.to_owned();
		self
	}

	pub fn with_edges(mut self, edges: &Vec<Edge>) -> Self {
		self.edges = edges.to_owned();
		self
	}

	pub fn get_node(self, id: &str) -> Node {
		match self.nodes.iter().find(|x| x.id == id) {
			Some(value) => value.to_owned(),
			None => panic!("Node {:?} not found.", id),
		}
	}

	attributes!();
}

#[derive(Clone, Debug, PartialEq, Eq)]
pub struct Node {
	pub id: String,
	pub attrs: HashMap<String, String>,
}

impl Node {
	pub fn new(id: &str) -> Self {
		Node {
			id: id.to_owned(),
			attrs: HashMap::new(),
		}
	}

	pub fn expect(self, _expectation: &str) -> Self {
		// it is unclear what expect should do, so i have not
		// implemented it here.
		self
	}

	attributes!();
}

#[derive(Clone, Debug, PartialEq, Eq)]
pub struct Edge {
	from: &'static str,
	to: &'static str,
	attrs: HashMap<String, String>,
}

impl Edge {
	pub fn new(from: &'static str, to: &'static str) -> Edge {
		Edge {
			from,
			to,
			attrs: HashMap::new(),
		}
	}

	attributes!();
}

pub mod graph {
	pub use super::Graph;
	pub mod graph_items {
		pub mod node {
			pub use super::super::super::Node;
		}
		pub mod edge {
			pub use super::super::super::Edge;
		}
	}
}
