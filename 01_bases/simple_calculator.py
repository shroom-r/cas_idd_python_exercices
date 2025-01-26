a = int(input("Entrez le nombre a: "))
b = int(input("Entrez le nombre b: "))

print(f'a + b = {a+b}')
print(f'a * b = {a*b}')
aPowerB = a**b
print(f"L'élévation de a à la puissance b est {aPowerB}.")
print(f"Ce nombre s'écrit avec {len(str(aPowerB))} chiffres et contient {str(aPowerB).count("1")} fois le chiffre 1.")
