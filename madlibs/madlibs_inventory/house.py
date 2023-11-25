def madlib():
    adj1 = input("Enter Adjective: ")
    num = input("Enter Number: ")
    plural_noun = input("Enter Plural Noun: ")
    adj2 = input("Enter Adjective: ")
    color = input("Enter Color: ")
    adj3 = input("Enter Adjective: ")
    noun = input("Enter Noun: ")


    paragraph = f"In the eerie {adj1} mansion, ghost hunters encountered {num} spooky {plural_noun}. \
Strange {adj2} noises echoed through the halls, while a {color} mist surrounded the {adj3} library. \
The mystery unfolded as they discovered a hidden {noun}!"

    print(f"Your output paragraph is as follows:\n{paragraph}")
