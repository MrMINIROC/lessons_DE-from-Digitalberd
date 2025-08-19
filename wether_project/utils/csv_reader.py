import csv

def read_city_names(filename=r"C:\Users\dm440\OneDrive\Рабочий стол\lessons_DE-from-Digitalberd\wether_project\utils\cities.csv"):
    cities = []
    with open(filename, newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cities.append(row["0"])
    return cities


