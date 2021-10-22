class Camion:

    def __init__(self, lotes):
        self.lotes = lotes
        self.size = len(lotes)
    
    def __iter__(self):
        return self.lotes.__iter__()

    def __contains__(self, nombre):
        return any([lote.nombre == nombre for lote in self.lotes])

    def __len__(self):
        return self.size
        
    def __getitem__(self,ii):
        return self.lotes.__getitem__(ii)     

    def __repr__(self):
        lotes = [l for l in self.lotes]
        return f'Camion({lotes})'
    
    def __str__(self):
        string=f'Camion con {len(self.lotes)} lotes:\n'
        for lote in self.lotes:
            string=string+'Lote de '+str(lote.cajones)+' cajones de '+ lote.nombre+', pagados a $'+str(lote.precio)+' cada uno.\n'
        return string

    def precio_total(self):
        return sum(l.costo() for l in self.lotes)

    def contar_cajones(self):
        from collections import Counter
        cantidad_total = Counter()
        for l in self.lotes:
            cantidad_total[l.nombre] += l.cajones
        return cantidad_total