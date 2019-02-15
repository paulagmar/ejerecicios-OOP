class empleado():
    def __init__(self,nombre,edad,genero,sueldo):
        self.nombre=nombre
        self.edad=edad
        self.genero=genero
        self.sueldo=sueldo
    def dame_nombre(self):
        return self.nombre
    def dime_edad(self):
        return self.edad
    def dame_genero(self):
        return self.genero
    def dame_sueldo(self):
        return self.sueldo

    def aumentar_sueldo(self):
        return print(self.sueldo+100)
    def disminuir_sueldo(self):
        return print(self.sueldo-100)

pablo=empleado('Pablo',29,'masculino',2300)

print('nombre: ', pablo.dame_nombre())
print('edad: ', pablo.dime_edad())
print('genero: ', pablo.dame_genero())
print('sueldo inicial: ', pablo.dame_sueldo())
pablo.aumentar_sueldo()
        
