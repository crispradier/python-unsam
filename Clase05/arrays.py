import numpy as np

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a[1,3])
print(a.shape)

b=np.zeros(3)
c=np.ones(4)
print(b,c)
d=np.arange(4)
e=np.arange(4,10,1)
f=np.linspace(0, 10, num=5)

#Ejercicio 5.7: arange() y linspace()
#Generá un vector que tenga los números impares entre el 1 y el 19 inclusive usando arange(). 
# Repetí el ejercicio usando linspace(). ¿Qué diferencia hay en el resultado?

#>>> np.arange(1,20,2) 
#array([ 1,  3,  5,  7,  9, 11, 13, 15, 17, 19])

#>>> np.linspace(1, 19, num=10) 
#array([ 1.,  3.,  5.,  7.,  9., 11., 13., 15., 17., 19.])

arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
np.sort(arr) #devuelve copia ordenada

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
#los podés concatenar usado np.concatenate().
np.concatenate((a, b))
#array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])
np.concatenate((x, y), axis=0)
# array([[1, 2],
#  [3, 4],
#  [5, 6]])
array_ejemplo = np.array([[[0, 1, 2, 3], [4, 5, 6, 7]], [[0, 1, 2, 3],[4, 5, 6, 7]],[[0 ,1 ,2, 3],[4, 5, 6, 7]]])
array_ejemplo.shape
#(3, 2, 4)
b=array_ejemplo.reshape(2,4,3)
# array([[[0, 1, 2],
#         [3, 4, 5],
#         [6, 7, 0],
#         [1, 2, 3]],

#        [[4, 5, 6],
#         [7, 0, 1],
#         [2, 3, 4],
#         [5, 6, 7]]])

