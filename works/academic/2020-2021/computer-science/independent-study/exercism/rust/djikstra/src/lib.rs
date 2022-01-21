type Link<T> = (Box<Node<T>>, u8);

pub struct Graph<T> {
	nodes: Vec<Node<T>>,
}

pub struct Node<T> {
	data: T,
	links: Vec<Link<T>>,
}

impl<T> Graph<T> {
	pub fn new(nodes: Option<Vec<Node<T>>>) -> Self {
		Graph {
			nodes: nodes.unwrap_or_else(|| Vec::new()),
		}
	}
}

impl<T> Node<T> {
	pub fn new(data: T, links: Option<Vec<Link<T>>>) -> Self {
		Node {
			data,
			links: links.unwrap_or_else(|| Vec::new()),
		}
	}

	pub fn can_access(&self, data: T) -> Self {
		self.links
			.iter()
			.map(|x| x.0.data)
			.collect::<Vec<T>>()
			.contains(data)
	}
}
