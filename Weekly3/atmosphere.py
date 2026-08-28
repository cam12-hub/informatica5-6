def main():
    layer = input("Descent atmosphere layer: ")#.strip().title()

    if layer == "exosphere":
        print("Your altitude level will be between 700 and 10000 km")

    elif layer == "thermosphere":
        print("Your altitude level will be between 85 and 7000 km")

    elif layer == "mesosphere":
        print("Your altitude level will be between 50 and 85 km")

    elif layer == "stratosphere":
        print("Your altitude level will be between 12 and 50 km")

    elif layer == "troposphere":
        print("Your altitude level will be between 0 and 12 km")

    else:
        print("Invalid respone")

    altitude = float(input("Enter your exact altitude: "))

    if altitude == "exosphere":
    exosphere = 2
    altitude /= exosphere
        print(altitude)

    elif altitude == "thermosphere":
    thermosphere = 0.5
    altitude /= thermosphere
        print(altitude)

    elif altitude == "mesosphere":
    mesosphere = 0.2
    altitude /= mesosphere
        print(altitude)

    elif altitude == "stratosphere":
    stratosphere = 0.075
    altitude /= stratosphere
        print(altitude)

    elif altitude == "troposphere":
    troposphere = 0.02
    altitude /= troposphere
        print(altitude)

    print("Total descent time: ")

if __name__ == "__main__":
    main()
