#task 1
numbers = []

while True:
    user_input = input("Enter a number (or press Enter to quit): ")
    if user_input == "":
        break
    try:
        num = float(user_input)
        numbers.append(num)
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

numbers.sort(reverse=True)
top_five = numbers[:5]

print("\nThe five greatest numbers in descending order are:")
for n in top_five:
    print(n)

#task 2
seasons = ("winter", "spring", "summer", "autumn")

try:
    month = int(input("Enter the number of a month (1-12): "))
    if 1 <= month <= 12:
        index = (month % 12) // 3
        print(f"The season is {seasons[index]}.")
    else:
        print("Please enter a number between 1 and 12.")
except ValueError:
    print("Invalid input. Please enter an integer.")

#task 3
names_set = set()

while True:
    name = input("Enter a name (or press Enter to quit): ")
    if name == "":
        break

    if name in names_set:
        print("Existing name")
    else:
        print("New name")
        names_set.add(name)

print("\nList of all unique names entered:")
for n in names_set:
    print(n)

#task 4
def get_word_frequency(text):
    word_counts = {}
    words = text.lower().split()

    for word in words:
        word = word.strip('.,!?;:"')
        if word:
            word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts
user_text = input("Enter a sentence to analyze: ")
frequencies = get_word_frequency(user_text)

print("\nWord frequencies:")
for word, count in frequencies.items():
    print(f"{word}: {count}")

#Task 5
def remove_odd_numbers(input_list):
    return [num for num in input_list if num % 2 == 0]
original_list = [3, 14, 15, 9, 26, 5, 35, 8, 97, 100]
filtered_list = remove_odd_numbers(original_list)

print(f"Original list: {original_list}")
print(f"List with odd numbers removed: {filtered_list}")

#task 6
import random
def calculate_pi_approximation():
    try:
        N = int(input("How many random points should be generated? "))
        n = 0  

        for _ in range(N):
            x = random.uniform(-1, 1)
            y = random.uniform(-1, 1)
            if x ** 2 + y ** 2 < 1:
                n += 1
        pi_estimate = 4 * n / N
        print(f"\nAfter {N} points, the approximation of pi is: {pi_estimate}")
    except ValueError:
        print("Please enter a valid integer for the number of points.")
calculate_pi_approximation()
