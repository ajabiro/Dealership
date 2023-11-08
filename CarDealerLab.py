class Vehicle:

    def __init__(self, make, miles, price):
        self.make = make
        self.miles = miles
        self.price = price
        self.engine_on = False

    def __str__(self):
        return f'{self.make} with {self.miles} miles costs ${self.price}.'

    def start_engine(self):
        print('Starting engine...')
        self.engine_on = True

    def make_noise(self):
        print("Beep beep!!")


class Truck(Vehicle):
    def __init__(self, make, miles, price):
        Vehicle.__init__(self, make, miles, price)
        self.has_cargo = False

    def load_cargo(self):
        print('Loading the truck bed')
        self.has_cargo = True


class Motorcycle(Vehicle):
    def __init__(self, make, miles, price, top_speed):
        self.top_speed = top_speed
        Vehicle.__init__(self, make, miles, price)

    def __str__(self):
        return f'{self.make} with {self.miles} miles and a top speed of {self.top_speed} costs ${self.price}.'

    def make_noise(self):
        print("Vroom vroom!!")


trucks = [Truck("Ford", 25000, 65000),
          Truck('Chevy', 50000, 25000),
          Truck('Ram', 15000, 40000)]
bikes = [Motorcycle('Harley', 0, 45000, 110),
         Motorcycle('BMW', 2000, 65000, 200),
         Motorcycle('Kawasaki', 700, 37500, 150)]

vehicles_to_compare = []


def list_vehicles(vehicles):
    for i, vehicle in enumerate(vehicles, start=1):
        print(f'{i}.{vehicle}')


def choose_vehicle(vehicles):
    while True:
        choice = int(input("Please choose a vehicle by number to compare, or 0 to choose another vehicle type: "))
        if choice == 0:
            break
        vehicles_to_compare.append(vehicles[choice - 1])
        print(f'{vehicles[choice - 1].make} added...')


def compare_vehicles(vehicles):
    for vehicle in vehicles:
        print(f'-{vehicle}')
        vehicle.make_noise()


while True:
    view = input("Would you like to view bikes or trucks? (b/t): ")
    if view == "b":
        list_vehicles(bikes)
        choose_vehicle(bikes)

    elif view == "t":
        list_vehicles(trucks)
        choose_vehicle(trucks)

    else:
        print("Enter either \"b\" or \"t\"")

    compare = input("Would you like to compare vehicles in another category? y/n: ")

    if compare != "y":
        break
if vehicles_to_compare:
    print("Here are your vehicles to compare: ")
    compare_vehicles(vehicles_to_compare)
else:
    print("Nothing to compare")
