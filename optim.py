from pulp import LpMaximize, LpProblem, LpVariable

lemonade = LpVariable("Lemonade", lowBound=0, cat="Integer")
fruit_juice = LpVariable("FruitJuice", lowBound=0, cat="Integer")


model = LpProblem("Maximize_Production", LpMaximize)


model += lemonade + fruit_juice, "Total_Production"

#  Обмеження 
model += 2 * lemonade + 1 * fruit_juice <= 100, "Water"
model += 1 * lemonade <= 50, "Sugar"
model += 1 * lemonade <= 30, "LemonJuice"
model += 2 * fruit_juice <= 40, "FruitPuree"


model.solve()


print(f"Lemonade produced: {lemonade.varValue}")
print(f"Fruit Juice produced: {fruit_juice.varValue}")
print(f"Total production: {lemonade.varValue + fruit_juice.varValue}")