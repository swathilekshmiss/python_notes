
bus = {
    "bus_no": 101,
    "name": "Super Fast",
    "source": "Kollam",
    "destination": "Kochi",
    "price": 150,
    "seats": 20
}
{
"bus_no": 102,
"name": "Express",
"source": "Kollam",
"destination": "Trivandrum",
"price": 100,
"seats": 15
}
}
print("Bus Ticket Booking")

name = input("Enter your name: ")
source = input("Enter source: ")
destination = input("Enter destination: ")

print("\nBus Details")
print("Bus No:", bus["bus_no"])
print("Bus Name:", bus["name"])
print("From:", bus["source"])
print("To:", bus["destination"])
print("Price:", bus["price"])
print("Available Seats:", bus["seats"])

seat = int(input("\nHow many seats do you want? "))

if seat <= bus["seats"]:
    total = seat * bus["price"]
    bus["seats"] = bus["seats"] - seat

    print("\nBooking Successful!")
    print("Passenger:", name)
    print("Seats:", seat)
    print("Total Amount:", total)
    print("Remaining Seats:", bus["seats"])

else:
    print("Sorry, seats are not available.")