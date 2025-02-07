tempCelsius = float(input("Entrez une température en °C : "))
# Ma version :
print(f"Equivalent en °F : {(tempCelsius * (9/5)) + 32}")

# Correction possible :
print("Ma version :")
fahrenheit = tempCelsius * 1.8 + 32

print("Version corrigée (arrondi à deux dixièmes)")
print(f"Equivalent en °F : {fahrenheit:.2f}")
# Le :.2f à la fin sert à arrondir à deux dixièmes
# Le f est pour float (si on lui donne une chaîne de caractères il essaie de transformer)