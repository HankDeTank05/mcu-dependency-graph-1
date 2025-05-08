# language imports
import typing

# my imports
import project as p

DEP_WEAK: str = "weak"
DEP_STRONG: str = "strong"

class Dependency:

	# specialized constructor
	def __init__(self, tail: p.Project, head: p.Project, strength: str):
		assert(strength == DEP_WEAK or strength == DEP_STRONG)
		self._tail: p.Project = tail # the preceding project, that is depended upon
		self._depender: p.Project = head # the following project, that is depending on the prior
		self._strength: str = strength

	# string representation of a dependency
	def __str__(self) -> str:
		out_str: str = self._tail.get_name()
		if self._strength == DEP_WEAK:
			out_str += ' ---> '
		elif self._strength == DEP_STRONG:
			out_str += ' ===> '
		else:
			assert(False) # crash if we don't recognize the dependency strength value
		out_str += self._depender.get_name()
		return out_str
	
	# comparison operator overloads

	# ==
	def __eq__(self, other) -> bool:
		# two dependencies are equivalent if...
		#	- their "dependency" projects are equivalent
		#	- their "depender" projects are equivalent
		#	- their dependency strength is equivalent
		assert(isinstance(other, Dependency)) # crash if we're comparing to anything other than a Dependency object
		return self._tail == other._tail and self._depender == other._depender and self._strength == other._strength
	
	# accessors
	def get_tail_project(self) -> p.Project:
		return self._tail
	
	def get_tail_name(self) -> str:
		return self._tail.get_name()
	
	def get_head_project(self) -> p.Project:
		return self._head
	
	def get_head_name(self) -> str:
		return self._depender.get_name()
	
	def get_connection_strength(self) -> str:
		return self._strength