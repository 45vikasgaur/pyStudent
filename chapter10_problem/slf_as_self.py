from random import randint
class  Train:
    def __init__(slf, trainNo):
        slf.trainNo = trainNo
    
    def book(slf, fro, to):
        print(f"Ticket is booked is train no: {slf.trainNo} from {fro} to {to}")

    def getStatus(slf):
        print(f"train no: {slf.trainNo} is running on time")

    def getFare(slf, trainNo, fro, to):
        print(f"Ticket fare in train no: {trainNo} from {fro} {to} is {randint(222, 5555)}")


t = Train(12399)
t.book("Rampur", "Delhi")
t.getStatus()
t.getFare("Rampur", "to", "Delhi")
 