class Libro():
    def __init__(self,prestamo, devolucion, dame_info=None):
        self.prestamo=prestamo
        self.devolucion=devolucion
        if dame_info is not None:
            self.dame_info=dame_info
        else:
            self.dame_info='no hay más información'
    def dia_prestamo(self):
        return self.prestamo
    def dia_devolucion(self):
        return self.devolucion


after=Libro('14 febrero', '15 abril','4 ejemplares disponibles')
print('nombre del libro: After')
print('Dia de présatmao: ',after.dia_prestamo())
print('Dia de devolución: ',after.dia_devolucion())
print('Más información: ', after.dame_info)
    
