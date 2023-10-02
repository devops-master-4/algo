import sqlite3
con = sqlite3.connect("./db/analytics.db")
cur = con.cursor()
catId = 5

# Pour la catégorie d’identifiant 5, combien y a t il d’acteurs sur le marché ayant un produit de cette catégorie?
reuslt = cur.execute("SELECT * FROM products WHERE catID = ? GROUP BY fabId  ORDER BY fabId", (catId,)).fetchall()
total = len (reuslt)
print ('Total acotrs ', total)

# Pour la catégorie d’identifiant 5, quel est en moyenne le nombre de produits qu’un fabricant offre sur le marché?
reuslt = cur.execute("SELECT fabId, COUNT(*) FROM products WHERE catID = ? GROUP BY fabId  ORDER BY fabId", (catId,)).fetchall()
print ('Average products ', sum([x[1] for x in reuslt]) / len(reuslt))

# Quels sont le top 10 des magasins parmi les magID enregistrés dans la base? N.B.:  based on the number of products
reuslt = cur.execute("SELECT magID, COUNT(*) FROM categories GROUP BY magID ORDER BY COUNT(*) DESC LIMIT 10").fetchall()
print ('Top 10 magasins ', reuslt)