import random

class Things:
    def __init__(self, Seeds, Animal, Machines, Worker):
        self.Seeds = Seeds
        self.Animal = Animal
        self.Machines = Machines
        self.Worker = Worker

    def TotalValue(self, animalList, seedsList, productList):
        totalValue = 0
        # Calculate total value by going through animals, seeds, and products
        for itemList in [animalList, seedsList, productList]:
            for item in itemList:
                totalValue += (item.number * item.price)
        return totalValue

class Animal:
    def __init__(self, name, number, product, price, productionCoefficient):
        self.name = name
        self.number = number
        self.product = product
        self.price = price
        self.productionCoefficient = productionCoefficient

class Weather:
    def __init__(self, name, temperature, moisture, weather):
        self.name = name
        self.temperature = temperature
        self.moisture = moisture
        self.weather = weather
        self.lastWeather = "sunny"
        self.weeklyWeather = "sunny"

    def change_weather(self, weatherList):
        self.lastWeather = self.weather
        self.weather = random.choice(weatherList)

# Creating weather instances
sunny = Weather("Sunny", "50°C", "20%", "sunny")
rainy = Weather("Rainy", "10°C", "100%", "rainy")
cloudy = Weather("Cloudy", "30°C", "50%", "cloudy")
snowy = Weather("Snowy", "-10°C", "80%", "snowy")

weatherList = [sunny, rainy, cloudy, snowy]

# Creating animal instances
cow = Animal("Cow", 0, "Milk", 100, 3)
pig = Animal("Pig", 0, "Meat", 80, 1)
chicken = Animal("Chicken", 0, "Egg", 20, 5)
sheep = Animal("Sheep", 0, "Wool", 50, 3)

# Creating seeds and products lists
productRice = ["rice"]
productWheat = ["bread", "noodles", "biscuits"]
productSoybeans = ["tofu", "animal_food", "soy", "oil"]
productOats = ["oatmeal"]

# List of animals, seeds, and products
animalList = [cow, pig, chicken, sheep]
seedsList = productRice + productWheat + productSoybeans + productOats  # combine all seed products in one list
productList = ["milk", "meat", "egg", "wool"] + productRice + productWheat + productSoybeans + productOats

# Example of using the TotalValue method
things = Things(Seeds=seedsList, Animal=animalList, Machines=[], Worker=[])
total_value = things.TotalValue(animalList, seedsList, productList)
print(f"Total value: {total_value}")

# Example of changing the weather
for weather in weatherList:
    weather.change_weather(weatherList)
    print(f"Weather: {weather.name} | Last: {weather.lastWeather} | Current: {weather.weather}")