import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import ast

def transformar_expresion(expresion):
    expresion = expresion.replace(" ", "")
    
    formula = expresion.replace("^", "**")  
    formula = formula + " "
    for n, it in enumerate(formula):
        if it == "x" and formula[n - 1] in [str(s) for s in range(0,10)]:
            formula = formula[:n] + "X" + formula[n + 1:]   
    
    formula_x = formula.replace("X", "*x") 
    
    return formula_x


class Funcion_Matematica:
    def __init__(self, _formula_=None):
        self._formula_ = _formula_

    def lineal(self, expresion, inplace=True):
        if not isinstance(expresion, str):
            raise TypeError("La expresion debe ser de tipo String.")
        
        if "x" not in expresion:
            raise ArithmeticError("La expresión debe contener la variable dependiente expresada\ncon la letra 'x'")
        
        form_x = transformar_expresion(expresion)

        if not inplace:
            return form_x
        else:
            self._formula_ = form_x

    def operar_expresion(self, numero):
        var_y = f"{self._formula_}".replace("x", f"({numero})")
        return eval(var_y)


    def grafico(self, init=-100, stop=100, num=1000):
        serie_x = np.linspace(init, stop, num)
        serie_y = [self.operar_expresion(x) for x in serie_x]

        plt.figure(figsize=(10, 6))
        sns.set(style="darkgrid")

        plt.plot(serie_x, serie_y, linestyle='-')

        plt.axvline(0, linestyle='-', color='grey')
        plt.plot([init * (10 ** 10), stop * (10 ** 10)], [0, 0], linestyle='-', color='grey')

        plt.title(f"f(x) = {self._formula_}")

        # plt.xticks(np.arange(-1000, 1000, 1))
        # plt.yticks(np.arange(-1000, 1000, 1))

        plt.xlim(-10, 10)
        plt.ylim(-10, 10)

        plt.show()