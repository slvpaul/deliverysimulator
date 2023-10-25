from distances import distances
from package import Package
from hashtable import HashTable
import csv
from datetime import timedelta, datetime

# This function creates an instance of the hash table class
# Then reads the data from packages.csv and loops through
# the packages creating a new instance of the package class at each stop
# while also inserting the packages into the hash table
def loadPackageData(file):
        h = HashTable()
        with open(file) as packages:
            packageData = csv.reader(packages, delimiter=',')
            next(packageData)
            for package in packageData:
                packageID = int(package[0])
                packageDestination = package[1]
                packageCity = package[2]
                packageState = package[3]
                packageZip = package[4]
                packageDeadline = package[5]
                packageWeight = package[6]
                packageNotes = package[7]
                packageStatus = "at hub"

                p = Package(packageID, packageDestination, packageCity, packageState, packageZip, packageDeadline, packageWeight, packageNotes, packageStatus)

                h.insertAndUpdate(packageID, p)

        return h

# By running the loadPackageData function with the csv file as input
# a new hash table is created with data from all 40 packages
packageHashTable = loadPackageData('./packages.csv')

# The addTime function is used to add the time elapsed during
# delivery to the current time
def addTime(x, y):
    time = datetime(2000, 1, 1, x.hour, x.minute, x.second)
    time = time + timedelta(seconds = y)
    return time.time()

# A Truck class is defined including the following attributes: a list containing the packages it carries,
# a list containing the routes it must take, the current time, the time when the truck has finished deliveries,
# the speed per minute, the miles the truck travels, the total miles it traveled at the end of deliveries,
# and the current location of the truck
# Its methods include: load, where the packages and their destinations are appended to separate lists
# Unload, where the packages and their destinations are removed as deliveries take place
# routeComplete, which runs when the truck is empy to record the time and total miles 
class Truck:

    def __init__(self):
        self.packages = []
        self.route = []
        self.curTime = None
        self.endTime = None
        self.speed = 0.3
        self.miles = 0.0
        self.endMiles = 0.0
        self.curLoc = '4001 South 700 East'

    def load(self, package):
        self.packages.append(package)
        self.route.append(package.destination)
        package.status = "en route"
        packageHashTable.insertAndUpdate(package.id, package)

    def unload(self, package):
        self.packages.remove(package)
        self.route.remove(package.destination)

    def routeComplete(self, time, miles):
        self.endTime = time
        self.endMiles = miles

    # Self-adjusting nearest neighbor algorithm
    # The algorithm sets a current minimum to the maximum
    # distance to another node from the current location
    # Then it loops through those nodes, finding the intersection
    # between the total set of all locations and those that
    # have been loaded in the truck as routes
    # Through successive comparisons the nearest location
    # to the current location is found and its key is removed
    # from the route list and reinserted at the start of the list
    # The algorithm is called again after every package is delivered
    # and the current location is updated.
    # Its time complexity is O(n^2)
    # Its space complexity is O(1)
    def optimize(self):
        xMin = 0
        curMin = max(distances[self.curLoc].values())
        for x in distances[self.curLoc].keys():
            if x in self.route:
                xMin = distances[self.curLoc][x]
                if xMin < curMin:
                    curMin = xMin
                    minKey = x
        self.route.remove(minKey)
        self.route.insert(0,minKey)

    # The deliver algorithm handles the delivery of the packages
    # as well as the updates of the packages data in the hash table
    # It receives a time parameter which sets the time at which the
    # truck leaves the depot and an option upTo parameter which simulates
    # the deliveries up to a particular time
    def deliver(self, time, upTo = None):
        secs = 0
        self.curTime = time
        # Call the optimize function for the first time        
        self.optimize()
        # The delivery while loop runs while the route list is not empty
        # It begins by looping through the keys in the nested distances dictionary
        # with the hub as the starting location
        # Whenever the key in the dictionary matches the optimized, first route
        # in the route list, we loop through the truck's packages list
        # saving the distance traveled, incrementing the total miles,
        # setting the time elapsed, and adding the time elapsed to the current time
        # Then we check if there is an up to time limit and if so end the delivery
        # In addition, we perform conditional checks that will set the status
        # of packages which only become "en route" later in the day
        # Finally, we update the status of the package, insert it into the hash table
        # and delete the package from the truck
        # If the truck is empty, the program is ended and final miles and time are tallied
        # If not, the current location is updated and the optimize algorithm is run again to
        # find the nearest neighbor
        # The delivery algorithm has a time complexity of O(n^2) as it requires a loop through of n distances n times
        # Its space complexity O(n) as the largest single source of memory usage is the n amount of packages to be delivered
        while self.route:
            for y in distances[self.curLoc].keys():
                  if y == self.route[0]:
                    for x in self.packages:
                        if x.destination == self.route[0]:
                            curDistance = distances[self.curLoc][y]
                            self.miles += distances[self.curLoc][y]
                            secs = round((curDistance / self.speed) * 60)
                            deliv = addTime(self.curTime, secs)
                            self.curTime = datetime(2000, 1, 1, deliv.hour, deliv.minute, deliv.second)
                            if upTo != None and self.curTime > upTo:
                                return True
                            x.status = "delivered at " + str(self.curTime.strftime("%H:%M:%S"))
                            packageHashTable.insertAndUpdate(x.id, x)
                            self.unload(x)
                            if not self.route:
                                self.routeComplete(self.curTime, self.miles)
                                return True
                            self.curLoc = y
                            self.optimize()
                            break