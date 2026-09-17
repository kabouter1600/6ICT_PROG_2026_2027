# nummers = ["+32 470 998301", "+32 483 313220", "+32 453 231456"]
# namen = ["Jan", "Piet", "Kapper Korneel"]

# Welke_naam = input("Van wie wilt u het tel nummer?  ")
# for index, naam in enumerate(namen):
#     if naam == Welke_naam:
#         index_nummer = index
# print(nummers[index_nummer])

telefoonboek = {
    "Jan": "+32 470 998301",
    "Piet": "+32 483 33220",
    "Kapper Korneel": "+32 blah blah blah"
}
naam = input("Geef naam"  )
if naam in telefoonboek:
    print("Naam bestaat in telefoonboek")
    print(telefoonboek[naam])
else:
    print("naam bestaat niet in telefoonboek")