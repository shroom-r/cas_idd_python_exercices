a = int(input("Entrez le nombre a: "))
b = int(input("Entrez le nombre b: "))

print(f'a + b = {a+b}')
print(f'a * b = {a*b}')
aPowerB = a**b
print("Ma version :")
print(f"L'élévation de a à la puissance b est {aPowerB}.")
print(f"Ce nombre s'écrit avec {len(str(aPowerB))} chiffres et contient {str(aPowerB).count("1")} fois le chiffre 1.")

# Correction :
power_as_string = str(a**b)
l = len(power_as_string)
n_1 = power_as_string.count("1")

print("Correction :")
print(f"""L'élévation de a à la puissance b est {power_as_string[:3]}..{power_as_string[-3:]}.
Ce nombre s'écrit avec {l} chiffres et contient {n_1} fois le chiffre 1.""")