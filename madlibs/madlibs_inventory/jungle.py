def madlib():
    adj1 = input("Enter Adjective: ")
    noun1 = input("Enter Noun: ")
    plural_noun = input("Enter Plural Noun: ")
    adj2 = input("Enter Adjective: ")
    animal = input("Enter Animal: ")
    color = input("Enter Color: ")
    noun2 = input("Enter Noun: ")
    adj3 = input("Enter Adjective: ")

    paragraph = f"Deep in the {adj1} jungle, explorers found a {noun1} full of {plural_noun}. \
As they ventured further, they encountered a {adj2} {animal} and a {color} {noun2}! \
Excitement filled the air as they discovered a hidden {adj3} temple."

    print(f"Your output paragraph is as follows:\n{paragraph}")
