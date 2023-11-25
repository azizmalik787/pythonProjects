from madlibs_inventory import house, school, jungle, space
import random

if __name__ == "__main__":
    script = random.choice([house, school, jungle, space])
    script.madlib()
