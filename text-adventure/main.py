from room import Room

print("---------------------------")
print("Welcome to my Textadventure")
print("---------------------------")
print("")
print("init started...")
print("")
kitchen = Room("Kitchen")
kitchen.set_description("A dark and dirty room buzzing with flies.")
print("")
print("init finised...")

kitchen.describe()

print("-------------")
print("<--- END --->")
print("-------------")
# input("finished - Press Enter to close")