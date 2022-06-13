class Bhaskara:
    def __init__(self, a, b, c):
        self.a = round(a)
        self.b = round(b)
        self.c = round(c)

    def delta(self):
        return round((self.b ** 2) - (4 * self.a * self.c))

    def raizes(self):
        x1 = ((-self.b + (self.delta() ** 0.5)) / (2 * self.a))
        x2 =  ((-self.b - (self.delta() ** 0.5)) / (2 * self.a))
        return x1, x2
    
    def delta_layout(self):
        return f"""a = {self.a} \
            \nb = {self.b} \
            \nc = {self.c} 
            \nΔ = ({self.b})² - 4 * {self.a} * {self.c} \
            \nΔ = {self.delta()}"""

    def raizes_layout(self, x1, x2):
        underline = "\u0332".join(f'- ({self.b}) +/- √{self.delta()}')
        center_divisao = f'2x{self.a}'.center(len(underline) -3)
        return f"""
            \nx = {underline}\
            \n{center_divisao} \
            \nx¹ = {x1}\nx² = {x2}"""

    def printa_resultados(self):
        delta = self.delta()
        delta_layout = self.delta_layout()

        if delta < 0:
            return f"{delta_layout}\nDelta é negativo, não existem raízes reais."
        else:
            x1, x2 = self.raizes()
            raizes = f"{self.raizes_layout(x1, x2)}"
            return f'{delta_layout}\n{raizes}'

