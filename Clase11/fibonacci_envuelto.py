def fibonacci(n):
    """
    Toma un entero positivo n y
    devuelve el n-ésimo número de Fibonacci
    donde F(0) = 0 y F(1) = 1.
    """
    def fibonacci_aux(n, dict_fibo):
        """
        Calcula el n-ésimo número de Fibonacci de forma recursiva
        utilizando un diccionario para almacenar los valores ya computados.
        dict_fibo es un diccionario que guarda en la clave 'k' el valor de F(k)
        """
        if n in dict_fibo.keys():
            F = dict_fibo[n]
        else:
            dict_fibo[len(dict_fibo)]=dict_fibo[len(dict_fibo)-2]+dict_fibo[len(dict_fibo)-1]
            F, dict_fibo = fibonacci_aux(n, dict_fibo)
            
        return  F, dict_fibo

    dict_fibo = {0:0, 1:1} 
    F, dict_fibo = fibonacci_aux(n, dict_fibo)
    return F 

if __name__=='__main__':
    print(fibonacci(7))