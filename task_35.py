class Vehicle:
    current_speed = 0
    elevation = 0

    def __init__(self, propulsion_power, max_speed, civil):
        self.propulsion_power = propulsion_power
        self.max_speed = max_speed
        self.civil = civil

    def start(self, desired_speed, direction):

        def message():
            print("The vehicle is moving in direction {} degrees with a speed of {}km/h with elevation of {}m above the water".format(direction, self.current_speed, self.elevation))
        if desired_speed > self.max_speed:
            error = "Desired speed exeeds maximum speed"
            return error
        else:
            self.current_speed = desired_speed
            message()
            return direction, self.current_speed, self.elevation

    def stop(self):
        print("The vehicle has been stopped")
        self.current_speed = 0
        return self.current_speed


class Train(Vehicle):

    def __init__(self, propulsion_power, max_speed, civil, quontity_of_carriages):
        Vehicle.__init__(self, propulsion_power, max_speed, civil)
        self.quontity_of_carriage = quontity_of_carriages

    def separate(self, carriages_to_separate):
        if carriages_to_separate <= self.quontity_of_carriage:
            self.quontity_of_carriage -= carriages_to_separate
            return self.quontity_of_carriage
        else:
            error = "Total amount of carrieges is less than you want to separate"
            return error


class Airplane(Vehicle):

    def __init__(self, propulsion_power, max_speed, civil, fuel_tank_vol):
        Vehicle.__init__(self, propulsion_power, max_speed, civil)
        self.fuel_tank_vol = fuel_tank_vol

    def elevation_up(self):
        self.elevation += 100
        return self.elevation

    def start(self, desired_speed, direction):
        self.elevation_up()
        return Vehicle.start(self=self, desired_speed=desired_speed, direction=direction)


volvo = Train("Solar", 30, True, 4)
bmw = Airplane("Fuel", 900, True, 1300)

volvo.start(10, 120)
print(bmw.fuel_tank_vol)
print(bmw.elevation_up())
print(volvo.separate(2))
bmw.start(300, 99)
