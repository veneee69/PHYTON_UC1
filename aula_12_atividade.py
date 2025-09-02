# Atividades_aula_12

class Carro:
    def __init__(self, seguro, placa, reboque, cor):
        self.seguro = seguro
        self.placa =  placa
        self.reboque = reboque
        self.cor = cor
        self._garantia = True
        self._ligado = False

    def contratar_seguro(self):
        if self._ligado :
            print(f"\t\t [ok] Seguro contratado")
        else:
            self._ligado=True 
            print(f"\n\t [erro] Seguro ja contratado\t")

    def seguro_cancelar(self):
        if self._ligado :
            print(f"\t\t [ok] o seguro foi cancelado")
        else:
            print(f"\n\t [erro] o seguro ja foi cancelado\t")

    def info_cor(self):
        if self._ligado :
            status =  "ligado"
        else :
            status = "desligado"
        print(f"{self.seguro} - {self.reboque} esta {status}")

    def emplacar(self):
        if self.placa:
            print(f"\t\t [ok]  carro foi emplacado com a placa SRN-2019")

    def reboque_instal(self):
        if self.reboque:
            print(f"\t\t [ok] O reboque foi instalado")
        else:
            print(f"\n\t [erro] o Reboque ja foi instalado\t")

    def reboque_destinatario(self):
        if self.reboque:
            print(f"\t\t [ok] o reboque foi enviado")
        else:
            print(f"\n\t [erro] o reboque ja foi enviado\t")
    
meu_carro = Carro ("BMW", "X1", 2020, "amarelo")

print(meu_carro)

meu_carro.info_cor()

meu_carro.contratar_seguro()

meu_carro.seguro_cancelar()

meu_carro.emplacar()

meu_carro.reboque_instal()

meu_carro.reboque_destinatario()

#####


class Carro:
    def __init__(self, seguro, placa, reboque, cor):
        self.seguro = seguro
        self.placa =  placa
        self.reboque = reboque
        self.cor = cor
        self._garantia = True
        self._ligado = False

    def contratar_seguro(self):
        if self._ligado :
            print(f"\t\t [ok] Seguro contratado")
        else:
            self._ligado=True 
            print(f"\n\t [erro] Seguro ja contratado\t")

    def seguro_cancelar(self):
        if self._ligado :
            print(f"\t\t [ok] o seguro foi cancelado")
        else:
            print(f"\n\t [erro] o seguro ja foi cancelado\t")

    def info_cor(self):
        if self._ligado :
            status =  "ligado"
        else :
            status = "desligado"
        print(f"{self.seguro} - {self.reboque} esta {status}")

    def emplacar(self):
        if self.placa:
            print(f"\t\t [ok]  carro foi emplacado com a placa SRN-2019")

    def reboque_instal(self):
        if self.reboque:
            print(f"\t\t [ok] O reboque foi instalado")
        else:
            print(f"\n\t [erro] o Reboque ja foi instalado\t")

    def reboque_destinatario(self):
        if self.reboque:
            print(f"\t\t [ok] o reboque foi enviado")
        else:
            print(f"\n\t [erro] o reboque ja foi enviado\t")
    
meu_carro1 = Carro ("BMW", "X1", 2020, "amarelo")

meu_carro2 = Carro ("audi", "A3", 2020, "amarelo")

meu_carro
