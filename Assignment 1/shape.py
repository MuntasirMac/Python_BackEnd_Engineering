class Shape:
    def __init__(self, name='Default', height=0, base=0):
        self.area = 0
        self.name = name
        self.height = height
        self.base = base
    def get_height_base(self):
        return "Height: "+str(self.height)+", Base: "+str(self.base)

class triangle(Shape):
    def __init__(self, name='Default', height=0, base=0):
        Shape.__init__(self, name, height, base)

    def calcArea(self):
        return 0.5*self.height*self.base
    
    def printDetail(self):
        print("Shape name:"+str(self.name))
        print(self.get_height_base())
        print("Area:"+str(self.calcArea()))

class trapezoid(Shape):
    def __init__(self, name='Default', height=0, base=0,side_a=0):
        Shape.__init__(self, name, height, base)
        self.side_a = side_a

    def get_height_base(self):
        return "Height: "+str(self.height)+", Base: "+str(self.base)+", Side_A: "+str(self.side_a)

    def calcArea(self):
        return 0.5*self.height*(self.base+self.side_a)

    def printDetail(self):
        print("Shape name:"+str(self.name))
        print(self.get_height_base())
        print("Area:"+str(self.calcArea()))

tri_default = triangle()
tri_default.calcArea()
tri_default.printDetail()
print('--------------------------')
tri = triangle('Triangle', 10, 5)
tri.calcArea()
tri.printDetail()
print('---------------------------')
trap = trapezoid('Trapezoid', 10, 6, 4)
trap.calcArea()
trap.printDetail()