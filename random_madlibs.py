from sample_madlibs import hp, code, zombie, hunger_games
import random

if __name__ == "__main__":
    m = random.choice([hp, code, zombie, hunger_games])
    m.madlib()