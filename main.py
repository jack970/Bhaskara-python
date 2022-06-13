from bhaskara import Bhaskara

class App:
    def __init__(self):
        self.a = float(input('Digite o valor de a: '))
        self.b = float(input('Digite o valor de b: '))
        self.c = float(input('Digite o valor de c: '))

    def run(self):
        bhaskara = Bhaskara(self.a, self.b, self.c)
        resultado = bhaskara.printa_resultados()
        
        print(resultado)
    
if __name__ == '__main__':
    app = App()
    app.run()