def typed_input(prompt, expectedType = int):
    value = input(prompt)
    try:
        convertedValue = expectedType(value)
        if (str(value) != str(convertedValue)):
            raise
    except:
        print("Vous devez fournir une entrée du type: " + str(expectedType))
        typed_input(prompt, expectedType)
    else :
        print(convertedValue)
