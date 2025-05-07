# language imports
import typing

# my imports
import project as p

DEP_WEAK: str = "weak"
DEP_STRONG: str = "strong"

class Dependency:

	def __init__(self, dependency: p.Project, depender: p.Project, strength: str):
		assert(strength == DEP_WEAK or strength == DEP_STRONG)
		self._dependency: p.Project = dependency
		self._depender: p.Project = depender
		self._strength: str = strength

	def __str__(self) -> str:
		out_str: str = self._dependency.get_name()
		if self._strength == DEP_WEAK:
			out_str += ' ---> '
		elif self._strength == DEP_STRONG:
			out_str += ' ===> '
		out_str += self._depender.get_name()
		return out_str
	
	def get_dependency_name(self) -> str:
		return self._dependency.get_name()
	
	def get_depender_name(self) -> str:
		return self._depender.get_name()
	
	def get_connection_strength(self) -> str:
		return self._strength