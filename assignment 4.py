#task 1

import re
def is_valid_course_code(code):
    pattern = r'^[A-Z]{3}\d{3}$'
    return bool(re.match(pattern, code))


if __name__ == "__main__":
    user_input = input("Enter course code: ")

    if is_valid_course_code(user_input):
        print("True ")
    else:
        print("False ")

#task 2
import re
def is_valid_hex_color(color):

    pattern = r'^#[0-9A-Fa-f]{6}$'
    return bool(re.match(pattern, color))
if __name__ == "__main__":
    user_input = input("Enter hex color: ")

    if is_valid_hex_color(user_input):
        print("Valid hex color ")
    else:
        print("Invalid hex color ")

#task 3
def analyze_numbers(text):
    # Find all full numbers
    numbers = re.findall(r'\d+', text)

    # Sum of full numbers
    sum_full_numbers = sum(int(num) for num in numbers)

    # Sum of individual digits
    sum_digits = sum(int(digit) for digit in ''.join(numbers))

    return sum_full_numbers, sum_digits
if __name__ == "__main__":
    user_input = input("Enter a paragraph: ")

    total_numbers, total_digits = analyze_numbers(user_input)

    print("Sum of full numbers:", total_numbers)
    print("Sum of all digits:", total_digits)

#task 4
import re
def redact_phone_numbers(text):
    pattern = r'(\b\d{10}\b|\+84\d+)'
    return re.sub(pattern, "[REDACTED]", text)
if __name__ == "__main__":
    user_input = input("Enter text: ")
    result = redact_phone_numbers(user_input)
    print("After redaction:")
    print(result)