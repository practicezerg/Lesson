class Cat:
    name = None
    age = None
    color = None


    def set_data(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color


    def get_data(self):
        print(self.name, "age:", self.age, "Color:", self.color)

cat1 = Cat()
cat2 = Cat()
cat1.set_data("Снежок", 3, "Черный")
cat2.set_data("Трутень", 12, "Белый")

print(cat1.name, cat2.age)
print(cat1.get_data())