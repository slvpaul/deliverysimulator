# Object class for a self-adjusting hash table
class HashTable:

    # Constructor with capacity for the 40 packages
    # Initializes a list of size 40
    def __init__(self):
        self.capacity = 40
        self.table = [None] * self.capacity
    
    

    # Function that takes a key and data and inserts it into the bucket associated with that key
    # Or updates the data associated with that key if the key is already present in its bucket
    def insertAndUpdate(self, key, data):
        bucketId = self.getBucketId(key)
        keyDataPair = [key, data]

        if self.table[bucketId] is None:
            self.table[bucketId] = list([keyDataPair])
            return True
        else:
            for x in self.table[bucketId]:
                if x[0] == key:
                    x[1] = data
                    return True
            self.table[bucketId].append(keyDataPair)
            return True
        
    # Function prints every package stored in the hash table
    def print(self):
        i = 1
        print("Packages: ")
        while i <= 40:
            print(self.get(i))
            i += 1

     # Function that gets index of bucket
    # If bucket is not empty, loops through bucket
    # If match for key is found, removes the ith element of the bucket
    def delete(self, key):
        bucketId = self.getBucketId(key)

        if self.table[bucketId] is None:
            return False
        for i in range(0, len(self.table[bucketId])):
            if self.table[bucketId][i][0] == key:
                self.table[bucketId].pop(i)
                return True
    
    
    # Function that gets the index of the bucket associated with the key
    # If that bucket is not empty, function loops through the bucket
    # If the key is present in the bucket, function retrieves the data associated with that key
    def get(self, key):
        bucketId = self.getBucketId(key)
        if self.table[bucketId] is not None:
            for x in self.table[bucketId]:
                if x[0] == key:
                    return x[1]
        return None


    # Function that receives a key, stringifies the key and converts the key to its unicode representation
    # That number mod the capacity is equal to the index of the bucket which that key matches up to
    def getBucketId(self, key):
        bucketId = 0
        for x in str(key):
            bucketId += ord(x)
        return bucketId % self.capacity