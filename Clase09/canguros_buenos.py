class Canguro():
    def __init__(self, nombre, lista=None):
        self.nombre=nombre
        if lista is None: 
            self.contenido_marsupio = []
        else:
            self.contenido_marsupio=lista

    def meter_en_marsupio(self,objeto):
        self.contenido_marsupio.append(objeto)

    def __str__(self):
        return f'{self.nombre} tiene en su marsupio {self.contenido_marsupio}'

if __name__=='__main__':
    cangurito=Canguro('Rito')
    madre_canguro=Canguro('Cangu', ['miel','guantes'])
    madre_canguro.meter_en_marsupio(cangurito)
    madre_canguro.meter_en_marsupio('bufanda')


# #%%
# # canguro_malo.py
# """Este código continene un 
# bug importante y dificil de ver
# """

# class Canguro:
#     """Un Canguro es un marsupial."""

#     def __init__(self, nombre, contenido=None):
#         """Inicializar los contenidos del marsupio.

#         nombre: string
#         contenido: contenido inicial del marsupio, lista.
#         """
#         self.nombre = nombre
#         if contenido is None: 
#             #acá estaba el problema, usaba la misma lista para todas las instancias d ela clase
#             self.contenido_marsupio = []
#         else:
#             self.contenido_marsupio=contenido

#     def __str__(self):
#         """devuelve una representación como cadena de este Canguro.
#         """
#         t = [ self.nombre + ' tiene en su marsupio:' ]
#         for obj in self.contenido_marsupio:
#             s = '    ' + object.__str__(obj)
#             t.append(s)
#         return '\n'.join(t)

#     def meter_en_marsupio(self, item):
#         """Agrega un nuevo item al marsupio.

#         item: objecto a ser agregado
#         """
#         self.contenido_marsupio.append(item)


# madre_canguro = Canguro('Madre')
# cangurito = Canguro('gurito')
# madre_canguro.meter_en_marsupio('billetera')
# madre_canguro.meter_en_marsupio('llaves del auto')
# madre_canguro.meter_en_marsupio(cangurito)

# print(madre_canguro)
# print(cangurito)

# # Al ejecutar este código todo parece funcionar correctamente.
# # Para ver el problema, imprimí el contenido de cangurito.
