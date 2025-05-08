# my imports
import dependency as d
import project as p

class DependencyGroup:

	def __init__(self):
		self._dependencies: list[d.Dependency] = []
		#					strength	tail		list of heads
		#					   vvv		 vvvvvvvvv  vvvvvvvvvvvvvvv
		self._connections: dict[str, dict[p.Project, list[p.Project]]] = {}

	def add(self, dep_to_add: d.Dependency) -> None:
		self._dependencies.append(dep_to_add)
		tail: p.Project = dep_to_add.get_tail_project()
		head: p.Project = dep_to_add.get_head_project()
		strength: str = dep_to_add.get_connection_strength()

		if strength not in self._connections.keys():
			self._connections[strength] = {}
		
		if tail not in self._connections[strength].keys():
			self._connections[strength][tail] = []

		self._connections[strength][tail].append(head)

	def create(self, tail_project: p.Project, head_project: p.Project, strength: str) -> None:
		self.add(d.Dependency(tail_project, head_project, strength))

	def get_dependency_sequence(self) -> list[p.Project]:
		# TODO: generate a sequence of dependencies
		# this list is generated such that the following are true
		#	- the item at index h is the head for a dependency between itself and the item at index h - 1
		#	- the item at index t is the tail for a dependency between itself and the item at index t + 1
		pass