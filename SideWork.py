import random
from listofbuilds import *

classes = ("Int", "Faith", "Arcane", "Strength", "Dexterity")
c = random.choice(classes)
print(c)

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
