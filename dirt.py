def distance():
    rate = float(input("Enter the rate:"))
    time = float(input("Enter the time:"))
    result = str(rate*time)
    print("The distance is " + result)

def time():
    distance = float(input("Enter the distance: "))
    rate = float(input("Enter the rate: "))
    result = str(distance/rate)
    print("The time is " + result)

def rate():
    distance = float(input("Enter the distance: "))
    time = float(input("Enter the time: "))
    result = str(distance/time)
    print("The rate is " + result)

def main():
    which_one = (input("What do you want to calculate? \n"))
    if which_one.upper() == "DISTANCE":
        distance()
    if which_one.upper() == "TIME":
        time()
    if which_one.upper() == "RATE":
        rate()

main()