#User details

name = input("What is your name?")
age = input("How old are you?")

print("{} is a nice age to be, {}!".format(age, name))

color = input("What's your favourite color?")

print("{}? That's a nice color!".format(color))

animal = input("Can you tell me your favourite animal?")

print("{}? That means... you like {} {}s!".format(animal, color, animal))

place = input("If you could live anywhere, where would you want to live?")

print("So basically, you'd enjoy living in {} with a {} {}!".format(place, color, animal))

print(" ")

#Design a creature!

print ("Time to design a creature!")

creature_type = input("What type of animal do you want to design?")

creature_element = input("Okay, then pick an element for your {}!".format(creature_type))

creature_size = input("How big do you want your {} {} to be?".format(creature_element, creature_type))

print("So far, you have a {}, {} {}!".format(creature_size, creature_element, creature_type))

creature_name = input("Now that you've created your own awesome creature, time to name it!")

print("{}? That's a perfect name for your creature!".format(creature_name))

print(" ")




