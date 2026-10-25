class BMW:
    def fuel_type(self):
        print("BMW uses petrol")
    def max_speed(self):
        print("BMW max speed is 280 km/h")
class Ferrari:
    def fuel_type(self):
        print("Ferrari uses petrol")
    def max_speed(self):
        print("Ferrari max speed is 360 km/h")
cars = [BMW(), Ferrari()]
for car in cars:
    car.fuel_type()
    car.max_speed()