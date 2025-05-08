import copy

class Character:

	# specialized constructor
	def __init__(self, name: str | None, aliases: list[str] = []):
		self._name: str = name
		self._aliases: list[str] = aliases

	# comparison operator overloads

	# ==
	def __eq__(self, other) -> bool:
		assert(isinstance(other, Character)) # crash if we're not comparing to another Character object

		# two Character objects are considered equal if...
		#	- their names are identical, and
		#	- their aliases are identical at the same index
		
		if self._name == other._name and len(self._aliases) == len(other._aliases):
			i: int = 0
			while i < len(self._aliases):
				if self._aliases[i] != other._aliases[i]:
					return False
				else:
					i += 1
			return True
		else:
			return False
		
	def __ne__(self, other) -> bool:
		return not(self == other)

	# accessors

	def get_name(self) -> str:
		return self._name
	
	def get_main_alias(self) -> str:
		return self._aliases[0]
	
	def get_all_aliases(self) -> list[str]:
		return copy.deepcopy(self._aliases)