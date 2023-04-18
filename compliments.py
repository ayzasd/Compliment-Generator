import random
from colorama import Fore
thing = ["good", "smart", "kind", "caring", "passionate", "intelligent", "good at coding"]
compliment = "You are" + Fore.BLUE + f" {random.choice(thing)}"
def joke():
    return compliment