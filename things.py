import random
import math

WEEKS_IN_ONE_ROUND = 52
WEEKS= 1

def start_rounds():
    round_input = input("How many rounds do you want to play?: " )
    try:
        round_input = int(round_input)
        print("Let's beginn ")
    
    except ValueError:
        while True:
            print("please input an iteger number")
            round_input = input("How many rounds do you want to play?: " )
            try:
                round_input = int(round_input)
                print("Let's beginn ")
                break
    
            except ValueError:
                continue

def rounds_played():
    while True:
        user_input = input()
        if user_input == "9":
            for weeks in WEEKS:
                WEEKS +=1
                current_weeks = WEEKS
                if current_WEEKS != 52:
                    continue
                else:
                    print("Congratulations you finished your first round")
            
        else:
            continue
    
        round_playing = current_week / WEEKS_IN_ONE_ROUND 
        rounded_rounds_playing = math.ceil(round_playing)

        print(f"You are currently in your {rounded_rounds_playing} round")
        # other method ("You are ... {}".format(rounded_rounds_playing))


class Keys():
    def __init__(self,name,money,totalValue,week):
        self.name= name
        self.money = money
        self.totalValue = totalValue
        self.week = week

    def TotalValue(self):

        TotalValue= 0

        for itemList in animalList,seedsList,productList:
            for item in itemList:
                self.totalValue += (item.number * item.price)
        return round(self.totalvalue,1)

#class Keys():

 #   def __init__(self,Seeds,Animal,Machines,Worker):
 #       self.Seeds= Seeds
  #      self.Animal= Animal
   #     self.Machines= Machines
   #     self.Worker= Worker

class Machines(Keys):
    def __init__(self,name,number,product,price,lastprice):
        self.name = name
        self.number = number
        self.product = product
        self.price = price
        self.lastprice =lastprice

        def Buy(self):
            if Keys.money > 0:
                
                print(">", self.name, "Market")
                print("--------------------------------------------")
                print("> Price            :", self.price)
                print("> Total Number     :", self.number)
                print("> Last Week Prices :", self.lastPrice, "$")
                print("> Total Money      :", farm.money, "$")
                print("> Max Buy Number   :", round((farm.money/self.price), 0))
                buyNumber = int(input("How much You want to Buy? "))
                farm.money = farm.money - (self.price * buyNumber)
                self.number = self.number + buyNumber
            else:
                print("\n> Not Enough Money!\n")

class Animal(Keys):
    def __init__(self,name,number,product,price,lastprice,productionCoefficient):
        self.name = name
        self.number = number
        self.product = product
        self.price = price
        self.lastprice =lastprice
        self.prodcutionCoefficient=productionCoefficient

    def Buy(self):
        if Keys.money > 0:
                
            print(">", self.name, "Market")
            print("--------------------------------------------")
            print("> Price            :", self.price)
            print("> Total Number     :", self.number)
            print("> Last Week Prices :", self.lastPrice, "$")
            print("> Total Money      :", farm.money, "$")
            print("> Max Buy Number   :", round((farm.money/self.price), 0))
            buyNumber = int(input("How much You want to Buy? "))
            farm.money = farm.money - (self.price * buyNumber)
            self.number = self.number + buyNumber
        else:
            print("\n> Not Enough Money!\n")
            
    def Sell(self):
        print(">", self.name, "Market")
        print("--------------------------------------------")
        print("> Price               :", self.price)
        print("> Total Number        :", self.number)
        print("> Last Week Prices    :", self.lastPrice, "$")
        print("> Total Money         :", farm.money, "$")
        print("> Max Buy Number      :", self.number)
        sellNumber = int(input("How much You want to Sell? "))
        if sellNumber <= self.number:
            farm.money = farm.money + (self.price * sellNumber)
            self.number = self.number - sellNumber
        else:
            print("\n> Error,You dont have!")
        
class Seeds():
    def __init__(self,name,number,product,price,productionCoefficient):
        self.name = name
        self.number = number
        self.product = product
        self.price = price
        self.prodcutionCoefficient=productionCoefficient

    def Buy(self):
        if Keys.money > 0:
                
            print(">", self.name, "Market")
            print("--------------------------------------------")
            print("> Price            :", self.price)
            print("> Total Number     :", self.number)
            print("> Last Week Prices :", self.lastPrice, "$")
            print("> Total Money      :", farm.money, "$")
            print("> Max Buy Number   :", round((farm.money/self.price), 0))
            buyNumber = int(input("How much You want to Buy? "))
            farm.money = farm.money - (self.price * buyNumber)
            self.number = self.number + buyNumber
        else:
            print("\n> Not Enough Money!\n")
            
    def Sell(self):
        print(">", self.name, "Market")
        print("--------------------------------------------")
        print("> Price               :", self.price)
        print("> Total Number        :", self.number)
        print("> Last Week Prices    :", self.lastPrice, "$")
        print("> Total Money         :", farm.money, "$")
        print("> Max Buy Number      :", self.number)
        sellNumber = int(input("How much You want to Sell? "))
        if sellNumber <= self.number:
            farm.money = farm.money + (self.price * sellNumber)
            self.number = self.number - sellNumber
        else:
            print("\n> Error,You dont have!")
        
        
class Worker():
    def __init__(self,name,number,product,price,productionCoefficient):
        self.name = name
        self.number = number
        self.product = product
        self.price = price
        self.prodcutionCoefficient=productionCoefficient  

    

    
        

    
              

class Weather(Keys):
    def __init__(self,name,temperature,moisture):
        self.name = name
        self.temperature= temperature
        self.moisture=moisture
         
        

    def WeatherChanges(self, weatherList):
        self.lastWeather = self.weather
        self.weather = random.choice(weatherList).name

    
    
keys = Keys("Farm",1000,0,1)

def week_changes(*Keys):
    global money
    global keys
    #user_input = input("Enter command: ").strip().upper()
    if user_input == "CHANGE WEEK":
        keys.week += 1
        print(f"Week has been updated to {keys.week}")
        salary_of_workers = lambda money: money - (Worker.number * 5)
    else:
        print("Invalid command")

def pandemic():
    pass
    

def lighting_bolt_animal():
    pass

    
    


rainy = Weather("Rainy","10°C","100%",)
cloudy = Weather("Cloudy","30°C","50%")
snowy = Weather("Snowy","-10°C","80%")
sunny = Weather("Sunny","50°C","20%")
                
weatherList = [sunny,rainy,cloudy,snowy]

cow = Animal("Cow",0,"Milk",100,3,1.5)
pig = Animal("Pig",0,"Meat",80,1,1.2)
chicken = Animal("Chicken",0,"Egg",20,5.3)
sheep = Animal("Sheep",0,"Wool",50,3,2.2)

#----------------------------- Products of seeds
productRice = [rice]
productWheat = [bread,noodles,biscuits]
productSoybeans= [tofu,animal_food,soy,oil]
productOats = [oatmeal]
#--------------------------------------

animalList = [cow,pig,chicken,sheep]
seedsList = [rice,wheat,soybeans,oats] 
productList = [milk,meat,egg,wool,productRice,productWheat,
               productSoybeans,productOats]
machinesList =[]

def PricesChange():
    for i in animalList:
        i.lastPrice = i.price
        i.price = round(i.price * (random.uniform(0.9, 1.1)), 2)

    for i in seedsList:
        i.lastPrice = i.price
        i.price = round(i.price * (random.uniform(0.85, 1.15)), 2)

    for i in productList:
        i.lastPrice = i.price
        i.price = round(i.price * (random.uniform(0.75, 1.25)), 2)

    for i in machinesList:
        i.lastprice = i.price
        i.price = round(i.price * (random.uniform(0.75, 1.25)), 2)

