from room import Room

# Create data and description
kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies")
ballroom = Room("Ballroom")
ballroom.set_description("A vast room with a shiny wooden floor")
dining_hall = Room("Dining hall")
dining_hall.set_description("A large room with ornate golden decorations")

#Rooms directions
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")
#The room you are linking from is the object you call the method on, and the room you are linking to is the object you pass into the method.

kitchen.get_details()