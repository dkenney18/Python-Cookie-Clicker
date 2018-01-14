import time
import random
import string
import subprocess as sp
import json

global i
global total_money
global tax
global money
global rate
global x
global gem
global loaded
global boost_rate
loaded = False
rate = 0
money = 11
x = 0
gem = 0
i = 1
total_money = 0
tax = 0
boost_rate = 1


def invest():
    global tax
    global total_money
    global money
    tax = 0.48
    total_money = tax * money


class Clicker:
    def __init__(self, name):
        self.name = name
        self.price = 0
        self.clicks_per_second = 0
        self.rate = 0
        self.p = 0
        self.c = 0
        self.k = ""
        self.key = ""

    def cps(self, c):
        self.c = c
        self.clicks_per_second = self.c

    def cost(self, p):
        self.p = p
        self.price = self.p

    def set_rate(self):
        self.rate = self.clicks_per_second + self.rate

    def key_bind(self, k):
        self.k = k
        self.key = self.k

    def print_cps(self):
        print("clicks per second is: " + str(self.clicks_per_second))

    def print_prices(self):
        print("price = " + str(self.price))

    def print_name(self):
        print(self.name)

    def print_rate(self):
        print("your current rate is: " + str(self.rate))


clicker = Clicker("clicker")
grandma = Clicker("grandma")
auto_oven = Clicker("auto_oven")
factory = Clicker("factory")
mine = Clicker("mine")
epic = Clicker("epic")
portal = Clicker("portal")
airship = Clicker("airship")
carrier = Clicker("carrier")
###
clicker.cps(1)
grandma.cps(5)
auto_oven.cps(10)
factory.cps(15)
mine.cps(20)
epic.cps(25)
portal.cps(30)
airship.cps(35)
carrier.cps(40)
###
clicker.cost(10)
grandma.cost(50)
auto_oven.cost(100)
factory.cost(500)
mine.cost(1000)
epic.cost(1500)
portal.cost(2000)
airship.cost(3000)
carrier.cost(5000)
###
clicker.key_bind('1')
grandma.key_bind('2')
auto_oven.key_bind('3')
factory.key_bind('4')
mine.key_bind('5')
epic.key_bind('6')
portal.key_bind('7')
airship.key_bind('8')
carrier.key_bind('9')


def clear_screen():
    sp.call('cls', shell=True)


def find_time():
    global current_time
    current_time = time.time()/60/60/24/7/4/12


def create_uuid():
    global uuid
    global friendCode
    chars = string.ascii_letters + string.digits + string.octdigits + string.hexdigits
    uuid = "".join(random.choice(chars) for x in range(0, 26))
    chars = string.hexdigits
    friendCode = "".join(random.choice(chars) for x in range(0, 6))


def search():
    global found
    found = False
    #path to your name
    with open('C:\\Users\\yourname\\Desktop\\pythonGame\\users\\{0}.txt'.format("users"), 'r') as v:
        searchlines = v.readlines()
        for e in searchlines:
            if e.strip('\n') == save_name.strip('\n'):
                found = True
            print(e.strip('\n'))

        if found:
            print("name is already used")
        else:
            addfile()
            adduser()


def save_file():
    global save_name
    global irl_name
    global irl_middle_name
    global irl_last_name
    global score
    global age
    global date_of_birth
    global month
    global day
    global year
    global sec_question_1_answer
    global sec_question_2_answer
    global sec_question_3_answer
    global total_money
    global tax
    save_name = input("username: ")
    irl_name = input("First name: ").lower()
    irl_middle_name = input("Middle name: ").lower()
    irl_last_name = input("Last name: ").lower()
    age = input("Age: ")
    month, day, year = input("Date of birth(MM/DD/YYYY): ").split("/")
    sec_question_1_answer = input("Name of Dad?: ").lower()
    sec_question_2_answer = input("Name of Mom?: ").lower()
    sec_question_3_answer = input("Favorite Food?: ").lower()
    total_money = total_money
    tax = tax
    score = money * rate
    date_of_birth = month + "/" + day + "/" + year
    search()


def adduser():
    #path to your folder
    path_user = 'C:\\Users\\yourname\\Desktop\\pythonGame\\users\\{0}.txt'.format("users")
    with open(path_user, 'a') as y:
        y.write(save_name)
        y.write("\n")


def addfile():
    global save_name
    global irl_name
    global irl_middle_name
    global irl_last_name
    global score
    global age
    global friendCode
    global date_of_birth
    global sec_question_1_answer
    global sec_question_2_answer
    global sec_question_3_answer
    #path to your folder
    path = 'C:\\Users\\yourname\\Desktop\\pythonGame\\saves\\{0}.json'.format(save_name)
    create_uuid()
    find_time()
    data = {
        'username': save_name,
        'money': money,
        'rate': rate,
        'gem': gem,
        'save_id': uuid,
        'time_saved': current_time,
        'name': irl_name,
        'middle_name': irl_middle_name,
        'last_name': irl_last_name,
        'age': age,
        'date_of_birth': date_of_birth,
        'birth_month': month,
        'birth_day': day,
        'birth_year': year,
        'security_answer_1': sec_question_1_answer,
        'security_answer_2': sec_question_2_answer,
        'security_answer_3': sec_question_3_answer,
        'score': score,
        'friend_code': friendCode,
        'tax_rate': tax,
        'money_gained_by_taxes': total_money,
        ###
        'clicker_key_bind': clicker.key,
        'grandma_key_bind': grandma.key,
        'auto_oven_key_bind': auto_oven.key,
        'factory_key_bind': factory.key,
        'mine_key_bind': mine.key,
        'epic_key_bind': epic.key,
        'portal_key_bind': portal.key,
        'airship_key_bind': airship.key,
        'carrier_key_bind': carrier.key,
        ###
        'clicker_name': clicker.name,
        'grandma_name': grandma.name,
        'auto_oven_name': auto_oven.name,
        'factory_name': factory.name,
        'mine_name': mine.name,
        'epic_name': epic.name,
        'portal_name': portal.name,
        'airship_name': airship.name,
        'carrier_name': carrier.name,
        ###
        'clicker_price': clicker.price,
        'grandma_price': grandma.price,
        'auto_oven_price': auto_oven.price,
        'factory_price': factory.price,
        'mine_price': mine.price,
        'epic_price': epic.price,
        'portal_price': portal.price,
        'airship_price': airship.price,
        'carrier_price': carrier.price,
        ###
        'clicker_cps': clicker.clicks_per_second,
        'grandma_cps': grandma.clicks_per_second,
        'auto_oven_cps': auto_oven.clicks_per_second,
        'factory_cps': factory.clicks_per_second,
        'mine_cps': mine.clicks_per_second,
        'epic_cps': epic.clicks_per_second,
        'portal_cps': portal.clicks_per_second,
        'airship_cps': airship.clicks_per_second,
        'carrier_cps': carrier.clicks_per_second,

    }
    with open(path, 'w+') as f:
        json.dump(data, f)


def load_file():
    global money
    global tax
    global total_money
    global load_name
    global rate
    global name
    global gem
    global answer
    global friendCode
    global sec_1_ans
    global sec_2_ans
    global sec_3_ans
    global sec_1_ans_flag
    global sec_2_ans_flag
    global sec_3_ans_flag
    sec_1_ans_flag = False
    sec_2_ans_flag = False
    sec_3_ans_flag = False
    load_name = input("username: ")
    #path to the folder
    path_two = 'C:\\Users\\yourname\\Desktop\\pythonGame\\saves\\{0}.json'.format(load_name)
    with open(path_two, 'r') as g:
        u = json.load(g)
        sec_1_ans = u['security_answer_1']
        sec_2_ans = u['security_answer_2']
        sec_3_ans = u['security_answer_3']
        friendCode = u['friend_code']
    answer = input("name of father?")
    if answer == friendCode:
        with open(path_two, 'r') as f:
            j = json.load(f)
            money = j['money']
            rate = j['rate']
            name = str(j['username'])
            gem = j['gem']
            tax = j['tax_rate']
            print("your code is" + j['friend_code'])
            print("Loaded " + load_name + "'s file")

    if answer == sec_1_ans:
        sec_1_ans_flag = True
    elif answer != sec_1_ans:
        print("Fathers name was wrong.")
    answer = input("name of mother?")
    if answer == sec_2_ans:
        sec_2_ans_flag = True
    elif answer != sec_2_ans:
        print("Mothers name was wrong.")
    answer = input("name of favorite food?")
    if answer == sec_3_ans:
        sec_3_ans_flag = True
    elif answer != sec_3_ans:
        print("Favorite food was wrong")
    if sec_1_ans_flag and sec_2_ans_flag and sec_3_ans_flag:
        with open(path_two, 'r') as f:
            j = json.load(f)
            money = j['money']
            rate = j['rate']
            name = str(j['username'])
            gem = j['gem']
            tax = j['tax_rate']
            total_money = j['money_gained_by_taxes']
            ###
            clicker.key = j['clicker_key_bind']
            grandma.key = j['grandma_key_bind']
            auto_oven.key = j['auto_oven_key_bind']
            factory.key = j['factory_key_bind']
            mine.key = j['mine_key_bind']
            epic.key = j['epic_key_bind']
            portal.key = j['portal_key_bind']
            airship.key = j['airship_key_bind']
            carrier.key = j['carrier_key_bind']
            ###
            clicker.name = j['clicker_name']
            grandma.name = j['grandma_name']
            auto_oven.name = j['auto_oven_name']
            factory.name = j['factory_name']
            mine.name = j['mine_name']
            epic.name = j['epic_name']
            portal.name = j['portal_name']
            airship.name = j['airship_name']
            carrier.name = j['carrier_name']
            ###
            clicker.price = j['clicker_price']
            grandma.price = j['grandma_price']
            auto_oven.price = j['auto_oven_price']
            factory.price = j['factory_price']
            mine.price = j['mine_price']
            epic.price = j['epic_price']
            portal.price = j['portal_price']
            airship.price = j['airship_price']
            carrier.price = j['carrier_price']
            ###
            clicker.clicks_per_second = j['clicker_cps']
            grandma.clicks_per_second = j['grandma_cps']
            auto_oven.clicks_per_second = j['auto_oven_cps']
            factory.clicks_per_second = j['factory_cps']
            mine.clicks_per_second = j['mine_cps']
            epic.clicks_per_second = j['epic_cps']
            portal.clicks_per_second = j['portal_cps']
            airship.clicks_per_second = j['airship_cps']
            carrier.clicks_per_second = j['carrier_cps']
            print("Loaded " + load_name + "'s file")
    else:
        print("an answer was not right")


def ran():
    global x
    global gem
    x = random.randrange(0, 5)
    gem = gem
    if x == 1:
        gem = gem + 1


def sleep(t):
    time.sleep(t)


def buying(ans):
    global money
    global rate
    global x
    global gem
    global loaded
    global boost_rate
    gem = gem
    ran()
    rate = rate
    money = money
    if ans == clicker.key and money > clicker.price:
        print("you bought a " + str(clicker.name))
        clicker.cps(1)
        clicker.set_rate()
        rate = rate + clicker.clicks_per_second
        money = money - clicker.price
        loaded = True

    elif ans == grandma.key and money > grandma.price:
        print("you bought a " + str(grandma.name))
        grandma.cps(5)
        grandma.set_rate()
        rate = rate + grandma.clicks_per_second
        money = money - grandma.price
        loaded = True

    elif ans == auto_oven.key and money > auto_oven.price:
        print("you bought an auto_oven!")
        auto_oven.cps(10)
        auto_oven.set_rate()
        rate = rate + auto_oven.clicks_per_second
        money = money - auto_oven.price
        loaded = True

    elif ans == factory.key and money > factory.price:
        print("you bought a " + str(factory.name))
        factory.cps(15)
        factory.set_rate()
        rate = rate + factory.clicks_per_second
        money = money - factory.price
        loaded = True

    elif ans == mine.key and money > mine.price:
        print("you bought a " + str(mine.name))
        mine.cps(20)
        mine.set_rate()
        rate = rate + mine.clicks_per_second
        money = money - mine.price
        loaded = True

    elif ans == epic.key and money > epic.price:
        print("you bought an " + str(epic.name))
        epic.cps(25)
        epic.set_rate()
        rate = rate + epic.clicks_per_second
        money = money - epic.price
        loaded = True

    elif ans == portal.key and money > portal.price:
        print("you bought a " + str(portal.name))
        portal.cps(30)
        portal.set_rate()
        rate = rate + portal.clicks_per_second
        money = money - portal.price
        loaded = True

    elif ans == airship.key and money > airship.price:
        print("you bought a " + str(airship.name))
        airship.cps(35)
        airship.set_rate()
        rate = rate + airship.clicks_per_second
        money = money - airship.price
        loaded = True

    elif ans == carrier.key and money > carrier.price:
        print("you bought a " + str(carrier.name))
        carrier.cps(40)
        carrier.set_rate()
        rate = rate + carrier.clicks_per_second
        money = money - carrier.price
        loaded = True
    elif ans == 'rate':
        print("your rate is: " + str(rate))
        loaded = True
    elif ans == 'exit':
        quit()
        loaded = True
    elif ans == 'save':
        save_file()
        loaded = True
    elif ans == 'load':
        load_file()
        loaded = True
    elif ans == 'boost':
        b = input("how many seconds do you want to boost? ")
        if gem > int(b):
            print("boosting... ")
            money = money + (rate * int(b))
            gem = gem - int(b)
        else:
            print("you need more gems ")
    elif ans == 'upgrade':
        u = float(input("boost earnings by 0.01% per gem"))
        if gem > u:
            boost_rate = u * 0.01
            gem = gem - u
        else:
            print("you do not have enough gems")


while True:
    print("press " + str(clicker.key) + " to buy " + str(clicker.name) + " for $" + str(clicker.price) + "(+" + str(
        clicker.clicks_per_second) + "ps) ")
    print("press " + str(grandma.key) + " to buy " + str(grandma.name) + " for $" + str(grandma.price) + "(+" + str(
        grandma.clicks_per_second) + "ps) ")
    print("press " + str(auto_oven.key) + " to buy " + str(auto_oven.name) + " for $" + str(auto_oven.price) + "(+" +
          str(auto_oven.clicks_per_second) + "ps) ")
    print("press " + str(factory.key) + " to buy " + str(factory.name) + " for $" + str(factory.price) + "(+" + str(
        factory.clicks_per_second) + "ps) ")
    print("press " + str(mine.key) + " to buy " + str(mine.name) + " for $" + str(mine.price) + "(+" + str(
        mine.clicks_per_second) + "ps) ")
    print("press " + str(epic.key) + " to buy " + str(epic.name) + " for $" + str(epic.price) + "(+" + str(
        epic.clicks_per_second) + "ps) ")
    print("press " + str(portal.key) + " to buy " + str(portal.name) + " for $" + str(portal.price) + "(+" + str(
        portal.clicks_per_second) + "ps) ")
    print("press " + str(airship.key) + " to buy " + str(airship.name) + " for $" + str(airship.price) + "(+" + str(
        airship.clicks_per_second) + "ps) ")
    print("press " + str(carrier.key) + " to buy " + str(carrier.name) + " for $" + str(carrier.price) + "(+" + str(
        carrier.clicks_per_second) + "ps) ")
    print("money: $" + str(money))
    print("gems: " + str(gem))
    buying(input())
    if loaded:
        loaded = False
        clear_screen()
    else:
        money = money + rate
