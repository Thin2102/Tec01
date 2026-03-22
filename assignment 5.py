#task 1
def main():
    numbers = []

    while True:
        user_input = input("Enter a number (or press Enter to quit): ")

        if user_input == "":
            break

        try:
            num = float(user_input)
            numbers.append(num)
        except ValueError:
            print("Invalid input. Please enter a number.")

    numbers.sort(reverse=True)

    print("\nThe five greatest numbers (descending):")
    for n in numbers[:5]:
        print(n)


if __name__ == "__main__":
    main()

#task 2
def is_prime():
    try:
        num = int(input("Enter an integer: "))

        if num < 2:
            print(f"{num} is not a prime number.")
            return

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                print(f"{num} is not a prime number.")
                break
        else:
            print(f"{num} is a prime number.")

    except ValueError:
        print("Invalid input. Please enter an integer.")


if __name__ == "__main__":
    is_prime()

#task 3
def main():
    cities=[]
    for i in range(5):
        city = input(f"enter city name {i+1}: ")
        cities.append(city)
    print("\nThe following cities are")
    for city in cities:
        print(city)
if __name__ == "__main__":
    main()

#task 3
cities = []

for i in range(5):
    city = input(f"Enter the name of city {i+1}: ")
    cities.append(city)

print("Cities entered:")
for city in cities:
    print(city)

#task 4
def sum_list(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

def main():
    nums = [5, 10, 3, 7, 2]
    result = sum_list(nums)
    print(result)

main()

#task 5
def remove_uneven(numbers):
    result = []
    for n in numbers:
        if n % 2 == 0:
            result.append(n)
    return result


def main():
    original_list = [3, 8, 5, 12, 7, 10, 1]

    new_list = remove_uneven(original_list)

    print("Original list:", original_list)
    print("List without uneven numbers:", new_list)


main()