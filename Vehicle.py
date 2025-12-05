def calculate_distance(speed, time):
    distance = speed * time
    return distance

# Example usage:
speed = float(input("Enter speed: "))
time = float(input("Enter time: "))

result = calculate_distance(speed, time)
print("Distance traveled:", result)
