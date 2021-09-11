print("con 2500 de sueldo/n")
sueldoEmp = 2500;
if (sueldoEmp >2000):
    print("El salario es de: $"+ str(sueldoEmp))
    sueldoEmp +=5* sueldoEmp/100;
    print("por lo tanto el aumento es del 5%/n")
    print("Nuevo sueldo:" + str (sueldoEmp))

elif (sueldoEmp<2000 and sueldoEmp >0):
    print("El sueldo es de : $"+ str(sueldoEmp) )
    sueldoEmp += 10  * sueldoEmp / 100;
    print("por lo tanto el aumento es del 10%/n")
    print("Nuevo sueldo:" + str(sueldoEmp))

print("/nCon 1500 de sueldo")
sueldoEmp = 1500;
if (sueldoEmp>2000):
    print("/nEl salario es de: $" + str(sueldoEmp))
    sueldoEmp += 5 * sueldoEmp / 100;
    print("por lo tanto el aumento es de 5%/n")
    print("Nuevo sueldo:" + str(sueldoEmp))

elif (sueldoEmp < 200 and sueldoEmp > 0):
    print("El salario es de: $" + str(sueldoEmp))
    sueldoEmp +=10* sueldoEmp /100;
    print("Por lo tanto el aumento es del 10%/n")
    print("Nuevo sueldo:" + str (sueldoEmp))
