class Rectangle:
    def __init__(self,length,breadth,unit_cost=0):
        self.length=length
        self.breadth=breadth
        self.unit_cost=unit_cost

    def get_area(self):
         return self.length*self.breadth

    def calculate_cost(self):
        area=self.get_area()
        return area*self.unit_cost

l=int(input("Enter lenght of Rectangle:"))
b=int(input("Enter breadth of Rectangle:"))
c=int(input("Enter Cost:"))
r=Rectangle(l,b,c)
print("Area of rectangle:%s sq units"%(r.get_area()))
print("cost =%s Rs."%(r.calculate_cost()))
