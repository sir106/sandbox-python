class Room():
    def __init__(self, room_name):
        self.name = room_name
        self.linked_rooms = {}
        self.description = "empty"
        print ("created room >"+self.name+"<")
    
    def get_description(self):
        return self.description

    def get_name(self):
        return self.name

    def set_description(self, room_description):    
        self.description = room_description
        print ("set description >"+self.description+"< for room >"+self.name+"<")
    
    def describe(self):
        print(self.description)

    def show_linked_rooms(self):
        print( self.name + " linked rooms :" + repr(self.linked_rooms) )

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link
        print ("linked room >"+direction+"< to room >"+self.name+"<")
    
    def get_details(self):
        print(self.name)
        print("------------------")
        print(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print( "The " + room.get_name() + " is " + direction)

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
        return self