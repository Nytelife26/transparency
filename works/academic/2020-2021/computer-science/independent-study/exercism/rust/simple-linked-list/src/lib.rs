use std::iter::FromIterator;

struct Node<T> {
	data: T,
	next: Link<T>,
}

type Link<T> = Option<Box<Node<T>>>;

pub struct SimpleLinkedList<T> {
	head: Link<T>,
}

impl<T> SimpleLinkedList<T> {
	pub fn new() -> Self {
		SimpleLinkedList { head: None }
	}

	pub fn is_empty(&self) -> bool {
		match self.head {
			Some(_) => false,
			None => true,
		}
	}

	pub fn len(&self) -> usize {
		let mut result = 0usize;
		let mut next = &self.head;
		while let Some(node) = next {
			result += 1usize;
			next = &node.next;
		}
		result
	}

	pub fn push(&mut self, element: T) {
		let new = Box::new(Node {
			data: element,
			next: self.head.take(),
		});
		self.head = Some(new);
	}

	pub fn pop(&mut self) -> Option<T> {
		self.head.take().map(|node| {
			self.head = node.next;
			node.data
		})
	}

	pub fn peek(&self) -> Option<&T> {
		self.head.as_ref().map(|node| &node.data)
	}

	pub fn rev(self) -> SimpleLinkedList<T> {
		let mut result = SimpleLinkedList::new();
		let mut next = self.head;
		while let Some(node) = next {
			result.push(node.data);
			next = node.next;
		}
		result
	}
}

impl<T> FromIterator<T> for SimpleLinkedList<T> {
	fn from_iter<I: IntoIterator<Item = T>>(iter: I) -> Self {
		let mut result = SimpleLinkedList::new();
		for i in iter {
			result.push(i);
		}
		result
	}
}

impl<T> Into<Vec<T>> for SimpleLinkedList<T> {
	fn into(self) -> Vec<T> {
		let mut result = Vec::new();
		let mut next = self.head;
		while let Some(node) = next {
			result.insert(0, node.data);
			next = node.next;
		}
		result
	}
}
