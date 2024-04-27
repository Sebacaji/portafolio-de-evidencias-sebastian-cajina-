salario_objetivo = 500

dinero_necesario = 0

for i in range(15): 
    salario = float(input("ingrese el salario #{}: ".format(i+1)))

    if salario < salario_objetivo:
        dinero_necesario += salario_objetivo - salario

print("para que todo ganen $500 se nececitan ${:.2f}".format(dinero_necesario))