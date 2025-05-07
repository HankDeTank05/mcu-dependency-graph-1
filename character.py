import copy

class Character:

	def __init__(self, name: str | None, aliases: list[str] = []):
		self._name: str = name
		self._aliases: list[str] = aliases

	def get_name(self) -> str:
		return self._name
	
	def get_main_alias(self) -> str:
		return self._aliases[0]
	
	def get_all_aliases(self) -> list[str]:
		return copy.deepcopy(self._aliases)