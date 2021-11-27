#1. Create a greeting for your program.

#2. Ask the user for the city that they grew up in.

#3. Ask the user for the name of a pet.

#4. Combine the name of their city and pet and show them their band name.

#5. Make sure the input cursor shows on a new line, see the example at:
#   https://replit.com/@appbrewery/band-name-generator-end

def name_generator():
    print("Hello and welcome to the amazing bandname-generator!")
    city = input("Please tell me the city you grew up in:\n")
    pet = input("Please tell me the name of your pet:\n")
    bandname = city + pet
    return bandname

print("Congratulations! You should name your band", name_generator())