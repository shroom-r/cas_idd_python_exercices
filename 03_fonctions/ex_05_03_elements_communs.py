from ex05_01_elements_communs import common
from ex05_02_elements_communs import common2
import timeit

word1 = 'anticonstitutionnellement'
word2 = 'ecclésiastique'

print("Execution de common (implementation avec 'set'):")
print("\ttimeit : " + str(timeit.timeit('common(word1, word2)', globals=globals())))
print("Execution de common2 (implementation sans 'set', comparaison avec boucles imbriquées):")
print("\ttimeit : " + str(timeit.timeit('common2(word1, word2)', globals=globals())))
