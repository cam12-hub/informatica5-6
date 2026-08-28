def main():
    layer = input("Descent atmosphere layer: ").strip().lower()
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

    #time = 0
    #if altitude > 700:        Right way to do the test
        #time += (Altutide - 700) / 2
        #altitude = 700
    #if altitude > 85:
        #time += (Altutide - 85) / 0.5
        #altitude = 85
    #if altitude > 50:
        #time += (Altutide - 50) / 0.2
        #altitude = 50
    #if altitude > 12:    
            #time += (Altutide - 12) / 0.075
            #altitude = 12

    #time += altitude / 0.02
    #print("Total time:", round(time,2))



    if layer == "exosphere":
    exosphere = 2
    altitude /= exosphere
        print(altitude)

    elif layer == "thermosphere":
    thermosphere = 0.5
    altitude /= thermosphere
        print(altitude)

    elif layer == "mesosphere":
    mesosphere = 0.2
    altitude /= mesosphere
        print(altitude)

    elif layer == "stratosphere":
    stratosphere = 0.075
    altitude /= stratosphere
        print(altitude)

    elif layer == "troposphere":
    troposphere = 0.02
    altitude /= troposphere
        print(altitude)

    print("Total descent time: ")

if __name__ == "__main__":
    main()
