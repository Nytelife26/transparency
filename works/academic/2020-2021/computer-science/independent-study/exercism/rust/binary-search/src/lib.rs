// using a non-mutative pointer variant to avoid duplicating the array in memory
pub fn find(array: &[i32], key: i32) -> Option<usize> {
	if array.len() == 0 {
		return None;
	}

	let mut start = 0usize;
	let mut stop = array.len() - 1;
	while start != stop {
		let mid = (start + stop) / 2;
		if key > array[mid] {
			start = mid + 1;
		} else {
			stop = mid;
		}
	}

	if array[stop] == key {
		Some(stop)
	} else {
		None
	}
}
