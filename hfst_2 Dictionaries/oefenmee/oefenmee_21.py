lijst_2D = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("rij kolom element")
for index_lijst, lijst in enumerate(lijst_2D):
    for index, getal in enumerate(lijst):
        if index_lijst == index:
            print(f"{index_lijst};{index} = {getal}")