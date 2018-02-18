class Room():
    def __init__(self, room_name):
        self.name = room_name
        self.description = "empty"
        print ("created room >"+self.name+"<")
    
    def get_description(self):
        return self.description

    def set_description(self, room_description):    
        self.description = room_description
        print ("set description >"+self.description+"< for room >"+self.name+"<")
    
    def describe(self):
        print(self.description)
    