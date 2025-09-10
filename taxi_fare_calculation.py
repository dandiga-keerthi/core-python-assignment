BASE_FARE = 50
DISTANCE_FARE = 10
def calculate_fare(distance):
    return BASE_FARE + DISTANCE_FARE * distance
trips = list(map(int, input("Enter trip distances (space separated): ").split()))
total = 0
for i, d in enumerate(trips, 1):
    fare = calculate_fare(d)
    total += fare
    print(f"Trip {i}: ${fare}")
print(f"Total Fare: ${total}")
