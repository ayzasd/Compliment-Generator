import random
from colorama import Fore
thing = ["good", "ugly", "smart", "kind", "caring", "dumb", "stupid"]
compliment = "You are" + Fore.BLUE + f" {random.choice(thing)}"
def joke():
    return compliment