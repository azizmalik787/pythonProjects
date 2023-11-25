def madlib():
    school_name = input("Enter School Name: ")
    adj1 = input("Enter Adjective: ")
    color = input("Enter Color: ")
    plural_noun = input("Enter Plural Noun: ")
    adj2 = input("Enter Adjective: ")
    animal = input("Enter Animal: ")
    adj3 = input("Enter Adjective: ")

    paragraph = f"At {school_name}, students were in for a {adj1} surprise. \
The cafeteria served {color} {plural_noun} for lunch, causing uproar! \
The principal danced a {adj2} jig to resolve the chaos, \
while the school mascot, a giant {animal}, cheered in the {adj3} gym."

    print(f"Your output paragraph is as follows:\n{paragraph}")
