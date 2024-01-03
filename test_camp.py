string = input("f(x) = ")

string = string.replace(" ", "")
formula = string.replace("^", "**")

formula = formula + " "
# print(formula)

for n, it in enumerate(formula):
    if it == "x" and formula[n - 1] in [str(s) for s in range(0,10)]:
        formula = formula[:n] + "X" + formula[n + 1:]

formula_x = formula.replace("X", "*x")

print(formula_x)

print("texto a reemplazar".replace("reemplazar", "decorar"))

exec("potencia = 2 ** 5")
# print(potencia)

print((-2)**2)