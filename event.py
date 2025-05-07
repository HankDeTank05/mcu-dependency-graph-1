class Event:

	def __init__(self, name: str):
		self._name = name

	# accessors

	def get_name(self) -> str:
		return self._name