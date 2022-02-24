#1
mood = input("What is your mood today? ")

if mood == "happy":
    print("It is great to see you happy!")
elif mood == "nervous":
    print("Take a deep breath 3 times.")
elif mood == "sad":
    print("Take a nap")

else:
    print("I don't recognize this mood.")

#2
secret = 10

guess = int(input ("Guess the number? "))

if guess == secret:
    print("right")
else:
    print("wrong")

#3
x = int(input("Value for x: "))

y = int(input("Value for y: "))

operation = input("Choose math operation (+, -, *, /): ")

if operation == "+":
    print(x + y)
elif operation == "-":
    print(x - y)
elif operation == "*":
    print(x * y)
elif operation == "/":
    print(x / y)
else:
    print("Error")