# my imports
import dependency as d
import data_projects as pdata

dependencies: list[d.Dependency] = [
	# ph1 internal
	d.Dependency(pdata.im1, pdata.im2, d.DEP_STRONG),
	d.Dependency(pdata.im2, pdata.hulk, d.DEP_WEAK),
	d.Dependency(pdata.im2, pdata.thor1, d.DEP_WEAK),
	d.Dependency(pdata.im2, pdata.avengers, d.DEP_STRONG),
	d.Dependency(pdata.cap1, pdata.avengers, d.DEP_STRONG),
	d.Dependency(pdata.thor1, pdata.avengers, d.DEP_STRONG),
	d.Dependency(pdata.hulk, pdata.avengers, d.DEP_STRONG),
	
	# ph1 -> ph2
	d.Dependency(pdata.avengers, pdata.im3, d.DEP_STRONG),
	d.Dependency(pdata.avengers, pdata.thor2, d.DEP_STRONG),
	d.Dependency(pdata.avengers, pdata.cap2, d.DEP_STRONG),
	
	# ph2 internal
	d.Dependency(pdata.im3, pdata.age_of_ultron, d.DEP_STRONG),
	d.Dependency(pdata.thor2, pdata.age_of_ultron, d.DEP_STRONG),
	d.Dependency(pdata.cap2, pdata.age_of_ultron, d.DEP_STRONG),
	d.Dependency(pdata.age_of_ultron, pdata.am1, d.DEP_WEAK),
	d.Dependency(pdata.cap2, pdata.am1, d.DEP_WEAK),
	d.Dependency(pdata.thor2, pdata.guardians1, d.DEP_WEAK),
	
	# ph2 -> ph3
	d.Dependency(pdata.am1, pdata.civil_war, d.DEP_WEAK),
	d.Dependency(pdata.guardians1, pdata.guardians2, d.DEP_STRONG),
	d.Dependency(pdata.age_of_ultron, pdata.thor3, d.DEP_STRONG),
	d.Dependency(pdata.age_of_ultron, pdata.civil_war, d.DEP_STRONG),

	# civil war -> ???
	d.Dependency(pdata.civil_war, pdata.spidey_home1, d.DEP_STRONG),
	d.Dependency(pdata.civil_war, pdata.bp1, d.DEP_STRONG),
	d.Dependency(pdata.civil_war, pdata.am2, d.DEP_STRONG),

	# other ph3 internal
	d.Dependency(pdata.ds1, pdata.thor3, d.DEP_WEAK),

	# ??? -> infinity war
	d.Dependency(pdata.guardians2, pdata.infinity_war, d.DEP_STRONG),
	d.Dependency(pdata.thor3, pdata.infinity_war, d.DEP_STRONG),
	d.Dependency(pdata.spidey_home1, pdata.infinity_war, d.DEP_STRONG),
	d.Dependency(pdata.bp1, pdata.infinity_war, d.DEP_STRONG),
	d.Dependency(pdata.ds1, pdata.infinity_war, d.DEP_STRONG),

	# ??? -> endgame
	d.Dependency(pdata.infinity_war, pdata.endgame, d.DEP_STRONG),
	d.Dependency(pdata.am2, pdata.endgame, d.DEP_STRONG),
	d.Dependency(pdata.cm, pdata.endgame, d.DEP_WEAK),

	# endgame -> ???
	d.Dependency(pdata.endgame, pdata.spidey_home2, d.DEP_STRONG),

	# ph3 -> ph4
	d.Dependency(pdata.civil_war, pdata.bw, d.DEP_STRONG)

	# ph4 internal
	# ph4 -> ph5
	# ph5 internal
]