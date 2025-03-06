# def typed_input(prompt, expectedType = int):
#     value = input(prompt)
#     try:
#         convertedValue = expectedType(value)
#         if (str(value) != str(convertedValue)):
#             raise
#     except:
#         print("Vous devez fournir une entrée du type: " + str(expectedType))
#         typed_input(prompt, expectedType)
#     else :
#         print(convertedValue)


# Version corrigée. Le fait d'appeler typed_input dans l'exception crée un stack d'appel potentiellement croissant à l'infini. Tant dis que le mettre dans une boucle non
def typed_input(prompt, expectedType = int):

    while True:
        value = input(prompt)
        try:
            convertedValue = expectedType(value)
            if (str(value) != str(convertedValue)):
                raise
        except:
            print("Vous devez fournir une entrée du type: " + str(expectedType))
        else :
            print(convertedValue)
            return convertedValue
