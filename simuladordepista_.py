import time

class Veiculo:
    def __init__(self, modelo, tanque, rendimento, desenho):
        self.modelo = modelo
        self.tanque = tanque # capacidade em litros
        self.rendimento = rendimento # km/litro
        self.odometro = 0  # km/s percorridos
        self.desenho = desenho # caracteres que representam o veículo
    def andar(self):
        # atualiza o odometro
        self.odometro += self.rendimento    
        # gastou gasolina :-)
        self.tanque -= 1 # self.tanque = self.tanque - 1

class Pista:
    def __init__(self, extensao):
        self.extensao = extensao
        self.veiculos = []
    def tick(self):
        for v in self.veiculos:
            # ainda tem pista pra andaR?
            if v.odometro <= self.extensao:
                v.andar() # anda, veículo :-)
                
    def pista_grafica(self):
        for v in self.veiculos:
            s = "." * int(v.odometro/10)
            print(v.modelo,"(",v.odometro,"):",s,v.desenho)            

fox = Veiculo("Fox", 42, 25, "o~W~o")
biz = Veiculo("Honda Biz", 5, 40, "o-o")
camaro = Veiculo("Camaro", 72, 50, "o=o")
indianapolis = Pista (500)
indianapolis.veiculos.append(fox)
indianapolis.veiculos.append(biz)
indianapolis.veiculos.append(camaro)
while True:
    indianapolis.tick() # fazer os veículos andarem
    # mostrar estado dos veículos
    #print(indianapolis.veiculos[0].modelo, "andou", indianapolis.veiculos[0].odometro)
    #print(indianapolis.veiculos[1].modelo, "andou", indianapolis.veiculos[1].odometro)
    indianapolis.pista_grafica()
    # esperar um pouco
    time.sleep(1)
    # os veículos terminaram de andar na pista?
    #if indianapolis.veiculos[0].odometro >= 500 and indianapolis.veiculos[1].odometro >= 500 and indianapolis.veiculos[2].odometro >=500:
    #for
    continua = False
    for v in indianapolis.veiculos:
        if v.odometro<500:
            continua = True
    if continua == False:
        break # encerra o programa

print("Fim da corrida")

'''
EXERCICIOS:
#a) (fácil) exibir a pista gráfica (comentar linhas 40 e 41 e descomentar linha 42)
#b) (trabalhoso) incluir mais dois veículos
#c) (médio) generalizar a exibição de veículos usando "for"
d) (difícil) incluir atributo velocidade no veículo
'''
