class Car(object):
    def __init__(self, model, company, color, speedlimit):
        self.model = model
        self.company = company
        self.color = color
        self.speedlimit = speedlimit

    def start(self):
        print("car started")

    def stop(self):
        print("car stopped")

    def accelerate(self):
        print("car accelerated")

    def changeGear(self):
        print("gear changed")

    def warningMessage(self,speedlimit):
        if(speedlimit>100):
            print("speed limit exceeded")

skoda = Car("superb","skoda","black","280")
skoda.start()
skoda.stop()
skoda.accelerate()