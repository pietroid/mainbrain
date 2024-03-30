class Brain:
    def __init__(self, units, receiver, connections):
        self.units = units
        self.receiver = receiver
        for connection in connections:
            connection[0].connect(connection[1])