class cuenta():
    def __init__(self,ingresos=None, transfer=None, reintegro=None):
        self.dinero= 15000#ponemos de ejemplo 15000,
         #ya que sino no se podria transferir nada
        if ingresos is not None:
            self.ingresos=ingresos
        else:
            self.ingresos=0

        if transfer is not None:
            self.transfer=transfer
        else:
            self.transfer=0

        if reintegro is not None:
            self.reintegro=reintegro
        else:
            self.reintegro=0

    def get_ingresos(self):
        return self.ingresos

    def transferencia(self):
        return self.transfer

    def reint(self):
        return self.reintegro

persona=cuenta(1500, 300, 245)

print(persona.get_ingresos())
print(persona.transferencia())
print(persona.reint())
            
