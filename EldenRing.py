import random

intbuilds = [
    "Battlemage",
    "Carian",
    "Spellknight",
    "Cold-Blooded Raptor",
    "Crystal Mage",
    "Dark Knight",
    "Darkmoon Spellblade",
    "Deathblade",
    "Death Knight",
    "Mage",
    "Magus",
    "Moonveil Samurai",
    "Moonveil Shinobi",
    "Royal Knight",
    "Sorcerer",
    "Spellblade",
    "Sword Sage",
]

faithbuilds = [
    "Blackflame Apostle",
    "Blackflame Bushido",
    "Blackflame Spellblade",
    "Blasphemous Herald",
    "Crusader",
    "Deathblade",
    "Dragon Priest",
    "Elementalist",
    "Hellfire Herald",
    "Golden Eye",
    "Lightning Lancer",
    "Paladin",
    "Sword Sage",
    "Templar",
]

arcanebuilds = [
    "Blood Danceer",
    "Blood Dragon",
    "Dragon Knight",
    "Dragon Warrior",
    "Eochaid Executioner",
    "Frenzied Acolyte",
    "Sanguine Samurai",
]

strengthbuilds = [
    "Barbarian",
    "Berserker",
    "Blasphemous Beastmaster",
    "Blasphemous Herald",
    "Blazing Bushido",
    "Champion",
    "Cold-Blooded Raptor",
    "Colossal Knight",
    "Colossus Guardian",
    "Gravity God",
    "Magic Archer",
    "Royal Knight",
    "Scorching Slayer",
    "Sorcery Sentinel",
    "Venmous Bloodblade",
]

dexbuilds = [
    "Blackflame Bushido",
    "Blazing Bushido",
    "Blood Blade",
    "Gravity God",
    "Lightning Dragoon",
    "Moonveil Samurai",
    "Sanguine Samurai",
    "Samurai",
    "Thundering Swordspear",
    "Venmous Bloodblade",
]


classes = ("Int", "Faith", "Arcane", "Strength", "Dexterity")
c = random.choice(classes)

if c == "Int":
    print(
        "Congrats, fate has decided to give you an intelligence build, the build you've been given is: "
        + random.choice(intbuilds)
        + "!"
    )
elif c == "Faith":
    print(
        "Congrats, fate has decided to give you a faith build, the build you've been given is: "
        + random.choice(faithbuilds)
        + "!"
    )
elif c == "Arcane":
    print(
        "Congrats, fate has decided to give you a arcane build, the build you've been given is: "
        + random.choice(arcanebuilds)
        + "!"
    )
elif c == "Strength":
    print(
        "Congrats, fate has decided to give you a strength build, the build you've been given is: "
        + random.choice(strengthbuilds)
        + "!"
    )
elif c == "Dexterity":
    print(
        "Congrats, fate has decided to give you a dexterity build, the build you've been given is: "
        + random.choice(dexbuilds)
        + "!"
    )
else:
    print("What happened here?")
