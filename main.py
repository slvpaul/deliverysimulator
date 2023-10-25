from truck import Truck
from truck import packageHashTable
from datetime import datetime

class Main:

    # Boolean variable for command-line interface
    cli = True
    
    # Create three different instances of the Truck class
    truck1 = Truck()
    truck2 = Truck()
    truck3 = Truck()

    # Create datetime objects which are used to set the start time for all three trucks
    # Truck2 leaves at 9:05 with the packages that have that constraint
    # Truck3 leaves after Truck1 arrives
    startTime1 = datetime(2000, 1, 1, 8, 0, 0)
    startTime2 = datetime(2000, 1, 1, 9, 5, 0)
    startTime3 = datetime(2000, 1, 1, 9, 33, 0)

    # Command-line interface with three options
    # First option loads the trucks and calls the deliver method of the truck class for each instance
    # Prints the time that all packages are delivered
    # Prints the total amount of miles traveled by all three trucks
    # And calls the print method of the hash table class that prints the details of every delivered package
    #
    # Second option accepts the user's input to create a new datetime object 
    # that represents the time to look up the status of the packages
    # Then the packages are loaded, the deliver method is called and the attributes of all the packages are printed
    #
    # Fourth option ends the program
    while cli:
        print("\nEnter 1 to deliver all packages")
        print("Enter 2 to look up all package statuses at a specific time")
        print("Enter 3 to look up a single package")
        print("Enter anything else to end the program\n")
        
        x = input()

        if x == str(1):
            truck1.load(packageHashTable.get(15))
            truck1.load(packageHashTable.get(16))
            truck1.load(packageHashTable.get(34))
            truck1.load(packageHashTable.get(14))
            truck1.load(packageHashTable.get(20))
            truck1.load(packageHashTable.get(40))
            truck1.load(packageHashTable.get(31))
            truck1.load(packageHashTable.get(13))
            truck1.load(packageHashTable.get(37))
            truck1.load(packageHashTable.get(30))
            truck1.load(packageHashTable.get(1))
            truck1.load(packageHashTable.get(29))
            truck1.load(packageHashTable.get(19))
            truck1.deliver(startTime1)
            truck2.load(packageHashTable.get(25))
            truck2.load(packageHashTable.get(6))
            truck2.load(packageHashTable.get(3))
            truck2.load(packageHashTable.get(2))
            truck2.load(packageHashTable.get(17))
            truck2.load(packageHashTable.get(4))
            truck2.load(packageHashTable.get(5))
            truck2.load(packageHashTable.get(18))
            truck2.load(packageHashTable.get(28))
            truck2.load(packageHashTable.get(32))
            truck2.load(packageHashTable.get(36))
            truck2.load(packageHashTable.get(38))
            truck2.load(packageHashTable.get(26))
            truck2.load(packageHashTable.get(27))
            truck2.load(packageHashTable.get(33))
            truck2.load(packageHashTable.get(35))
            truck2.deliver(startTime2)
            truck3.load(packageHashTable.get(7))
            truck3.load(packageHashTable.get(8))
            truck3.load(packageHashTable.get(9))
            truck3.load(packageHashTable.get(10))
            truck3.load(packageHashTable.get(11))
            truck3.load(packageHashTable.get(12))
            truck3.load(packageHashTable.get(21))
            truck3.load(packageHashTable.get(22))
            truck3.load(packageHashTable.get(23))
            truck3.load(packageHashTable.get(24))
            truck3.load(packageHashTable.get(39))
            truck3.deliver(startTime3)
            totalMiles = truck1.endMiles + truck2.endMiles + truck3.endMiles
            print("\nAll packages delivered by " + truck3.endTime.strftime("%H:%M:%S"))
            print(str(round(totalMiles, 1)) + " total miles traveled")
            packageHashTable.print()
            break
        
        elif x == str(2):
            print("Input the hour and minute you want to look up (24hr time)")
            hour = int(input())
            minute = int(input())
            upto = datetime(2000, 1, 1, hour, minute, 0)
            truck1.load(packageHashTable.get(15))
            truck1.load(packageHashTable.get(16))
            truck1.load(packageHashTable.get(34))
            truck1.load(packageHashTable.get(14))
            truck1.load(packageHashTable.get(20))
            truck1.load(packageHashTable.get(40))
            truck1.load(packageHashTable.get(31))
            truck1.load(packageHashTable.get(13))
            truck1.load(packageHashTable.get(37))
            truck1.load(packageHashTable.get(30))
            truck1.load(packageHashTable.get(1))
            truck1.load(packageHashTable.get(29))
            truck1.load(packageHashTable.get(19))
            truck1.deliver(startTime1, upto)
            truck2.load(packageHashTable.get(25))
            truck2.load(packageHashTable.get(6))
            truck2.load(packageHashTable.get(3))
            truck2.load(packageHashTable.get(2))
            truck2.load(packageHashTable.get(17))
            truck2.load(packageHashTable.get(4))
            truck2.load(packageHashTable.get(5))
            truck2.load(packageHashTable.get(18))
            truck2.load(packageHashTable.get(28))
            truck2.load(packageHashTable.get(32))
            truck2.load(packageHashTable.get(36))
            truck2.load(packageHashTable.get(38))
            truck2.load(packageHashTable.get(26))
            truck2.load(packageHashTable.get(27))
            truck2.load(packageHashTable.get(33))
            truck2.load(packageHashTable.get(35))
            truck2.deliver(startTime2, upto)
            truck3.load(packageHashTable.get(7))
            truck3.load(packageHashTable.get(8))
            truck3.load(packageHashTable.get(9))
            truck3.load(packageHashTable.get(10))
            truck3.load(packageHashTable.get(11))
            truck3.load(packageHashTable.get(12))
            truck3.load(packageHashTable.get(21))
            truck3.load(packageHashTable.get(22))
            truck3.load(packageHashTable.get(23))
            truck3.load(packageHashTable.get(24))
            truck3.load(packageHashTable.get(39))
            truck3.deliver(startTime3, upto)
            packageHashTable.print()
            break
        
        elif x == str(3):
            
            print("Input the hour and minute you want to look up (24hr time)")
            print("Then enter the ID of a package")
            hour = int(input())
            minute = int(input())
            id = int(input())
            upto = datetime(2000, 1, 1, hour, minute, 0)
            truck1.load(packageHashTable.get(15))
            truck1.load(packageHashTable.get(16))
            truck1.load(packageHashTable.get(34))
            truck1.load(packageHashTable.get(14))
            truck1.load(packageHashTable.get(20))
            truck1.load(packageHashTable.get(40))
            truck1.load(packageHashTable.get(31))
            truck1.load(packageHashTable.get(13))
            truck1.load(packageHashTable.get(37))
            truck1.load(packageHashTable.get(30))
            truck1.load(packageHashTable.get(1))
            truck1.load(packageHashTable.get(29))
            truck1.load(packageHashTable.get(19))
            truck1.deliver(startTime1, upto)
            truck2.load(packageHashTable.get(25))
            truck2.load(packageHashTable.get(6))
            truck2.load(packageHashTable.get(3))
            truck2.load(packageHashTable.get(2))
            truck2.load(packageHashTable.get(17))
            truck2.load(packageHashTable.get(4))
            truck2.load(packageHashTable.get(5))
            truck2.load(packageHashTable.get(18))
            truck2.load(packageHashTable.get(28))
            truck2.load(packageHashTable.get(32))
            truck2.load(packageHashTable.get(36))
            truck2.load(packageHashTable.get(38))
            truck2.load(packageHashTable.get(26))
            truck2.load(packageHashTable.get(27))
            truck2.load(packageHashTable.get(33))
            truck2.load(packageHashTable.get(35))
            truck2.deliver(startTime2, upto)
            truck3.load(packageHashTable.get(7))
            truck3.load(packageHashTable.get(8))
            truck3.load(packageHashTable.get(9))
            truck3.load(packageHashTable.get(10))
            truck3.load(packageHashTable.get(11))
            truck3.load(packageHashTable.get(12))
            truck3.load(packageHashTable.get(21))
            truck3.load(packageHashTable.get(22))
            truck3.load(packageHashTable.get(23))
            truck3.load(packageHashTable.get(24))
            truck3.load(packageHashTable.get(39))
            truck3.deliver(startTime3, upto)
            print(packageHashTable.get(id))
            break



        else:
            cli = False