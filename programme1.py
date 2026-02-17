ca = float(input("Entre le chiffre d'affaires : "))

if ca > 5000:
    taux = 0.07
else:
    taux = 0.05

commission = ca * taux

print("\n--- Résultat ---")
print("CA :", round(ca, 2), "€")
print("Taux appliqué :", round(taux * 100, 2), "%")
print("Commission :", round(commission, 2), "€")
print("Tets")
print("Deuxième test")