# Programa para invertir un número de 4 digitos

# input
n = input("digite un número de 4 digitos : ")
n = int(n)

# processsing
r4 = n%10
r3 = (n//10)%10
r2 = (n//100)%10
r1 = (n//1000)%10

ni = r4*1000 + r3*100 + r2*10 + r1

# output
print("-----Resultados-----")
print("Numero original: " + str(n))
print("Ultimo digito: " + str(r4))
print("Tercer digito: " + str(r3))
print("Segundo digito: " + str(r2))
print("Primer digito: " + str(r1))
print("El numero invertido es: " + str(ni))
