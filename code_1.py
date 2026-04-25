import csv
def generer_fichier():
    with open("ventes.csv", mode='w', newline='') as fichier:
        writer = csv.writer(fichier)
        writer.writerow(["ID", "Prix", "Quantite", "Remise"])
        writer.writerow([101, 15.0, 3, 10])
        writer.writerow([102, 25.0, 2, 5])
        writer.writerow([103, 10.0, 5, 0])
def lire_fichier(nom_fichier):
    ventes = []
    with open(nom_fichier, mode='r') as fichier:
        lecteur = csv.DictReader(fichier)
        for ligne in lecteur:
            ventes.append({
                "ID": int(ligne["ID"]),
                "Prix": float(ligne["Prix"]),
                "Quantite": int(ligne["Quantite"]),
                "Remise": float(ligne["Remise"])
            })
    return ventes
def calculer_total(ventes):
    total = 0
    max_ca = 0
    id_max = None
    for vente in ventes:
        # CA Brut
        ca_brut = vente["Prix"] * vente["Quantite"]
        # CA Net (correction remise)
        ca_net = ca_brut * (1 - vente["Remise"] / 100)
        # TVA
        tva = ca_net * 0.20
        # Ajouter sans changer ta logique
        vente["CA_Brut"] = round(ca_brut, 2)
        vente["CA_Net"] = round(ca_net, 2)
        vente["TVA"] = round(tva, 2)
        total += ca_net
        # produit le plus rentable
        if ca_net > max_ca:
            max_ca = ca_net
            id_max = vente["ID"]
    return total, id_max
def ecrire_fichier(nom_fichier, ventes):
    champs = ["ID", "Prix", "Quantite", "Remise", "CA_Brut", "CA_Net", "TVA"]

    with open(nom_fichier, mode='w', newline='') as fichier:
        writer = csv.DictWriter(fichier, fieldnames=champs)
        writer.writeheader()
        for vente in ventes:
            writer.writerow(vente)
def main() -> None:
    generer_fichier() 
    ventes = lire_fichier("ventes.csv")
    total, id_max = calculer_total(ventes)
    ecrire_fichier("resultats_final.csv", ventes)
    print(f"Le total des ventes est: {total:.2f} euros")
    print(f"Produit le plus rentable (ID): {id_max}")
if __name__ == "__main__":
    main()