# my imports
import dependency as d
import data_projects as pdata

dependencies: list[d.Dependency] = [
	# ph1 internal
	d.Dependency(pdata.im1, pdata.im2, d.DEP_STRONG),
	d.Dependency(pdata.im2, pdata.hulk, d.DEP_WEAK),
	d.Dependency(pdata.im2, pdata.thor1, d.DEP_WEAK),
	d.Dependency(pdata.cap1, pdata.im2, d.DEP_WEAK),
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
	d.Dependency(pdata.civil_war, pdata.spidey_home2, d.DEP_STRONG),

	# ??? -> civil war
	d.Dependency(pdata.am1, pdata.civil_war, d.DEP_WEAK),
	d.Dependency(pdata.cap2, pdata.civil_war, d.DEP_STRONG),
	d.Dependency(pdata.avengers, pdata.civil_war, d.DEP_WEAK),
	d.Dependency(pdata.age_of_ultron, pdata.civil_war, d.DEP_STRONG),
	
	# ??? -> ph3
	d.Dependency(pdata.avengers, pdata.spidey_home1, d.DEP_STRONG),
	d.Dependency(pdata.guardians1, pdata.guardians2, d.DEP_STRONG),
	d.Dependency(pdata.age_of_ultron, pdata.thor3, d.DEP_STRONG),
	d.Dependency(pdata.am1, pdata.am2, d.DEP_STRONG),

	# civil war -> ???
	d.Dependency(pdata.civil_war, pdata.spidey_home1, d.DEP_STRONG),
	d.Dependency(pdata.civil_war, pdata.bp1, d.DEP_STRONG),
	d.Dependency(pdata.civil_war, pdata.am2, d.DEP_STRONG),

	# other ph3 internal
	d.Dependency(pdata.ds1, pdata.thor3, d.DEP_WEAK),
	d.Dependency(pdata.cm, pdata.spidey_home2, d.DEP_WEAK),
	d.Dependency(pdata.infinity_war, pdata.cm, d.DEP_WEAK),

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
	d.Dependency(pdata.endgame, pdata.eternals, d.DEP_WEAK),
	d.Dependency(pdata.endgame, pdata.thor4, d.DEP_STRONG),
	d.Dependency(pdata.endgame, pdata.bp2, d.DEP_STRONG),
	d.Dependency(pdata.endgame, pdata.am3, d.DEP_WEAK),
	d.Dependency(pdata.endgame, pdata.guardians3, d.DEP_STRONG),
	d.Dependency(pdata.endgame, pdata.marvels, d.DEP_WEAK),
	d.Dependency(pdata.endgame, pdata.wandavision, d.DEP_STRONG),
	d.Dependency(pdata.endgame, pdata.tfatws, d.DEP_STRONG),
	d.Dependency(pdata.endgame, pdata.loki_s1, d.DEP_STRONG),
	d.Dependency(pdata.endgame, pdata.hawkeye, d.DEP_STRONG),
	d.Dependency(pdata.endgame, pdata.secret_invasion, d.DEP_WEAK),
	d.Dependency(pdata.endgame, pdata.ds2, d.DEP_STRONG),
	d.Dependency(pdata.endgame, pdata.am3, d.DEP_STRONG),
	d.Dependency(pdata.endgame, pdata.shehulk, d.DEP_STRONG),
	d.Dependency(pdata.endgame, pdata.shang_chi, d.DEP_WEAK),

	# ??? -> ph4
	d.Dependency(pdata.civil_war, pdata.bw, d.DEP_STRONG),
	d.Dependency(pdata.hulk, pdata.shang_chi, d.DEP_WEAK),
	d.Dependency(pdata.ds1, pdata.shang_chi, d.DEP_WEAK),
	d.Dependency(pdata.im3, pdata.shang_chi, d.DEP_STRONG),
	d.Dependency(pdata.spidey_home2, pdata.spidey_home3, d.DEP_STRONG),
	d.Dependency(pdata.hulk, pdata.shehulk, d.DEP_STRONG),
	d.Dependency(pdata.cm, pdata.shang_chi, d.DEP_WEAK),

	# ph4 internal
	d.Dependency(pdata.spidey_home3, pdata.ds2, d.DEP_WEAK),
	d.Dependency(pdata.bw, pdata.tfatws, d.DEP_WEAK),
	d.Dependency(pdata.tfatws, pdata.bw, d.DEP_WEAK),
	d.Dependency(pdata.wandavision, pdata.ds2, d.DEP_STRONG),
	d.Dependency(pdata.shang_chi, pdata.shehulk, d.DEP_WEAK),

	# ??? -> ph5
	d.Dependency(pdata.bw, pdata.tbolts, d.DEP_STRONG),
	d.Dependency(pdata.msmarvel, pdata.marvels, d.DEP_STRONG),
	d.Dependency(pdata.wandavision, pdata.marvels, d.DEP_STRONG),
	d.Dependency(pdata.hawkeye, pdata.marvels, d.DEP_WEAK),
	d.Dependency(pdata.cm, pdata.secret_invasion, d.DEP_STRONG),
	d.Dependency(pdata.loki_s1, pdata.loki_s2, d.DEP_STRONG),
	d.Dependency(pdata.loki_s1, pdata.am3, d.DEP_STRONG),
	d.Dependency(pdata.whatif_s1, pdata.whatif_s2, d.DEP_STRONG),
	d.Dependency(pdata.hawkeye, pdata.echo, d.DEP_STRONG),
	d.Dependency(pdata.loki_s1, pdata.dp_n_wolv, d.DEP_STRONG),
	d.Dependency(pdata.am2, pdata.tbolts, d.DEP_WEAK),
	d.Dependency(pdata.tfatws, pdata.tbolts, d.DEP_STRONG),
	d.Dependency(pdata.spidey_home3, pdata.echo, d.DEP_WEAK),
	d.Dependency(pdata.spidey_home3, pdata.dd_bornagain, d.DEP_WEAK),
	d.Dependency(pdata.cm, pdata.marvels, d.DEP_STRONG),
	d.Dependency(pdata.tfatws, pdata.cap4, d.DEP_STRONG),
	d.Dependency(pdata.wandavision, pdata.agatha, d.DEP_STRONG),
	d.Dependency(pdata.hulk, pdata.cap4, d.DEP_STRONG),

	# ph5 internal
	d.Dependency(pdata.whatif_s2, pdata.whatif_s3, d.DEP_STRONG),
	d.Dependency(pdata.echo, pdata.dd_bornagain, d.DEP_STRONG),
	d.Dependency(pdata.loki_s2, pdata.dp_n_wolv, d.DEP_WEAK),

	# ??? -> ph6
	d.Dependency(pdata.spidey_home3, pdata.spidey_bnd, d.DEP_STRONG),
	d.Dependency(pdata.tbolts, pdata.f4, d.DEP_WEAK),

	# ??? -> doomsday
	d.Dependency(pdata.f4, pdata.doomsday, d.DEP_STRONG),
	d.Dependency(pdata.tbolts, pdata.doomsday, d.DEP_STRONG),
	d.Dependency(pdata.shang_chi, pdata.doomsday, d.DEP_STRONG),
	d.Dependency(pdata.cap4, pdata.doomsday, d.DEP_STRONG),
	d.Dependency(pdata.thor4, pdata.doomsday, d.DEP_STRONG),
	d.Dependency(pdata.bp2, pdata.doomsday, d.DEP_STRONG),
	d.Dependency(pdata.loki_s2, pdata.doomsday, d.DEP_WEAK),
	d.Dependency(pdata.am3, pdata.doomsday, d.DEP_STRONG),
	d.Dependency(pdata.dp_n_wolv, pdata.doomsday, d.DEP_STRONG),

	# ph6 internal
	d.Dependency(pdata.doomsday, pdata.secret_wars, d.DEP_STRONG),

	# TODO: categorize these
	d.Dependency(pdata.spidey_home3, pdata.shehulk, d.DEP_WEAK),
	d.Dependency(pdata.shehulk, pdata.echo, d.DEP_WEAK),




]