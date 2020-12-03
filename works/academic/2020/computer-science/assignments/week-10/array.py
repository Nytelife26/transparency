class array:
	"""This class implements the concept of arrays, based on Python's `list`.
	It has fixed size (will never expand or shrink) and fixed types (no value can be assigned a different type than the array was instantiated with).

	kwargs:
		`size`: `int` denoting the number of elements the array will have
		`types`: `class` for which all array elements will be an instance of
		`default`: Default value for which to instantiate `types` for all elements"""

	def __init__(self, size, types, default):
		"""Create an array of `size` with exclusive data type of `types`."""

		self.__type__ = types(default)
		self.__list__ = [self.__type__ for x in range(size)]

	def __getitem__(self, key):
		"""Return the value of `key` in the array."""

		return self.__list__[key]

	def __setitem__(self, key, val):
		"""Set the value of `key` in the array to `val`.

		Raise `TypeError` if the value is not the same type the array was instantiated with."""

		if type(val) != type(self.__type__):
			raise TypeError("The type of the value you are setting must match" \
				"the type the array was instantiated with.")
		self.__list__[key] = val

	def __delitem__(self, key):
		"""Delete `key` from the array, resetting it to the initial empty type."""

		self.__list__[key] = self.__type__

	def __len__(self):
		"""Return the length of the array."""

		return len(self.__list__)

	def __str__(self):
		"""Return the array in a printable string, in list format."""

		return str(self.__list__)

	def __repr__(self):
		"""Returns self.__str__, for REPL, like IDLE."""

		return self.__str__()
