# Creá un archivo llamado lote.py y adentro definí una clase llamada Lote que 
# represente un lote de cajones de una misma fruta. Definila de modo que cada
#  instancia de la clase Lote (es decir, cada objeto lote) tenga los atributos
#  nombre, cajones, y precio. Éste es un ejemplo del comportamiento buscado:

class Lote:
    def __init__(self, nombre, cajones, precio):
        self.nombre=nombre
        self.cajones=cajones
        self.precio=precio
    
    def __repr__(self):
        return f"Lote('{self.nombre}', {self.cajones}, {self.precio})"

    def costo(self):
        return self.cajones*self.precio

    def vender(self,n):
        self.cajones-=n