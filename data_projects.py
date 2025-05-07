# language imports
import datetime

# my imports
import project as p
import data_characters as cdata

############
# projects #
############

# NOTE: all release dates are based on US release

# phase 1

im1: p.Movie = p.Movie("Iron Man", datetime.date(2008, 5, 2))
im1.add_character(p.CHAR_MAIN, cdata.tony)
im1.add_character(p.CHAR_SECONDARY, cdata.vision)
im1.add_character(p.CHAR_SECONDARY, cdata.rhodey)
im1.add_character(p.CHAR_SECONDARY, cdata.coulson)
im1.add_character(p.CHAR_SECONDARY, cdata.pepper)
im1.add_character(p.CHAR_SECONDARY, cdata.yinsen)
im1.add_character(p.CHAR_CAMEO, cdata.fury)

hulk: p.Movie = p.Movie("The\nIncredible\nHulk",
								   release_date=datetime.date(2008, 6, 13),
								   timeline_placement=datetime.date(2010, 6, 13)) # happens after iron man 2
hulk.add_character(p.CHAR_MAIN, cdata.hulk)
hulk.add_character(p.CHAR_SECONDARY, cdata.tbolt_ross)
hulk.add_character(p.CHAR_SECONDARY, cdata.betty_ross)
hulk.add_character(p.CHAR_SECONDARY, cdata.abomination)
hulk.add_character(p.CHAR_SECONDARY, cdata.leader)
hulk.add_character(p.CHAR_CAMEO, cdata.tony)

im2: p.Movie = p.Movie("Iron Man 2",
					   release_date=datetime.date(2010, 5, 7),
					   timeline_placement=datetime.date(2009, 5, 7)) # happens before incredible hulk
im2.add_character(p.CHAR_MAIN, cdata.tony)
im2.add_character(p.CHAR_SECONDARY, cdata.vision)
im2.add_character(p.CHAR_SECONDARY, cdata.rhodey)
im2.add_character(p.CHAR_SECONDARY, cdata.pepper)
im2.add_character(p.CHAR_SECONDARY, cdata.widow)
im2.add_character(p.CHAR_SECONDARY, cdata.fury)
# TODO: add post-credits scene characters

thor1: p.Movie = p.Movie("Thor", datetime.date(2011, 5, 6))
thor1.add_character(p.CHAR_MAIN, cdata.thor)
thor1.add_character(p.CHAR_MAIN, cdata.loki)
thor1.add_character(p.CHAR_SECONDARY, cdata.odin)
thor1.add_character(p.CHAR_SECONDARY, cdata.frigga)
thor1.add_character(p.CHAR_SECONDARY, cdata.heimdall)
thor1.add_character(p.CHAR_SECONDARY, cdata.sif)
# TODO: add post-credits scene characters

cap1: p.Movie = p.Movie("Captain America\nThe First Avenger",
						release_date=datetime.date(2011, 7, 22),
						timeline_placement=datetime.date(1940, 1, 1)) # TODO: figure out when in the 1940s this takes place
cap1.add_character(p.CHAR_MAIN, cdata.cap)
cap1.add_character(p.CHAR_MAIN, cdata.red_skull)
cap1.add_character(p.CHAR_SECONDARY, cdata.bucky)
cap1.add_character(p.CHAR_SECONDARY, cdata.zola)
cap1.add_character(p.CHAR_SECONDARY, cdata.peggy)
cap1.add_character(p.CHAR_SECONDARY, cdata.howard)
cap1.add_character(p.CHAR_CAMEO, cdata.fury)
# NOTE: not counting post-credits scene characters here since it's literally just a trailer for Avengers

avengers: p.Movie = p.Movie("The Avengers", datetime.date(2012, 5, 4))
avengers.add_character(p.CHAR_MAIN, cdata.tony)
avengers.add_character(p.CHAR_SECONDARY, cdata.vision)
avengers.add_character(p.CHAR_MAIN, cdata.cap)
avengers.add_character(p.CHAR_MAIN, cdata.thor)
avengers.add_character(p.CHAR_MAIN, cdata.hulk)
avengers.add_character(p.CHAR_MAIN, cdata.widow)
avengers.add_character(p.CHAR_MAIN, cdata.clint)
avengers.add_character(p.CHAR_MAIN, cdata.loki)
avengers.add_character(p.CHAR_SECONDARY, cdata.fury)
avengers.add_character(p.CHAR_SECONDARY, cdata.hill)
avengers.add_character(p.CHAR_SECONDARY, cdata.selvig)
avengers.add_character(p.CHAR_SECONDARY, cdata.coulson)
avengers.add_character(p.CHAR_CAMEO, cdata.pepper)
avengers.add_character(p.CHAR_CAMEO, cdata.sitwell)
avengers.add_character(p.CHAR_CAMEO, cdata.other)
avengers.add_character(p.CHAR_CAMEO, cdata.thanos)

# phase 2

im3: p.Movie = p.Movie("Iron Man 3", datetime.date(2013, 5, 3))
im3.add_character(p.CHAR_MAIN, cdata.tony)
im3.add_character(p.CHAR_SECONDARY, cdata.vision)
im3.add_character(p.CHAR_SECONDARY, cdata.rhodey)
im3.add_character(p.CHAR_CAMEO, cdata.yinsen)
im3.add_character(p.CHAR_CAMEO, cdata.hulk)

# NOTE: according to the D+ MCU timeline, thor 2 happens before iron man 3
# NOTE: but since these movies don't share any characters, idgaf about timeline

thor2: p.Movie = p.Movie("Thor\nThe Dark World", datetime.date(2013, 11, 8))
# TODO: add characters to thor2

cap2: p.Movie = p.Movie("Captain America\nThe Winter Soldier", datetime.date(2014, 4, 4))
# TODO: add characters to cap2

guardians1: p.Movie = p.Movie("Guardians\nof the\nGalaxy", datetime.date(2014, 8, 1))
# TODO: add characters to guardians1

age_of_ultron: p.Movie = p.Movie("Avengers\nAge of Ultron", datetime.date(2015, 5, 1))
# TODO: add characters to age of ultron

am1: p.Movie = p.Movie("Ant-Man", datetime.date(2015, 7, 17))
# TODO: add characters to antman

# phase 3

civil_war: p.Movie = p.Movie("Captain America\nCivil War", datetime.date(2016, 5, 6))
# TODO: add characters to civil war

ds1: p.Movie = p.Movie("Doctor Strange", datetime.date(2016, 11, 4))
# TODO: add characters to ds1

guardians2: p.Movie = p.Movie("Guardians\nof the\nGalaxy\nvol. 2",
							  release_date=datetime.date(2017, 5, 7),
							  timeline_placement=datetime.date(2014, 11, 1)) # takes place a few months after guardians 1
# TODO: add characters to guardians2

spidey_home1: p.Movie = p.Movie("Spider-Man\nHomecoming", datetime.date(2017, 7, 7))
# TODO: add characters to spiderman homecoming

thor3: p.Movie = p.Movie("Thor\nRagnarok", datetime.date(2017, 11, 3))
# TODO: add characters to thor3

bp1: p.Movie = p.Movie("Black Panther", datetime.date(2018, 2, 16))
# TODO: add characters to bp1

infinity_war: p.Movie = p.Movie("Avengers\nInfinity War", datetime.date(2018, 4, 27))
# TODO: add characters to infinity war

am2: p.Movie = p.Movie("Ant-Man\nand the Wasp",
					   release_date=datetime.date(2018, 7, 6),
					   timeline_placement=datetime.date(2018, 4, 1))
# TODO: add characters to antman and the wasp

cm: p.Movie = p.Movie("Captain Marvel",
					  release_date=datetime.date(2019, 3, 8),
					  timeline_placement=datetime.date(1995, 1, 1))
# TODO: add characters to captain marvel

endgame: p.Movie = p.Movie("Avengers\nEndgame",
						   release_date=datetime.date(2019, 4, 26),
						   timeline_placement=datetime.date(2023, 4, 26))
# TODO: add characters to endgame

spidey_home2: p.Movie = p.Movie("Spider-Man\nFar From Home",
								release_date=datetime.date(2019, 7, 2),
								timeline_placement=datetime.date(2023, 7, 2))
# TODO: add characters to spiderman far from home

# phase 4
bw: p.Movie = p.Movie("Black Widow", datetime.date(2021, 7, 9))
# TODO: add characters to black widow

# TODO: add shang chi
# TODO: add characters to shang chi

# TODO: add eternals
# TODO: add characters to eternals

# TODO: add no way home
# TODO: add characters to no way home

# TODO: add dsmom
# TODO: add characters to dsmom

# TODO: add thor4
# TODO: add characters to thor4

# TODO: add wakanda forever
# TODO: add characters to wakanda forever

# phase 5

# TODO: add quantumania
# TODO: add characters to quantumania

# TODO: add guardians3
# TODO: add characters to guardians3

# TODO: add the marvels
# TODO: add characters to the marvels

# TODO: add dp&wolverine
# TODO: add characters to dp&wolverine

# TODO: add cap4
# TODO: add characters to cap4

# TODO: add thunderbolts
# TODO: add characters to thunderbolts

# phase 6

# TODO: add f4
# TODO: add characters to f4

# TODO: add doomsday
# TODO: add characters to doomsday

# TODO: add spiderman brand new day
# TODO: add characters to brand new day

# TODO: add secret wars
# TODO: add characters to secret wars

# netflix

# NOTE: daredevil (s1) happens after guardians 2/i am groot and before AoU, timeline-wise

# NOTE: jessica jones (s2) happens after guardians 2/i am groot and before AoU, timeline-wise

# NOTE: luke cage (s1) happens after ant-man and before

"""
the complete timeline according to disney+

cap 1
agent carter one-shot
captain marvel
iron man 1
iron man 2
incredible hulk
a funny thing happened on the way to thor's hammer one-shot
thor
the consultant one-shot
avengers
item 47 one-shot
thor 2
iron man 3
all hail the king one-shot
cap 2
guardians 1
guardians 2
i am groot
daredevil (s1)
jessica jones (s1)
age of ultron
ant man
luke cage (s1)
iron fist (s1)
defenders
civil war
black widow
black panther
spider-man homecoming
punisher (s1)
doctor strange
thorgnarok
ant man and the wasp
infinity war
endgame
loki (s1)
	presumed: loki (s2)
what if (s1)
	presumed: what if (s2)
	presumed: what if (s3)
wandavision
shang-chi
falcon and the winter soldier
spider-man far from home
eternals
dsmom
hawkeye (s1)
moon knight (s1)
wakanda forever
echo (s1)
she-hulk (s1)
ms marvel (s1)
thor 4
werewolf by night
guardians holiday special
quantumania
guardians 3
secret invasion
marvels
deadpool & wolverine
agatha all along (s1)
daredevil born again (s1)

what's not accounted for?
- daredevil s2, s3
	- s2: happens after s1, before defenders
		- need to see if there's any "hand" involvement in iron fist to determine timeline placement relative to it
	- s3: happens after defenders, before infinity war
- jessica jones s2, s3
	- s2: happens after s1, before defenders
		- need to watch this
	- s3: happens after defenders, before infinity war
		- need to watch this
- luke cage s2
	- happens after defenders
		verdict:
- iron fist s2
	- happens after defenders
- loki s2
	- happens after loki s1, other timeline events are irrelevant (outside timeline)
		verdict: happens immediately after s1
- what if s2, s3
	- happens after what if s1, other timeline events are irrelevant (multiverse)
		verdict: happens immediately after s1
- punisher s2
	- happens after s1, before infinity war
		verdict: happens immediately after s1

- agent carter (abc) s1, s2
	verdict: presumed not canon

- agents of shield (abc) s1-7
	verdict: presumed not canon
"""

# NOTE: projects are listed in release order
projects: list[p.Project] = [
	# phase 1
	im1, hulk, im2, thor1, cap1, avengers,
	# phase 2
	im3, thor2, cap2, guardians1, age_of_ultron, am1,
	# phase 3
	civil_war, ds1, guardians2, spidey_home1, thor3, bp1, infinity_war, am2, cm, endgame, spidey_home2
]