# import pandas as pd

# import csv data file with a bunch of brand names
# data = pd.read_csv("7003_1.csv", low_memory=False, index_col=0)
#
# index = data.index
# columns = data.columns
# values = data.values
#
# print(columns)
#
# type(index)
# type(columns)
# type(values)
#
# brands = data["brand"]
#
#
# # sort out duplicate brands from data
# old_brand = []
# for i, b in enumerate(brands):
#     b = str(b).replace("-", " ")
#     if b not in old_brand:
#         old_brand.append(b)
#
# df_brands = {'Brand': old_brand}
# df = pd.DataFrame(df_brands, columns= ['Brand'])
# df.to_csv("brand_list.csv")

import csv

old_brand = []

with open('brand_list.csv', 'r') as file:
    my_reader = csv.reader(file, delimiter=',')
    for row in my_reader:
        old_brand.append(row[1])

print(f"Searching through a total of {len(old_brand)} brands!")

checkbrands = True
while checkbrands == True:


    # get input for which brands ending in what to search for
    print()
    print("Keywords [Contains, Ending, Starting]")
    print("Usage: contains ace, ending na, starting s")
    search = input("Search for brands: ")
    print()


    def list_search(brand_end_in_an, term, function):
        # print the brands found if any
        print("---------------------------------------------------")
        print(f"There are a total of {len(brand_end_in_an)} brands {function} {term}!")
        for i, b in enumerate(brand_end_in_an):
            print(b)
        print("---------------------------------------------------")


    def contains(term):
        # search brands list for desired brands
        brand_end_in_an = []
        for i, b in enumerate(old_brand):
            if term in b.lower():
                print(b)
                brand_end_in_an.append(b)

        list_search(brand_end_in_an, term, "containing")
        print()


    def ending(term):
        # search brands list for desired brands
        brand_end_in_an = []
        for i, b in enumerate(old_brand):
            an = str(b)[-len(term):]
            if an.lower() == term:
                brand_end_in_an.append(b)

        list_search(brand_end_in_an, term, "ending in")


    def starting(term):
        # search brands list for desired brands
        brand_end_in_an = []
        for i, b in enumerate(old_brand):
            an = str(b)[:len(term)]
            if an.lower() == term:
                brand_end_in_an.append(b)

        list_search(brand_end_in_an, term, "starting with")


    def check(search):
        mode = search.replace(" ", "")
        if mode[:8].lower() in "contains":
            contains(mode[8:].lower())
        elif mode[:6].lower() == "ending":
            ending(mode[6:].lower())
        elif mode[:8].lower() == "starting":
            starting(mode[8:].lower())

    check(search)
