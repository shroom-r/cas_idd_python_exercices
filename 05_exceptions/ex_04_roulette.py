# counter1 = 9
# counter2 = 10
# counter3 = 11
# try:
#     while True:
#         if counter1 == 9:
#             counter1 = 0
#         else:
#             counter1 += 1
#         if counter2 == 10:
#             counter2 = 0
#         else:
#             counter2 += 1
#         if counter3 == 11:
#             counter3 = 0
#         else:
#             counter3 += 1
# except KeyboardInterrupt:
#     print("Vous avez appuyé ctrl-c!")
#     print(f'Valeurs de compteurs : {counter1} {counter2} {counter3}')
#     if counter1 == counter2 and counter2 == counter3:
#         print("Vous avez gagné !")
#     else:
#         print("Vous avez perdu !")

# Correction, bien meilleure version
x = y = z = 0

try:
    while True:
        x = (x+1) % 10
        y = (x+1) % 11
        z = (x+1) % 12
except KeyboardInterrupt:
    print('Vous avez appuyé ctrl-c!')

print('Valeurs des compteurs:', x, y, z)

if x == y == z:
    print("Vous avez gagné!")
else:
    print("Vous avez perdu!")