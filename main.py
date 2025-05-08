# language imports
import os

# library imports
import graphviz

# my imports (types)
import dependency as d
import project as p
import character as c

# my imports (data)
import data_projects as pdata
import data_dependencies as ddata

os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

mcu = graphviz.Digraph('mcu-graph', comment='MCU Dependency Graph')

'''
# phase 1
mcu.node(pdata.iron_man.get_name())
mcu.node(pdata.im2.get_name())
mcu.node(pdata.incredible_hulk.get_name())
mcu.node(pdata.thor1.get_name())
mcu.node(pdata.cap1.get_name())
mcu.node(pdata.avengers.get_name())

# phase 1 connections
mcu.edge(pdata.iron_man.get_name(), pdata.im2.get_name())
mcu.edge(pdata.im2.get_name(), pdata.incredible_hulk.get_name())
mcu.edge(pdata.im2.get_name(), pdata.avengers.get_name())
mcu.edge(pdata.incredible_hulk.get_name(), pdata.avengers.get_name())
mcu.edge(pdata.cap1.get_name(), pdata.avengers.get_name())
mcu.edge(pdata.thor1.get_name(), pdata.avengers.get_name())

# phase 2

# phase 1 -> 2 connections

# phase 2 connections
'''


def generate_from_dependency_list(dependency_list: list[d.Dependency]) -> None:
	
	# create nodes for every project
	for project in pdata.projects:
		mcu.node(project.get_name())

	# create edges for every dependency
	for dependency in dependency_list:
		# strong dependencies have a solid line
		if dependency.get_connection_strength() == d.DEP_STRONG:
			mcu.attr('edge', style='solid')

		# weak dependencies have a dashed line
		elif dependency.get_connection_strength() == d.DEP_WEAK:
			mcu.attr('edge', style='dashed')

		# create the edge
		# if dependency.get_connection_strength() == d.DEP_STRONG:
		mcu.edge(dependency.get_tail_name(), dependency.get_head_name())

def generate_manually() -> None:
	# generates a graph manually based on all the explicitly defined connections in data_dependencies.py
	generate_from_dependency_list(ddata.dependencies)

def generate_automatically() -> None:
	# generates a graph automatically based on character and event data
	# in order to do this, we need to automatically generate a list of dependency objects

	# a list of generated dependencies
	dep_list: list[d.Dependency] = []

	# a list of relevant projects (relevant = has one or more characters in its data)
	relevant_projects: list[p.Project] = []

	# for project1 in pdata.projects:
	# 	for main_char in project1.get_characters()[p.CHAR_MAIN]:
	# 		for project2 in pdata.projects:
	# 			if project1 != project2 \
	# 				and main_char in project2.get_characters()[p.CHAR_MAIN] \
	# 					and project1 < project2:
	# 				dep_list.append(d.Dependency(project1, project2, d.DEP_STRONG))

	for i1 in range(len(pdata.projects)):
		project1: p.Project = pdata.projects[i1]
		for main_char in project1.get_characters()[p.CHAR_MAIN]:
			for i2 in range(i1 + 1, len(pdata.projects)):
				project2: p.Project = pdata.projects[i2]
				if main_char in project2.get_characters()[p.CHAR_MAIN] and project1 < project2:
					dep_list.append(d.Dependency(project1, project2, d.DEP_STRONG))

	generate_from_dependency_list(dep_list)

# generate_manually()
generate_automatically()

mcu.render(view=True)