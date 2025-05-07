# my imports
import character as c

##############
# characters #
##############

# NOTE: only characters appearing more than once (or expected to reappear) will be recorded

# the original six avengers
tony: c.Character = c.Character("Tony Stark", ["Iron Man"])
cap: c.Character = c.Character("Steve Rogers", ["Captain America (1)"])
thor: c.Character = c.Character("Thor Odinson", ["Thor", "God of Thunder"])
hulk: c.Character = c.Character("Bruce Banner", ["Hulk", "Smart Hulk"])
widow: c.Character = c.Character("Natasha Romanoff", ["Black Widow"])
clint: c.Character = c.Character("Clint Barton", ["Hawkeye", "Ronin"])

# other superheroes
rhodey: c.Character = c.Character("James Rhodes", ["War Machine", "Iron Patriot", "Rhodey"])
bucky: c.Character = c.Character("James Buchanan Barnes", ["Winter Soldier", "Bucky"])
sam: c.Character = c.Character("Sam Wilson", ["Falcon", "Captain America (2)"])
wanda: c.Character = c.Character("Wanda Maximoff", ["Scarlet Witch"])
pietro: c.Character = c.Character("Pietro Maximoff", ["Quicksilver"])
vision: c.Character = c.Character("J.A.R.V.I.S.", ["Vision", "White Vision"])
loki: c.Character = c.Character("Loki Laufeson", ["Loki", "God of Mischief"])
odin: c.Character = c.Character("Odin")
frigga: c.Character = c.Character("Frigga")
heimdall: c.Character = c.Character("Heimdall")
sif: c.Character = c.Character("Sif", ["Lady Sif"])

# supervillains
abomination: c.Character = c.Character("Emil Blonsky", ["Abomination"])
leader: c.Character = c.Character("Samuel Sterns", ["Leader"])
red_skull: c.Character = c.Character("Johann Schmidt", ["Red Skull"])
zola: c.Character = c.Character("Arnim Zola")
thanos: c.Character = c.Character("Thanos", ["The Mad Titan"])
other: c.Character = c.Character("The Other")

# non-super iron man characters
pepper: c.Character = c.Character("Pepper Potts")
happy: c.Character = c.Character("Harold Hogan", ["Happy"])
yinsen: c.Character = c.Character("Ho Yinsen")

# non-super hulk characters
tbolt_ross: c.Character = c.Character("Thaddeus Ross", ["Thunderbolt Ross", "Red Hulk"])
betty_ross: c.Character = c.Character("Betty Ross")

# non-super thor characters
selvig: c.Character = c.Character("Erik Selvig")
darcy: c.Character = c.Character("Darcy Lewis")
jane: c.Character = c.Character("Jane Foster", ["Lady Thor"])

# shield people
fury: c.Character = c.Character("Nick Fury")
coulson: c.Character = c.Character("Phil Coulson")
hill: c.Character = c.Character("Maria Hill")
sitwell: c.Character = c.Character("Jasper Sitwell")
howard: c.Character = c.Character("Howard Stark")
peggy: c.Character = c.Character("Margaret Carter", ["Agent Carter", "Peggy"])
sharon: c.Character = c.Character("Sharon Carter", ["Agent 13", "Power Broker"])