class Vehicle:

    def __init__(self, propulsion_power, max_speed, civil):
        self.propulsion_power = propulsion_power
        self.max_speed = max_speed
        self.civil = civil
        self.current_speed = 0
        self.elevation = 0
        self.current_direction = 0

    def start(self, desired_speed, direction):

        def message():
            print("The vehicle is moving in direction {} degrees with a speed of {} km/h".format(direction, self.current_speed, self.elevation))
        if desired_speed > self.max_speed:
            raise ValueError("Desired speed exeeds maximum speed")
        else:
            self.current_speed = desired_speed
            self.current_direction = direction
            message()
            return self.current_direction, self.current_speed, self.elevation

    def stop(self):
        self.current_speed = 0
        self.elevation = 0
        print("The vehicle has been stopped. Current speed: {} km/h".format(self.current_speed))
        return self.current_speed


class Train(Vehicle):

    def __init__(self, propulsion_power, max_speed, civil, quantity_of_carriages):
        super().__init__(propulsion_power, max_speed, civil)
        self.quantity_of_carriage = quantity_of_carriages

    def separate(self, carriages_to_separate):
        if carriages_to_separate <= self.quantity_of_carriage:
            self.quantity_of_carriage -= carriages_to_separate
            print("{} carriages have been separated from the train and now it consists of {} carriages only".format(carriages_to_separate, self.quantity_of_carriage))
            return self.quantity_of_carriage
        else:
            raise ValueError("Total amount of carriages is less than you want to separate")


class Airplane(Vehicle):

    def __init__(self, propulsion_power, max_speed, civil, fuel_tank_vol):
        super().__init__(propulsion_power, max_speed, civil)
        self.fuel_tank_vol = fuel_tank_vol

    def elevation_up(self, meters):
        self.elevation += meters
        print("The elevation has been increased by {} m and now you are in {} m above the water level".format(meters, self.elevation))
        return self.elevation

    def elevation_down(self, meters):
        self.elevation -= meters
        print("The vehicle's elevation has been reduced by {} m and now you are in {} m above the water level".format(meters, self.elevation))
        return self.elevation

    def takeoff(self, desired_speed, direction, meters_to_raise):
        super().start(desired_speed=desired_speed, direction=direction)
        self.elevation_up(meters_to_raise)
        return None


volvo = Train(propulsion_power="Solar", max_speed=200, civil=True, quantity_of_carriages=25)
bmw = Airplane(propulsion_power="Fuel Engine", max_speed=900, civil=True, fuel_tank_vol=400)

volvo.start(desired_speed=80, direction=140)
bmw.takeoff(desired_speed=250, direction=30, meters_to_raise=150)

print(bmw.fuel_tank_vol)
print(bmw.elevation_up(meters=300))
print(volvo.separate(2))

volvo.stop()
bmw.stop()
