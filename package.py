class Package:

    def __init__(self, id, destination, city, state, zip, deadline, weight, notes, status):
        self.id = id
        self.destination = destination
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.status = status

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.id, self.destination, self.city, self.state, self.zip, self.deadline, self.weight, self.notes, self.status)
