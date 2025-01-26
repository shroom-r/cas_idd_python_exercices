# 1. Pyhton comme calculette
### 1
Lorsqu'on mélange les types, par ex 'int' + 'float', le résultat est de type float

### 2
Pour les int, il n'y a pas de limite de taille. Il y a par contre un limite dans le nombre de digit.
L'erreur affichée : ValueError: Exceeds the limit (4300 digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit
Pour les float, il y a une taille limite. Un trop grand résultat génèrera une erreur 'OverflowError : Result too large'

### 3

### 4
On s'attendrait à ce que le résultat soit 0 mais ce n'est pas le cas.
Pourquoi ?????
La conversiont en 'int' ajoute des valeurs bizarres...


# 2. Le module Math
RAS

# 3. Les chaînes de caractères
### 1
Les délimiteurs triplés permettent de faire des chaînes de caractères sur plusieurs lignes (sans besoin d'escape le saut de ligne).
Les délimiteurs simples : Si on utilise les guillements simples, pas besoin d'escape les guillements doubles dans la chaîne de caractère et inversement.

### 2
?

### 3
La seule opération qui marche c'est l'addition. C'est la synthaxe pour concaténer deux chaînes de caractères.

### 4
Si on mélange les types string integer, on peut utiliser la multiplication. Par exmple la chaîne de caractères `'aaaaa'` peut s'écrire `'a' * 5`.

# 8
En écrivant b = a, les variables a et b sont liées au même tableau [1,2,3]. En modifiant le tableau a, le tableau b est aussi impacté.