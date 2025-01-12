class produto:
    def __init__ (self, nome, preco = 1.99, desc=0 ):
        self.nome = nome
        self.__preco = preco
        self.desc = desc

    @property
    def preço_final(self):
        return (1 - self.desc) * self.preco
    
    @property
    def preco(self):
        return self.__preco
    
    @property
    def preco(self, novo_preco):
        if novo_preco > 0:
            self.__preco


class carro():
    def __init__(self, ligar, desligar):
        self.ligar = ligar
        self.desligar = desligar

class uno(carro):
    def acelerar(self):
        super().acelerar()
        return super(). acelerar

class contador:
    contador = 0

    @classmethod
    def inc(cls):
        cls.contador += 1 
        return cls.contador
    
    @classmethod
    def dec(cls):
            cls.contador -=1
            return cls.contador
    
c1 = contador()

print(c1.inc())
print (c1.inc())

@staticmethod
def maisum(n):
    return n+1

