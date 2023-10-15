import math
class angle:
    def init(self, x, y, z):
        self.graduses = int(x)
        self.minutes = int(y)
        self.seconds = int(z)
    def to_seconds(self):
        return self.graduses*3600 + self.minutes*60 + self.seconds
step = 1
while step != 0:
    if step == 1:
        print('START')
    print('Enter angle')
    x = input("Graduses: ")
    y = input("Minutes: ")
    z = input("Seconds: ")
    class_of_angle = angle(x, y, z)
    print("It's ", class_of_angle.to_seconds(), " secondes")
    print("  or ", class_of_angle.to_seconds()/60, " minutes")
    print("  or ", class_of_angle.to_seconds()/3600, " graduses")
    sin = round(math.sin(class_of_angle.to_seconds()/3600*math.pi/180),15)
    cos = round(math.cos(class_of_angle.to_seconds()/3600*math.pi/180),15)
    print("Sin = ", sin)
    print("Cos = ", cos)
    print("Tg = ", sin/cos)
    print("Ctg = ", cos/sin)
    tmp = int(input("Do you want to continue? Yes-1,no-0: "))
    if tmp == 0:
        step = tmp
        print("Thank you for using!")
