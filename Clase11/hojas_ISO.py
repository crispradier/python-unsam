def medidas_hoja_A(N):
    if N==0:
        a=841
        l=1189
    else:
        ancho,largo=medidas_hoja_A(N-1)
        l=ancho
        a=largo//2
    return a,l

if __name__=='__main__':
    print(medidas_hoja_A(4))
