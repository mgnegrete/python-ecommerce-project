from oscar.apps.catalogue.categories import create_from_breadcrumbs

#define the categories list


categories = [
    'Clothing > Men > T-Shirts',
    'Clothing > Men > Sweatershirts',
    'Clothing > Men > Hats',
    'Clothing > Men > Polos',
    'Clothing > Men > Outerwear',

    'Clothing > Women > T-Shirts',
    'Clothing > Women > Sweatershirts',
    'Clothing > Women > Hats',
    'Clothing > Women > Polos',
    'Clothing > Women > Outerwear',

    'Clothing > Accessories',

]

for breadcrumbs in categories:
    create_from_breadcrumbs(breadcrumbs)

print("categories added succesfully")
