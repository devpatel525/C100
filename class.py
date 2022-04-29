class Car(object):
    def __init__(self, model, color, company, speed_limit):
        self.color=color
        self.model=model
        self.company=company
        self.speed_limit=speed_limit

    def start(self):
        print("started")

    def stop(self):
        print("stopped")

    def accelarate(self):
        print("accelarated")

mustang=Car("v8","black","ford",240)
print(mustang.start()) 
print(mustang.stop())