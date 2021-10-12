class Punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'Punto({self.x}, {self.y})'

    def __add__(self, b):
      return Punto(self.x + b.x, self.y + b.y)

class Rectangulo():
    def __init__(self, a,b):
        self.ax=a.x
        self.ay=a.y
        self.bx=b.x
        self.by=b.y
    
    def base(self):
        return abs(self.ax-self.bx)
    
    def altura(self):
        return abs(self.ay-self.by)
    
    def area(self):
        return self.altura()*self.base()
    
    def desplazar(self,desplazamiento):
        self.ax+=desplazamiento.x
        self.ay+=desplazamiento.y
        self.bx+=desplazamiento.x
        self.by+=desplazamiento.y
    
    def rotar(self):
        lr=Punto(max(self.ax,self.bx),min(self.ay,self.by))
        h=self.altura()
        b=self.base()
        self.ax=lr.x
        self.ay=lr.y
        self.bx=self.ax+h
        self.by=self.ay+b
        
    def __str__(self):
        return f'({self.ax},{self.ay}), ({self.bx},{self.by})'

    def __repr__(self):
        return f'Rectangulo(Punto({self.ax}, {self.ay}), Punto({self.bx}, {self.by}))'