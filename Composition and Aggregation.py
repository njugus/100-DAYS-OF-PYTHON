# composition example 1

class Room:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def room_info(self):
        print(f" Room Name : {self.name}")
        print(f" Room Area : {self.area}")


class House:
    def __init__(self, address):
        self.address = address
        self.rooms = []

    def add_rooms(self, name, area):
        room = Room(name, area)
        return self.rooms.append(room)

    def available_rooms(self):
        for room in self.rooms:
            room.room_info()


house_system = House("841 LIMURU")
house_system.add_rooms("Bedroom", 25)
house_system.add_rooms("Living Room", 24)
house_system.available_rooms()