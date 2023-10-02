import sqlite3
import datetime
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

shops = reuslt
#  Pour le fabricant d’identifiant 1664, et parmi le top 10 des magasins vendant les produits de la catégorie d’identifiant 5, quel est en moyenne la part du nombre de produits qu’offre le fabricant 1664 dans l’ensemble des produits de catégorie 5 en vente dans ces magasins?
# add 1664 to the top 10 magasins
reuslt = cur.execute("SELECT magID, COUNT(*) FROM categories WHERE fabID = 1664 GROUP BY magID ORDER BY COUNT(*) DESC LIMIT 10").fetchall()
shops.extend(reuslt)

# get the average of the top 10 magasins
print ('Average of the top 10 shops and 1664 ', sum([x[1] for x in shops]) / len(shops))


# Pour la catégorie d’identifiant 5, combien y a-t-il d’acteurs sur le marché ayant un produit de cette catégorie en Janvier, en Février, et en Mars?
catId = 5
start_date = 20220101
end_date = 20220331

result = cur.execute("SELECT DISTINCT fabID FROM products WHERE catID = ? AND dateID BETWEEN ? AND ?",
                     (catId, start_date, end_date)).fetchall()

total = len(result)
print('Total actors in January, February, and March:', total)

# Idem avec des valeurs prises pendant les soldes d’hiver (Janvier).
start_date = 20220101
end_date = 20220131

result = cur.execute("SELECT DISTINCT fabID FROM products WHERE catID = ? AND dateID BETWEEN ? AND ?",
                     (catId, start_date, end_date)).fetchall()

total = len(result)
print('Total actors in January:', total)

# Idem avec des valeurs prises pendant les soldes d’hiver (Janvier) et celles d’été (Juillet).
start_date_winter = 20220101
end_date_winter = 20220131
start_date_summer = 20220701
end_date_summer = 20220731

result_winter = cur.execute("SELECT DISTINCT fabID FROM products WHERE catID = ? AND dateID BETWEEN ? AND ?",
                            (catId, start_date_winter, end_date_winter)).fetchall()

result_summer = cur.execute("SELECT DISTINCT fabID FROM products WHERE catID = ? AND dateID BETWEEN ? AND ?",
                            (catId, start_date_summer, end_date_summer)).fetchall()

total_winter = len(result_winter)
total_summer = len(result_summer)
print('Total actors in January and July (Winter and Summer sales combined):', total_winter + total_summer)

# Idem pour la question 1.4., avec des valeurs prises une fois tous les mois du 1er Janvier 2022 jusqu’au jour du jour.
# Define the start date as January 1, 2022
start_date = 20220101

# Get the current date
current_date = int(datetime.datetime.now().strftime('%Y%m%d'))

# Initialize a list to store distinct fabIDs
distinct_fabids = []

# Loop through each month from January 2022 to the current month
current_month = int(datetime.datetime.now().strftime('%Y%m'))
while start_date <= current_date:
    result = cur.execute("SELECT DISTINCT fabID FROM products WHERE catID = ? AND dateID BETWEEN ? AND ?",
                         (catId, start_date, start_date + 31)).fetchall()
    
    distinct_fabids.extend([fabid[0] for fabid in result])

    # Move to the next month
    start_date = int((datetime.datetime.strptime(str(start_date), '%Y%m%d') + datetime.timedelta(days=32)).strftime('%Y%m%d'))

# Get the total number of distinct actors
total_actors = len(set(distinct_fabids))

print('Total actors for each month from January 2022 until today:', total_actors)

