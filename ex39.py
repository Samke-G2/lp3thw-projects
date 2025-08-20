"""
Exercise 39 - Dictionaries, oh Lovely Dictionaries
author: Samke_g2

In this exercise we learn, not only how to create dictionaries, but how to connect them s well.\
I had to modify the exercise somewhat, as the names in certain parts was based off American geography, of which I am no expert.
So the parts that required me to fill them out, I changed to South African geography
"""
# Create a mapping of provinces to abbreviation
provinces = {
    "Gauteng": "GP",
    "Limpopo": "LP",
    "Mpumalanga": "MP",
    "KwaZulu Natal": "KZN",
    "Northern Cape": "NC",
    "Eastern Cape": "EC",
    "North West": "NW",
    "Free State": "FS",
    "Western Cape": "WC"
}

# Create a basic set of states and some cities in them
cities = {
    "GP": ["Joburg", "Pretoria", "Midrand", "Springs", "Vereeniging", "Krugersdorp" ]
    "LP": ["Polokwane", "Tohoyandou"]
    "MP": ["Nelspruit/Mbombela", "Balfour", "Standerton"]
}

# Add some more cities
cities["KZN"] = ["Durban", "Ladysmith", "Newcastle"]
cities["NC"] = ["Kimberly"]
cities["EC"] = ["Matatiele", "Port Elizabeth"]
cities["NW"] = ["Suncity", "Hartebeespoort", "Potchefstroom"]
cities["FS"] = ["Bloemfontein"]
cities["WC"] = ["Cape Town"]

# Print out some cities
print('-' * 10)
print("Gauteng has: ", cities["GP"])
print(f"Mpumalanga has: {cities["MP"]}")
print("Kwazulu Natal has: ", cities[provinces["KwaZulu Natal"]] )
print(f"Limpopo has: {cities[provinces["Limpopo"]]}")

# Print out some states
print("-" * 10)
print("The Western Cape's abbreviation is:", provinces["Western Cape"])
print("North West's abbreviation is: {}".format(provinces["North West"]))

# Print every province abbreviation
print("-" * 10)
for state, abbrev in list(provinces.items()):        # look up what that last bit does
    print("{} is abbreviated {}".format(state, abbrev))

# Print every city in states
print("-" * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has these cities: {city}")

# Now do both at once:
print("-" * 10)
for province, abbrev in list(provinces.items()):
    print(f"{province} province is abbreviated {abbrev}")
    print("and has the cities: {}".format(cities[abbrev]))

print("-" * 10)
# safely get abbreviation by province that might not be there
province = provinces.get("Lesotho")

if not province:
    print("Sorry, no Lesotho")

# Get a city with a default value
city = cities.get("LS", "Does not exist")
print(f'The city for the province "Lesotho" is: {city}')
