from room import Room
from character import Character
from character import Enemy
from character import Friend

print("---------------------------")
print("Welcome to my Textadventure")
print("---------------------------")
print("")
print("init started...")
print("")
kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")

dining_hall = Room("Dining Hall")
dining_hall.set_description("A large room with ornate golden decorations on each wall.")

ballroom = Room("Ballroom")
ballroom.set_description("A vast room with a shiny wooden floor. Huge candlesticks guard the entrance.")

print("linking rooms...")
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")
print("linking finished!")
dining_hall.show_linked_rooms()
print("wait for adding zombies...")
dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Brrlgrh... rgrhl... brains...")
dave.set_weakness("cheese")
dining_hall.set_character(dave)
print("")
print("init finished...")

# dining_hall.get_details()

current_room = kitchen          

# new character dave
dave = Character("Dave", "A smelly zombie")
dave.set_conversation("howdy, brother! how you're doing?")


dead = False

while dead == False:	
    print("\n")         
    current_room.get_details()    

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()     
    
    command = input("> ")    
    
    if command in ["north", "south", "east", "west"]:
        # Move in the given direction
        current_room = current_room.move(command)
    elif command == "talk":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
          inhabitant.talk()
    elif command == "fight":
        # You can check whether an object is an instance of a particular
        # class with isinstance() - useful! This code means
        # "If the character is a Friend"
        if inhabitant == None or isinstance(inhabitant, Friend):
            print("There is no one here to fight with")
        else:
            # Fight with the inhabitant, if there is one
            print("What will you fight with?")
            fight_with = input()
            if inhabitant.fight(fight_with) == True:
                # What happens if you win?
                print("Hooray, you won the fight!")
                current_room.set_character(None)
            else:
                # What happens if you lose?
                print("Oh dear, you lost the fight.")
                print("That's the end of the game")
                dead = True
    elif command == "hug":
        if inhabitant == None:
            print("There is no one here to hug :(")
        else:
            if isinstance(inhabitant, Enemy):
                print("I wouldn't do that if I were you...")
            else:
                inhabitant.hug()
    else:
        print("unknown command!")
      
print("-------------")
print("<--- END --->")
print("-------------")
# input("finished - Press Enter to close")