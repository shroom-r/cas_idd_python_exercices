# 1. Pyhton comme calculette
### 1
Lorsqu'on mélange les types, par ex 'int' + 'float', le résultat est de type float

### 2
Pour les int, il n'y a pas de limite de taille. Il y a par contre un limite dans le nombre de digit.
L'erreur affichée : ValueError: Exceeds the limit (4300 digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit
Pour les float, il y a une taille limite. Un trop grand résultat génèrera une erreur 'OverflowError : Result too large'

### 3
OK conversion types natifs

### 4
On s'attendrait à ce que le résultat soit 0 mais ce n'est pas le cas.
Pourquoi ?????
La conversiont en 'int' ajoute des valeurs bizarres...

### 5
OK nombre complexes

# 2. Le module Math
### 1
OK Racine carré

### 2
OK essais autres fonctions mathématiques

### 3
OK aide à la completion dans l'IDE

# 3. Les chaînes de caractères
### 1
Les délimiteurs triplés permettent de faire des chaînes de caractères sur plusieurs lignes (sans besoin d'escape le saut de ligne).
Les délimiteurs simples : Pas de string sur plusieurs lignes. Pour cela, il faut utiliser des caractères \n ou d'autres pour les tabulations, etc.
Si on utilise les guillements simples, pas besoin d'escape les guillements doubles dans la chaîne de caractère et inversement.

### 2
?
Facilite la synthaxe du langage ?
Facilite une utilisation plutôt qu'une autre en fonction du clavier
Facilite la lisibilité par exemple dans le cas où notre phrase contient des guillements ou apostrophes (pas besoin de les escape selon le délimiteur utilisé).
?

### 3
La seule opération qui marche c'est l'addition. C'est la synthaxe pour concaténer deux chaînes de caractères.

### 4
Si on mélange les types string integer, on peut utiliser la multiplication. Par exmple la chaîne de caractères `'aaaaa'` peut s'écrire `'a' * 5`.

# 4.Variables
### 1
Certaines choses sont interdites :
- Tous les mots réservés de pyhton ne peuvent pas être utilisé pour nommer un variable (if, then, for, etc.)
- Selon W3 schools :
  
    A variable name must start with a letter or the underscore character
    A variable name cannot start with a number
    A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
    Variable names are case-sensitive (age, Age and AGE are three different variables)
    A variable name cannot be any of the Python keywords.

### 2
OK integration variables dans chaînes de caractères.
Dans thonny, quelques erreurs sortent lorsque j'ai utilisé certaine synthaxe qui fonctionne lorsque je lance le programme depuis la console.

# 5.Expression vs print
On peut parfois être amenés à calculer des choses, concaténer des chaines, etc. sans forcément vouloir les print. Dnas un fichier .py, seul le print serait imprimé. Parfois c'est nécessaire pour debugger ou informer l'utilisateur, parfois on ne veut pas forcément imprimer un résultat.

Le `1+1` qui affiche le résultat n'arrive que dans la console en mode interactif. Dans un programme ce n'est jamais le cas.

# 6.Premiers programmes python
OK fait

# 7.Débogueur
OK fait

# 8.Et pour finir...
En écrivant b = a, les variables a et b sont liées au même tableau [1,2,3]. En modifiant le tableau a, le tableau b est aussi impacté.