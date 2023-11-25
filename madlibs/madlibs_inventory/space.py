def madlib():
    adj1 = input("Enter Adjective: ")
    noun1 = input("Enter Noun: ")
    adj2 = input("Enter Adjective: ")
    number = input("Enter Number: ")
    adj3 = input("Enter Adjective: ")
    noun2 = input("Enter Noun: ")
    adj4 = input("Enter Adjective: ")
    planet_name = input("Enter Planet Name: ")


    paragraph = f"In the vast {adj1} expanse of space, a brave {noun1} piloted their {adj2} spaceship. \
They encountered {number} {adj3} aliens, each with a peculiar {noun2}. \
Their mission was to uncover the {adj4} planet of {planet_name}."

    print(f"Your output paragraph is as follows:\n{paragraph}")
