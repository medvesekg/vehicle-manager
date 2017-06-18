from Vehicle import Vehicle

vehicle_list = []


def user_input_prompt(prompt):
    user_input = raw_input(prompt)
    if user_input.lower() == "exit":
        exit()
    return user_input

def begin():
    while True:
        print "Would you like to create a new vehicle list or open and edit an existing one?"
        user_input = user_input_prompt("new/open: ")
        if user_input.lower() == "new":
            create_new_vehicle_list()
        elif user_input.lower() == "open":
            open_vehicle_list()
        else:
            continue
        review_vehicle_list()

def open_vehicle_list():
    global vehicle_list
    vehicle_list = []

    user_input = user_input_prompt("Enter the name of the file: ")
    try:
        with open(user_input, "r") as vehicle_file:
            content = vehicle_file.readlines()

        brands = []
        models = []
        odos = []
        services = []
        i = 3
        while i < len(content):
            brand = content[i].split()[1]
            brands.append(brand)
            i += 6
        i = 4
        while i < len(content):
            model = content[i].split()[1]
            models.append(model)
            i += 6
        i = 5
        while i < len(content):
            odo = content[i].split()[1]
            odos.append(odo)
            i += 6
        i = 6
        while i < len(content):
            service = content[i].split()[2]
            services.append(service)
            i += 6

        for i in range(0, len(brands)):
            vehicle_list.append(Vehicle(brands[i], models[i], odos[i], services[i]))
        print "File opened succesfuly."

    except:
        print "That file could not be opened"
        begin()



def create_new_vehicle_list():
    global vehicle_list
    vehicle_list = []
    print "Created a new vehicle list. Enter your first vehicle."
    add_vehicle()

def add_vehicle():
    while True:
        brand = user_input_prompt("Enter a brand: ")
        model = user_input_prompt("Enter a model: ")
        odometer = user_input_prompt("Enter the number of km: ")
        last_service = user_input_prompt("Enter date of last service: ")

        vehicle_list.append(Vehicle(brand,model,odometer,last_service))

        print "Would you like to add another vehicle?"
        add_another = user_input_prompt("y/n: ")
        if add_another.lower() == "n":
            break

def review_vehicle_list():

    print "You can: "
    print "Show the list to review it."
    print "Edit individual items on the list."
    print "Delete the list and start from the beginning."
    print "Add a new item to the list."
    print "Save the list to a file."

    while True:
        print "You have %s vehicles in your list." % len(vehicle_list)

        user_input = user_input_prompt("show/edit/delete/add/save: ")
        if user_input == "edit":
            show_vehicle_list()
            print "Enter the ID of the vehicle you would like to edit."
            user_input = user_input_prompt("ID: ")
            try:
                edit_vehicle(int(user_input))
            except:
                print "Not a valid ID"

        elif user_input == "delete":
            print "List deleted"
            break
        elif user_input == "show":
            show_vehicle_list()
        elif user_input == "save":
            save_to_file()
            break
        elif user_input == "add":
            add_vehicle()


def show_vehicle_list():
    print "Your vehicle list: \n"
    for i, vehicle in enumerate(vehicle_list):
        print "Vehicle ID: ", i
        print "Brand: ", vehicle.brand
        print "Model: ", vehicle.model
        print "ODO: ", vehicle.odometer
        print "Last Service: ", vehicle.last_service
        print "\n"


def edit_vehicle(vehicleID):
    while True:
        print "\nEditing vehicle ", vehicleID
        print "Brand: ", vehicle_list[vehicleID].brand
        print "Model: ", vehicle_list[vehicleID].model
        print "Odometer: ", vehicle_list[vehicleID].odometer
        print "Last_service: ", vehicle_list[vehicleID].last_service
        print "Enter a property name to edit it. Enter 'back' to stop editing and enter 'delete' to delete the vehicle."
        user_input = user_input_prompt(">> ")
        if user_input == "back":
            break
        if user_input == "delete":
            vehicle_list.pop(vehicleID)
            break
        if hasattr(vehicle_list[vehicleID], user_input.lower()):
            edit_property(user_input, vehicleID)
        else:
            print "Not a valid property."

def edit_property(vehicle_property, vehicleID):
    user_input = user_input_prompt("Enter new value: ")
    if vehicle_property.lower() == "brand":
        vehicle_list[vehicleID].brand = user_input.capitalize()
    elif vehicle_property.lower() == "model":
        vehicle_list[vehicleID].model = user_input.capitalize()
    elif vehicle_property.lower() == "odometer":
        vehicle_list[vehicleID].odometer = user_input
    elif vehicle_property.lower() == "last_service":
        vehicle_list[vehicleID].last_service = user_input


def save_to_file():
    file_name = user_input_prompt("Enter the name of the file: ") + ".txt"
    with open(file_name, "w") as list_file:
        list_file.write("VEHICLE LIST \n\n")
        for id, vehicle in enumerate(vehicle_list):
            list_file.write("Vehicle ID: " + str(id) + "\n")
            list_file.write("Brand: " + vehicle.brand + "\n")
            list_file.write("Model: " + vehicle.model + "\n")
            list_file.write("Odometer: " + vehicle.odometer + "\n")
            list_file.write("Last service: " + vehicle.last_service + "\n\n")
    print "Vehicle list saved to: " + file_name

