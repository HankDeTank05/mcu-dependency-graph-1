# language imports
import datetime
import copy

# my imports
import character as c
import event as e

CHAR_MAIN: str = 'main'
CHAR_SECONDARY: str = 'secondary'
CHAR_CAMEO: str = 'cameo'

EVENT_HAPPENS: str = 'happens' # use this to denote when an event actually happens
EVENT_FOLLOWUP: str = 'follow-up' # use this to denote when an event's direct follow-up happens
EVENT_FALLOUT: str = 'fallout' # use this to denote when the fallout of an event affects a project
EVENT_REFERENCE: str = 'reference' # use this to denote when a project references an event

TYPE_MOVIE: str = 'movie'
TYPE_SEASON: str = 'season'

class Project:

	# specialized constructor
	def __init__(self, name: str, release_date: datetime.date, type: str, timeline_placement: datetime.date | None):
		self._name: str = name
		self._release_date: datetime.date = release_date
		self._characters: dict[str, list[c.Character]] = {
			CHAR_MAIN: [],
			CHAR_SECONDARY: [],
			CHAR_CAMEO: []
		}
		self._events: dict[str, list[e.Event]] = {
			EVENT_HAPPENS: [],
			EVENT_FOLLOWUP: [],
			EVENT_FALLOUT: [],
			EVENT_REFERENCE: []
		}
		self._type: str = type
		if timeline_placement is None:
			self._timeline_placement: datetime.date = release_date
		else:
			self._timeline_placement: datetime.date = timeline_placement

	# comparison operator overloads

	# <
	def __lt__(self, other) -> bool:
		assert(isinstance(other, Project)) # crash if we're not comparing to another Project object
		return self._release_date < other._release_date
	
	# >
	def __gt__(self, other) -> bool:
		assert(isinstance(other, Project)) # crash if we're not comparing to another Project object
		return self._release_date > other._release_date
	
	# <=
	def __le__(self, other) -> bool:
		assert(isinstance(other, Project)) # crash if we're not comparing to another Project object
		return self._release_date <= other._release_date
	
	# >=
	def __ge__(self, other) -> bool:
		assert(isinstance(other, Project)) # crash if we're not comparing to another Project object
		return self._release_date >= other._release_date
	
	# ==
	def __eq__(self, other) -> bool:
		assert(isinstance(other, Project)) # crash if we're not comparing to another Project object
		return self._release_date == other._release_date
	
	# !=
	def __ne__(self, other) -> bool:
		assert(isinstance(other, Project)) # crash if we're not comparing to another Project object
		return self._release_date != other._release_date

	# accessors

	def get_name(self) -> str:
		return self._name
	
	def get_release_date(self) -> datetime.date:
		return self._release_date
	
	def get_characters(self) -> dict[str, list[c.Character]]:
		return copy.deepcopy(self._characters)

	def get_character_count(self) -> int:
		count: int = 0
		for key in self._characters.keys():
			count += len(self._characters[key])
		return count

	def get_events(self) -> dict[str, list[e.Event]]:
		return copy.deepcopy(self._events)

	def get_event_count(self) -> int:
		count: int = 0
		for key in self._events.keys():
			count += len(self._events[key])
		return count

	def get_project_type(self) -> str:
		return self._type

	def get_timeline_placement(self) -> datetime.date:
		return self._timeline_placement

	# mutators

	def add_character(self, significance: str, character: c.Character) -> None:
		assert(significance in self._characters.keys())
		if character not in self._characters[significance]:
			self._characters[significance].append(character)
	
	def add_event(self, significance: str, event: e.Event) -> None:
		assert(significance in self._events.keys())
		if event not in self._events[significance]:
			self._events[significance].append(event)

class Movie(Project):

	def __init__(self, name: str, release_date: datetime.date, timeline_placement: datetime.date = None):
		super().__init__(name, release_date, TYPE_MOVIE, timeline_placement)

class Season(Project):

	def __init__(self, name: str, season_number: int, release_date: datetime.date, timeline_placement: datetime.date = None):
		season_name: str = f'{name} S{season_number}'
		super().__init__(season_name, release_date, TYPE_SEASON, timeline_placement)