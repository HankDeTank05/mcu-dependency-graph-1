# language imports
import os

# library imports
import graphviz

# my imports
import dependency as d
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

# create nodes for every project
for project in pdata.projects:
	mcu.node(project.get_name())

# create edges for every dependency
for dependency in ddata.dependencies:
	# strong dependencies have a solid line
	if dependency.get_connection_strength() == d.DEP_STRONG:
		mcu.attr('edge', style='solid')

	# weak dependencies have a dashed line
	elif dependency.get_connection_strength() == d.DEP_WEAK:
		mcu.attr('edge', style='dashed')

	# create the edge
	# if dependency.get_connection_strength() == d.DEP_STRONG:
	mcu.edge(dependency.get_dependency_name(), dependency.get_depender_name())

mcu.render(view=True)