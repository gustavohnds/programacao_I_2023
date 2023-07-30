import time
class Bomba_de_Combustivel:
    def __init__ (self, valor_litro, quantidade_disponivel):
        self.__valor_litro = valor_litro
        self.__quantidade_disponivel = quantidade_disponivel

    @property
    def quantidade_disponivel(self):
        return self.__quantidade_disponivel
    @quantidade_disponivel.setter
    def quantidade_disponivel(self, nova_quantidade):
        # novaquantidade = self.__quantidade_disponivel - litros_abastecidos
        self.__quantidade_disponivel = nova_quantidade

    def abastecer_por_valor(self): 
        while True:
            valor = float(input("Digite o valor que deseja abastecer:"))
            if valor > 0 and (self.quantidade_disponivel - (valor/self.__valor_litro)) >= 0:
                litros_abastecidos = valor/self.__valor_litro
                self.quantidade_disponivel = self.quantidade_disponivel - litros_abastecidos
                time.sleep(1)
                return litros_abastecidos
                break
            else:
                if (self.quantidade_disponivel - (valor/self.__valor_litro)) < 0:
                    print("Não temos combustível suficiente, tente um número menor")
                elif valor <= 0:
                    print("Valor inválido, deve ser maior que zero.")

    def abastecer_por_litro(self):
        while True:
            quantidade_litros = float(input("Digite a quantidade de litros que deseja abastecer:"))
            if quantidade_litros > 0 and (self.quantidade_disponivel - quantidade_litros) >= 0:
                valor_a_pagar = quantidade_litros*(self.__valor_litro)
                self.quantidade_disponivel = self.quantidade_disponivel - quantidade_litros
                time.sleep(1)
                return valor_a_pagar
                break
            else:
                if self.quantidade_disponivel - quantidade_litros < 0:
                    print("Não temos combustível suficiente, tente um número menor")
                elif quantidade_litros <= 0:
                    print("Valor inválido, deve ser maior que zero.")

class Gasolina(Bomba_de_Combustivel):
    def __init__(self, valor_litro, quantidade_disponivel, tipo_combustivel):
        super().__init__(valor_litro, quantidade_disponivel)
        self.gasolina = tipo_combustivel
    
    def abastecer_por_valor(self): 
        return super().abastecer_por_valor()

    def abastecer_por_litro(self):
        return super().abastecer_por_litro()
    
class Etanol(Bomba_de_Combustivel):
    def __init__(self, valor_litro, quantidade_disponivel, tipo_combustivel):
        super().__init__(valor_litro, quantidade_disponivel)
        self.etanol = tipo_combustivel
    
    def abastecer_por_valor(self): 
        return super().abastecer_por_valor()

    def abastecer_por_litro(self):
        return super().abastecer_por_litro()

bomba1 = Bomba_de_Combustivel(5, 100) #instanciação do objeto
print("Com esse valor, você abasteceu:", bomba1.abastecer_por_valor(), "litros") #teste de classe
print("O total a pagar é de: R$", bomba1.abastecer_por_litro()) #teste de classe
print("Ainda resta", bomba1.quantidade_disponivel, "litros.")

print("--------------")
print(" 1 - GASOLINA ")
print(" 2 - ETANOL   ")
print("--------------")
gasolina1 = Gasolina(6, 1000, "gasolina")
etanol1 = Etanol(4, 1000, "etanol")
while True:
    g_ou_e = input("Digite o tipo de combustível que deseja abastecer (1 ou 2):")
    if g_ou_e == "1":
        tipo_abastecimento = input("Deseja abastecer por litro ou por valor (V/L)?")
        while True:
            if tipo_abastecimento.upper() == "V":
                print("Com esse valor, você abasteceu:", gasolina1.abastecer_por_valor(), "litros") 
                break 
            elif tipo_abastecimento.upper() == "L":
                print("O total a pagar é de: R$", gasolina1.abastecer_por_litro())
                break
            else:
                print("Inválido. Tente Novamente.")
    if g_ou_e == "2":
        tipo_abastecimento = input("Deseja abastecer por litro ou por valor (V/L)?")
        while True:
            if tipo_abastecimento.upper() == "V":
                print("Com esse valor, você abasteceu:", etanol1.abastecer_por_valor(), "litros") 
                break 
            elif tipo_abastecimento.upper() == "L":
                print("O total a pagar é de: R$", etanol1.abastecer_por_litro())
                break
            else:
                print("Inválido. Tente Novamente.")
    d = input("Deseja fazer mais algum abastecimento? (S/N):")
    if d.upper() == "N":
        print("Agradecemos a preferência.")
        break
    elif d.upper() == "S":
        print("Ok, vou chamar um frentista.")
        
# INTEGRANTES DO GRUPO
# Beatriz Cristina Deschamps
# Gustavo Henrique Nogueira dos Santos
# Kemilly Domingos de Souza
# Leonardo Oliveira de Sousa
# Letícia Gabriela Henschel
# 202