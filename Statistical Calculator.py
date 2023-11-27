import math

def calculate_mean(numbers):
    return round(sum(numbers) / len(numbers), 2)

def calculate_stddev(numbers):
    mean = calculate_mean(numbers)
    squared_diff = [(x - mean) ** 2 for x in numbers]
    variance = sum(squared_diff) / len(numbers)
    stddev = round(math.sqrt(variance), 2)
    return stddev

def get_numbers():
    try:
        num_list = [float(x) for x in input("Enter five numbers: ").split()]
        if len(num_list) == 5:
            return num_list
        else:
            print("Please enter exactly five numbers.")
            return get_numbers()
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return get_numbers()

while True:
    numbers = get_numbers()
    mean = calculate_mean(numbers)
    stddev = calculate_stddev(numbers)

    print(f"The mean of the numbers is: {mean}")
    print(f"The standard deviation of the numbers is: {stddev}")

    repeat = input("Enter 'Yes' to do another calculation, or 'No' to quit: ")
    if repeat.lower() != 'yes':
        break