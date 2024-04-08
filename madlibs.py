# String concatination (putting strings together)
# hot to:

# string2 = "This is string2"

# 1. print ("string1 " + string2) 
# 2. print ("string1 {}".format(string2)) 
# 3. print (f"string1 {string2}")

noun = input("Who: ")
adj = input("Adjective: ")
Verb1 = input("Verb: ")
Verb2 = input("Verb: ")
Verb3 = input("Verb: ")
Verb4 = input("Verb: ")
Verb5 = input("Verb: ")

madlibs = f"{noun} is a somewhat {adj} programmer. They are good at {Verb1}, {Verb2} and {Verb3}. \
You would think it ends there, right? Nope, they are also great at {Verb4} with mastery in {Verb5}. \
That is the story of {noun}"

print(madlibs)

