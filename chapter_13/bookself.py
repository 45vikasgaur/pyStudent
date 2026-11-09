from random import randint
class  Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo
    
    def book(self, fro, to):
        print(f"Ticket is booked is train no: {self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"train no: {self.trainNo} is running on time")

    def getFare(self, trainNo, fro, to):
        print(f"Ticket fare in train no: {trainNo} from {fro} {to} is {randint(222, 5555)}")


t = Train(12399)
t.book("Rampur", "Delhi")
t.getStatus()
t.getFare("Rampur", "to", "Delhi")
