# ile converter

print("Hello! This is a unit converter that converts kilometers into miles.")

while True:
    print("Please enter a number of kilometers that you'd like to convert into miles.")

    km = input("Kilometers: ")

    km = float(km.replace(",", "."))  # replace comma with dot, if user entered a comma

    miles = km * 0.621371

    print("{0} kilometers is {1} miles.".format(km, miles))

    choice = input("Would you like to do another conversion (y/n): ")

    if choice.lower() != "y" and choice.lower() != "yes":
        break


#1 FizzBuzz


x = int(input("Enter a number between 1 and 100: "))

for x in range(1, x+1):
    if x % 3 == 0 and x % 5 == 0:
        print("fizzbuzz")
    elif x % 3 == 0:
        print("fizz")
    elif x % 5 == 0:
        print("buzz")
    else:
        print(x)

# Make string lowercase

str = "Today Is A BeautiFul DAY"
print(str.lower())
