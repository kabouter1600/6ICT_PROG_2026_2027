lijst = [ [4, 5, 1, 9, 3],
          [4, 6, 1],
          [8, 3, 5, 0],
          [7] ]
aantal_waardes = 0
som = 0
for index_hoofd, sublijst in enumerate(lijst):
  for getal in sublijst:
    som += getal
    aantal_waardes += 1
totaal = som/aantal_waardes
print(totaal)