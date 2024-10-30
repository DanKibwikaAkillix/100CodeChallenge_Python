
katanga = ["Lubumbashi", "Kolwezi", "Likasi", "Kipushi"]
date_of_birth = [1990,1908,1876, 1877]
governor = ["Kibwika", "Antoime", "Mike", "Mickol"," "]

province = [katanga, date_of_birth, governor]
print(province[2])
# alter data

governor[1] = "Antoine"
print(province)

# extend or add data in my list
katanga.extend(["Herric City", "Mark City"])

print(date_of_birth.pop[0])