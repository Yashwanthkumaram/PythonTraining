class Category():
    def __init__(self , name , sub_category):
        self.name = name
        self.sub_category = sub_category

        pass

class Product():
    def __init__(self ,name ,categories):
        self.name  = name
        self.categories = categories
        pass

    def display_categories(self):
        parent_category= []
        parent_category.append(self.categories.name)
        for category in self.categories.sub_category:
            parent_category.append(category.name)
        res = '-'.join(parent_category)
        print(res)


mobiles = Category("mobiles" ,[])
electronics = Category("electronics" ,[mobiles])


rog14 = Product("rog14", electronics)

rog14.display_categories()