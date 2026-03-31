#task 1
class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator is now at floor {self.current_floor}")
        else:
            print("Already at the top floor.")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator is now at floor {self.current_floor}")
        else:
            print("Already at the bottom floor.")

    def go_to_floor(self, target_floor):
        if target_floor < self.bottom_floor or target_floor > self.top_floor:
            print(f"Invalid floor: {target_floor}. Please stay within {self.bottom_floor}-{self.top_floor}.")
            return

        print(f"-- Moving to floor {target_floor} --")
        while self.current_floor < target_floor:
            self.floor_up()

        while self.current_floor > target_floor:
            self.floor_down()

        print(f"Reached floor {self.current_floor}\n")

if __name__ == "__main__":
    h = Elevator(0, 10)
    h.go_to_floor(5)
    h.go_to_floor(0)

#task 2
class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator is now at floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator is now at floor {self.current_floor}")

    def go_to_floor(self, target_floor):
        if target_floor < self.bottom_floor or target_floor > self.top_floor:
            return

        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()

class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, elevator_num, target_floor):
        if 0 <= (elevator_num - 1) < len(self.elevators):
            print(f"--- Calling Elevator #{elevator_num} to floor {target_floor} ---")
            selected_elevator = self.elevators[elevator_num - 1]
            selected_elevator.go_to_floor(target_floor)
        else:
            print(f"Elevator #{elevator_num} does not exist in this building.")
if __name__ == "__main__":
    grand_plaza = Building(0, 12, 3)
    grand_plaza.run_elevator(1, 7)
    grand_plaza.run_elevator(2, 10)
    grand_plaza.run_elevator(1, 0)

#Task 3
class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator is now at floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator is now at floor {self.current_floor}")

    def go_to_floor(self, target_floor):
        if target_floor < self.bottom_floor or target_floor > self.top_floor:
            return

        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()

class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, elevator_num, target_floor):
        if 0 <= (elevator_num - 1) < len(self.elevators):
            print(f"\n--- Moving Elevator #{elevator_num} to floor {target_floor} ---")
            self.elevators[elevator_num - 1].go_to_floor(target_floor)
        else:
            print(f"Elevator #{elevator_num} does not exist.")

    def fire_alarm(self):
        print("\n!!! FIRE ALARM ACTIVATED !!!")
        print("Returning all elevators to the bottom floor...")
        for i, elevator in enumerate(self.elevators, start=1):
            print(f"Evacuating Elevator #{i}:")
            elevator.go_to_floor(self.bottom_floor)
        print("All elevators are safely at the bottom floor.")
if __name__ == "__main__":
    my_building = Building(0, 15, 3)
    my_building.run_elevator(1, 12)
    my_building.run_elevator(2, 5)
    my_building.run_elevator(3, 8)
    my_building.fire_alarm()

#task 4
import random
class Car:
    """Represents a car in the race."""

    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change_of_speed):
        """Adjusts the speed of the car, staying within 0 and max_speed."""
        self.current_speed += change_of_speed
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        """Increases the travelled distance based on current speed."""
        self.travelled_distance += self.current_speed * hours


class Race:
    """Manages the race logistics and participants."""

    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        """Simulates one hour of racing for all participants."""
        for car in self.cars:
            # Change speed by a random amount between -10 and +15
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)

    def print_status(self):
        """Prints the current race standings in a formatted table."""
        header = f"| {'Reg. Number':<12} | {'Max Speed':<10} | {'Cur. Speed':<10} | {'Travelled':<12} |"
        separator = "-" * len(header)

        print(separator)
        print(header)
        print(separator)

        for car in self.cars:
            print(f"| {car.registration_number:<12} | "
                  f"{car.maximum_speed:>3} km/h    | "
                  f"{car.current_speed:>3} km/h    | "
                  f"{car.travelled_distance:>7} km   |")
        print(separator)

    def race_finished(self):
        """Checks if any car has covered the race distance."""
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False


if __name__ == "__main__":
    cars_list = []
    for i in range(1, 11):
        max_v = random.randint(100, 200)
        cars_list.append(Car(f"ABC-{i}", max_v))

    grand_derby = Race("Grand Demolition Derby", 8000, cars_list)

    hours_passed = 0

    print(f"Starting {grand_derby.name} ({grand_derby.distance} km)!")

    while not grand_derby.race_finished():
        grand_derby.hour_passes()
        hours_passed += 1
        if hours_passed % 10 == 0:
            print(f"\nSTATUS AT HOUR {hours_passed}:")
            grand_derby.print_status()

    print(f"\n--- RACE FINISHED AFTER {hours_passed} HOURS ---")
    grand_derby.print_status()