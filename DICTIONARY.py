#BRIANNE KELLY R. OLLOS
#DICTIONARY

print(" ")
print("NBA PLAYER")
print(" ")
player = {
            "Kawhi Leonard" : "SPURS",
            "James Harden" : "ROCKETS",
            "Russel Westbrook" : "THUNDER",
            "Lebron James" : "CAVALIERS",
            "Kevin Durant" : "WARRIORS",
            "Anthony Davis" : "PELICANS",
            "Kemba Walker" : "HORNETS",
            "Kyrie Irving" : "CELTICS",
            "Dwyane Wade" : "HEAT",
            "Demar Derozan" : "RAPTORS",
            "Damian Lillard" : "TRAILBLAZER",
            "Joel Emniid" : "76ERS",
            "John Wall" : "WIZARDS",
            "Victor Oladipo" : "PACERS",
            "Giannis Antetokounmpo" : "BUCKS"
    }

for key, val in player.items():
    print(key, "===", val)

#add in dictionary
player["Kristaps Porzingis"] = "KNICKS"
player["Andre Drummond"] = "PISTONS"
player["Donovan Mitchell"] = "JAZZ"
player["Jimmy Butler"] = "TIMBERWOLVES"
player["Nicola Jokic"] = "NUGGETS"
player["Andre Jordan"] = "CLIPPERS"

print("-"*10)

for key, value in sorted(player.items()):     #SORT
    print(key, "===", value)
