#task 1
class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

if __name__ == "__main__":
    new_car = Car("ABC-123", 142)

    print("Registration Number:", new_car.registration_number)
    print("Maximum Speed:      ", new_car.max_speed, "km/h")
    print("Current Speed:      ", new_car.current_speed, "km/h")
    print("Travelled Distance: ", new_car.travelled_distance, "km")

#task 2
class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        self.current_speed += speed_change

        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

        if self.current_speed < 0:
            self.current_speed = 0


if __name__ == "__main__":
    new_car = Car("ABC-123", 142)

    new_car.accelerate(30)
    new_car.accelerate(70)
    new_car.accelerate(50)

    print("Current speed after acceleration:", new_car.current_speed, "km/h")

    new_car.accelerate(-200)

    print("Final speed after emergency brake:", new_car.current_speed, "km/h")

#task 3
class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        self.current_speed += speed_change

        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        distance_covered = self.current_speed * hours
        self.travelled_distance += distance_covered


if __name__ == "__main__":
    new_car = Car("ABC-123", 142)

    new_car.travelled_distance = 2000
    new_car.accelerate(60)

    new_car.drive(1.5)

    print("Car Registration:  ", new_car.registration_number)
    print("Final Speed:       ", new_car.current_speed, "km/h")
    print("Travelled Distance:", new_car.travelled_distance, "km")

#task 4
import random

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

cars = []
for i in range(1, 11):
    cars.append(Car(f"ABC-{i}", random.randint(150, 200)))

race_on = True
while race_on:
    for car in cars:
        car.accelerate(random.randint(-10, 15))
        car.drive(1)
        if car.travelled_distance >= 10000:
            race_on = False

print(f"{'Reg. Num':<10} | {'Max Speed':<12} | {'Cur. Speed':<12} | {'Distance':<12}")
print("-" * 55)
for car in cars:
    print(f"{car.registration_number:<10} | {car.max_speed:<12} | {car.current_speed:<12} | {car.travelled_distance:<12.1f}")