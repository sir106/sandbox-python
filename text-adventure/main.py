from room import Room
from character import Character

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
print("")
print("init finished...")

# dining_hall.get_details()

current_room = kitchen          

# new character dave
dave = Character("Dave", "A smelly zombie")
dave.talk()
dave.set_conversation("howdy, brother! how you're doing?")


while True:		
    print("\n")         
    current_room.get_details()         
    command = input("> ")    
    current_room = current_room.move(command)
    dave.talk()

print("-------------")
print("<--- END --->")
print("-------------")
# input("finished - Press Enter to close")