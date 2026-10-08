dambord_2D = [
    ['W', 'Z', 'W', 'Z', 'W', 'Z'],
    ['Z', 'W', 'Z', 'W', 'Z', 'W'],
    ['W', 'Z', 'W', 'Z', 'W', 'Z'],
    ['Z', 'W', 'Z', 'W', 'Z', 'W'],
    ['W', 'Z', 'W', 'Z', 'W', 'Z'],
    ['Z', 'W', 'Z', 'W', 'Z', 'W']]

rij = int(input("geef een rij nummer"))
kolom = int(input("geef een kolom nummer"))
rij -= 1
kolom -= 1

print(dambord_2D[rij][kolom])

#omdat dit niet bestaat geeft het een error
for dambord, waarde in enumerate(dambord_2D):
    groote = dambord
for getal in waarde:
    aantal_kolomen += 1

if rij >= groote and kolom >= aantal_kolomen:
    rij = int(input("geef een rij nummer"))
    kolom = int(input("geef een kolom nummer"))
    rij -= 1
    kolom -= 1
    print(dambord_2D[rij][kolom])
else:
    print("dambord niet groot genoeg")