#!/usr/bin/env python

# Hogwarts Sorting Hat Python Project

import sys

# Display Welcome Banner
print("Welcome To Hogwarts!\n")

# Display Instructions
print("You will be asked 5 questions to determine which house you will be joining.\nPlease answer the questions exactly how they were asked!\nGOOD LUCK!\n")

# Set Points To Zero
gryffindor = 0
hufflepuff = 0
ravenclaw = 0
slytherin = 0

# Question 1
trait = input("How would your friends describe you?\nBrave, Kind, Clever, or Cunning.\n")

if trait == "Brave":
  gryffindor = gryffindor + 1
elif trait == "Kind":
  hufflepuff = hufflepuff + 1
elif trait == "Clever":
  ravenclaw = ravenclaw + 1
elif trait == "Cunning":
  slytherin = slytherin + 1
else:
  print("Invalid trait:  '", trait, "'  Exiting.")
  sys.exit()

print("")

# Question 2
subject = input("What subject are you most looking forward to studying at Hogwarts?\nDefense Against the Dark Arts, Herbology, Potions, or Charms.\n")

if subject == "Defense Against the Dark Arts":
  gryffindor = gryffindor + 1
elif subject == "Herbology":
  hufflepuff = hufflepuff + 1
elif subject == "Potions":
  syltherin = slytherin + 1
elif subject == "Charms":
  ravenclaw = ravenclaw + 1
else:
  print("Invalid subject:  '", subject, "'  Exiting.")
  sys.exit()

print("")

# Question 3
history = input("How would you like to be known to history?\nThe Wise, The Good, The Bold, or The Great.\n")

if history == "The Wise":
  ravenclaw = ravenclaw + 1
elif history == "The Good":
  hufflepuff = hufflepuff + 1
elif history == "The Bold":
  gryffindor = gryffindor + 1
elif history == "The Great":
  slytherin = slytherin + 1
else:
  print("Invalid trait:  '", history, "'  Exiting.")
  sys.exit()

print("")

# Question 4
potion = input("Given the choice, would you rather create a potion that would guarantee you:\nLove, Glory, Wisdom, or Power?\n")

if potion == "Love":
  hufflepuff = hufflepuff + 1
elif potion == "Glory":
  gryffindor = gryffindor + 1
elif potion == "Wisdom":
  ravenclaw = ravenclaw + 1
elif potion == "Power":
  slytherin = slytherin + 1
else:
  print("Invalid potion:  '", potion, "'  Exiting.")
  sys.exit()

print("")

# Question 5
deathlyhallow = input("Choose a Deathly Hallow:\nThe Elder Wand, The Resurrection Stone, or The Cloak of Invisibility?\n")

if deathlyhallow == "The Elder Wand":
  gryffindor = gryffindor + 1
elif deathlyhallow == "The Resurrection Stone":
  slytherin = slytherin + 1
elif deathlyhallow == "The Cloak of Invisibility":
  hufflepuff = hufflepuff + 1
  ravenclaw = ravenclaw + 1
else:
  print("Invalid Deathly Hallow:  '", deathlyhallow, "'  Exiting.")
  sys.exit()

print("")

# Count Points
print("Gryffindor:", gryffindor, "points.")
print("Hufflepuff:", hufflepuff, "points.")
print("Ravenclaw:", ravenclaw, "points.")
print("Slytherin:", slytherin, "points.")

print("")

# Sort Into A House
if gryffindor >= ravenclaw and gryffindor >= hufflepuff and gryffindor >= slytherin:
  house = "Gryffindor"
  print("You belong to Gryffindor!")
elif ravenclaw >= gryffindor and ravenclaw >= hufflepuff and ravenclaw >= slytherin:
  house = "Ravenclaw"
  print("You belong to Ravenclaw!")
elif hufflepuff >= ravenclaw and hufflepuff >= gryffindor and hufflepuff >= slytherin:
  house = "Hufflepuff"
  print("You belong to Hufflepuff!")
elif slytherin >= gryffindor and slytherin >= ravenclaw and slytherin >= hufflepuff:
  house = "Slytherin"
  print("You belong to Slytherin!")

print("")

# Describe Your House
if house == "Gryffindor":
  print("GRYFFINDOR:")
  print("")
  print("'You might belong in Gryffindor, where dwell the brave of heart. Their daring, nerve, and chivalry set Gryffindors apart.'")
  print("")
  print("Traits: Courage, Chivalry, and Strong Moral Compass.")
  print("")
  print("Notable Members: Harry Potter, Albus Dumbledore, Ron Weasley, and Hermione Granger.")
elif house == "Hufflepuff":
  print("HUFFLEPUFF:")
  print("")
  print("'You might belong in Hufflepuff, where they are just and loyal. Those patient Hufflepuffs are true and unafraid of toil.'")
  print("")
  print("Traits: Loyalty, Dedication, and Humbleness.")
  print("")
  print("Notable Members: Newt Scamander, Cedric Diggory, and Nymphadora Tonks.")
elif house == "Ravenclaw":
  print("RAVENCLAW:")
  print("")
  print("'Or yet in wise old Ravenclaw, if you've a ready mind, where those of wit and learning can always find their kind.'")
  print("")
  print("Traits: Intelligence, Creativity, and Individuality.")
  print("")
  print("Notable Members: Luna Lovegood, Gilderoy Lockhart, and Filius Flitwick.")
elif house == "Slytherin":
  print("SLYTHERIN:")
  print("")
  print("'Or perhaps in Slytherin you'll make your real friends. Those cunning folk use any means to achieve their ends.'")
  print("")
  print("Traits: Ambition, Cunning, and Resourcefulness.")
  print("")
  print("Notable Members: Tom Riddle, Severus Snape, and Draco Malfoy.")

print("")
