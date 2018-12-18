#All imports are used as follows:
#import time is used to create the sleep() function as well as to create the save time
#random deals with code gen and gem gen
#string is for code gen
# subprocess as sp is for device spicifc screen clear
#json is is for file save and read
#os is for creating file structres 
#imaplib is for the email and sms interactions
#sys is not used at the moment
#datetime is not used at the moment
#email is used to read emails and do a function based on contents
#mailbox is used with email and imaplib to select a mailbox to use
# from imapclient import IMAPClient is used in the SMS valadation to wait for a user to input a phone number
import time
import random
import string
import subprocess as sp
import json
import os
import imaplib
import sys
import datetime
import email
import mailbox
import smtplib
from imapclient import IMAPClient
#all globals are defined here so as to be used in functions and definations
global i
global total_money
global tax
global money
global rate
global x
global gem
global loaded
global boost_rate
global count
global HOST
global text_input
global actavation_code
global username
global password
global sender
global valadated
global text_input
global phonenumber
global service_provider
global phone_number
global one_time_setup
global email_sender
one_time_setup = False
valadated = False
loaded = False
rate = 0
money = 11
x = 0
gem = 0
i = 1
total_money = 0
tax = 0
boost_rate = 1
count = 0
name = "guest"
#this section below marks the beginning set up of the file structer
file_path = os.getcwd() + "/pythonGame/users/"
directory = os.path.dirname(file_path)
if not os.path.exists(directory):
    os.makedirs(directory)
file = os.getcwd() + "/pythonGame/users/users.txt"
fptr = open(file, "w")
file_path = os.getcwd() + "/pythonGame/saves/"
directory = os.path.dirname(file_path)
if not os.path.exists(directory):
    os.makedirs(directory)
#---The SMS inteaction section---#
#below is to setup the varaiables needed to run the SMS inteaction. 
def SMS_setup():
    global HOST
    global text_input
    global actavation_code
    global username
    global password
    global sender
    global valadated
    global text_input
    global phonenumber
    global service_provider
    global phone_number
    global one_time_setup
    global email_sender
    HOST = ''
    text = "somthing more"
    email_username = input("email adress for account you want to use: ")
    email_password = input("the password to your emaiul account: ")
    phone_number = input("phone number (must be able to send and recieve texts): ") 
    service_provider = ""
    phonenumber = ''
    actavation_code = ""
    text_input = ""
    username = email_username
    password =  email_password
    email_sender = ""
    z = input("who provides you email? enter (1)gmail\n(2)microsoft ")
    if z == "1":
        email_provider = 'gmail'
        HOST = 'imap.' + email_provider + '.com'
        server = smtplib.SMTP( "smtp." + email_provider + ".com", 587 )
        mail = imaplib.IMAP4_SSL(HOST)
        server = smtplib.SMTP( HOST, 587 )
    elif z == "2":
        email_provider = 'outlook'
        HOST = 'imap.' + email_provider + '.com'
        server = smtplib.SMTP( "smtp." + email_provider + ".com", 587 )
        mail = imaplib.IMAP4_SSL(HOST)
        server = smtplib.SMTP( HOST, 587 )
    else:
        print("Unrecognized email provider.")
    zz = input("phone service provider enter (1)verizon\n(2)sprint\n(3)t-moible\n(4)AT&T")
    if zz == "1":
        phonenumber = phone_number + '@' + 'vtext.com'
        email_sender = phone_number + '@'  + 'vzwpix.com'
        sender = email_sender
    elif zz == "2":
        phonenumber = phone_number + '@' + 'messaging.sprintpcs.com'
        email_sender = phone_number + '@' + 'pm.sprint.com'
        sender = email_sender
    elif zz == "3":
        phonenumber = phone_number + '@' + 'tmomail.net'
        email_sender = phone_number + '@' + 'tmomail.net'
        sender = email_sender
    elif zz == "4":
        phonenumber = phone_number + '@' + 'txt.att.net'
        email_sender = phone_number + '@' + 'mms.att.net4 '
        sender = email_sender
# below is to valadate phone numbers

def validate_phone_number():
    def send_SMS(SMS_message):
        server = smtplib.SMTP(HOST, 587)
        server.starttls()
        server.login( username, password )
        server.sendmail( 'message', phonenumber, SMS_message)
    def readEmail():
        mail = imaplib.IMAP4_SSL(HOST)
        server = smtplib.SMTP( HOST, 587 )
        mail.login(username, password)
        mail.list()
        mail.select('inbox')
        result, data = mail.uid('search', None, "UNSEEN") # (ALL/UNSEEN)
        i = len(data[0].split())
        for x in range(i):
                latest_email_uid = data[0].split()[x]
                result, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')
                # result, email_data = conn.store(num,'-FLAGS','\\Seen') 
                # this might work to set flag to seen, if it doesn't already
                raw_email = email_data[0][1]
                raw_email_string = raw_email.decode('utf-8')
                email_message = email.message_from_string(raw_email_string)
                # Body details
                for part in email_message.walk():
                    if part.get_content_type() == "text/plain":
                        body = part.get_payload(decode=True)
                        text_input = str(body.decode('utf-8'))
                        print(text_input)
                        if text_input == actavation_code:
                            print("good")
                            valadated = True
                            server.starttls()
                            server.login( username, password )
                            server.sendmail( 'message', phonenumber, str(phonenumber) + " is actavated")
                        else:
                            print("problem")
                    else:
                        continue
    def deleteEmails():
        sender = email_sender
        mail = imaplib.IMAP4_SSL(HOST)
        connection_message = mail.login(username, password)
        print(connection_message)
        mail.select("inbox")

        print("Searching emails from {0}".format(sender))
        result_status, email_ids = mail.search(None, '(FROM "{0}")'.format(sender))
        email_ids = email_ids[0].split()

        if len(email_ids) == 0:
            print("No emails found, finishing...")

        else:
            print("%d emails found, sending to trash folder..." % len(email_ids))
            mail.store('1:*', '+X-GM-LABELS', '\\Trash')
            mail.expunge()

        print("Done!")
    chars = string.hexdigits
    actavation_code = "".join(random.choice(chars) for x in range(0, 6))
    send_SMS("reply code to actavate number " + str(actavation_code))
    server_alert = IMAPClient(HOST)
    server_alert.login(username, password)
    server_alert.select_folder('INBOX')
    server_alert.idle()
    print("Connection is now in IDLE mode, send yourself an email or quit with ^c")

    while True:
        try:
            # Wait for up to 30 seconds for an IDLE response
            responses = server_alert.idle_check(timeout=30)
            if responses:
                readEmail()
                deleteEmails()
                return False
            else:
                print("nothing")
        except KeyboardInterrupt:
            break
# in this defination emailcode() you can put code to be run when a word or number or such is texted.
def SMS_execute_code():
    global text_input
    global money
    global rate
    money = money
    def readEmail():
        global money
        global rate
        mail = imaplib.IMAP4_SSL(HOST)
        mail.login(username, password)
        mail.list()
        mail.select('inbox')
        result, data = mail.uid('search', None, "UNSEEN") # (ALL/UNSEEN)
        i = len(data[0].split())
        for x in range(i):
                latest_email_uid = data[0].split()[x]
                result, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')
                # result, email_data = conn.store(num,'-FLAGS','\\Seen') 
                # this might work to set flag to seen, if it doesn't already
                raw_email = email_data[0][1]
                raw_email_string = raw_email.decode('utf-8')
                email_message = email.message_from_string(raw_email_string)
                # Body details
                for part in email_message.walk():
                    if part.get_content_type() == "text/plain":
                        body = part.get_payload(decode=True)
                        text_input = str(body.decode('utf-8').strip())
                        print(text_input)
                       
                        input_command = text_input.lower()
                        command, what_item, number_of_item = input_command.split(" ")
                        command = {"command": command, "item": what_item, "number": number_of_item}
                        print("parts: command:'{command}', what_item:'{item}', number_of_item: '{number}'".format(**command))
                        commands = ["/buy", "/sell"]
                        items_prices = [clicker.price, grandma.price, auto_oven.price, factory.price, mine.price, epic.price, portal.price, airship.price, carrier.price]
                        if command['command'] == commands[0]:
                            if command['item'] == clicker.name:
                                #working exapmle for the rest of them below is the logic to buy an item
                                if command['item'] == clicker.name and int(money) > int(command['number']) * int(clicker.price):
                                    print("you bought: " + str(clicker.name))
                                    clicker.cps(clicker.clicks_per_second)
                                    clicker.set_rate()
                                    rate = rate + (clicker.clicks_per_second * int(command['number']))
                                    money = int(money) - (int(clicker.price) * int(command['number']))
                                    clicker.num_bought = clicker.num_bought +  int(command['number'])
                                    print("number bought:{number}".format(**command))
                                    loaded = True
                                else:
                                    print("not enough")
                                    continue
                            elif command['item'] == grandma.name:
                                if command['item'] == grandma.name and int(money) > int(command['number']) * int(grandma.price):
                                    print("you bought a " + str(grandma.name))
                                    grandma.cps(grandma.clicks_per_second)
                                    grandma.set_rate()
                                    rate = rate + (grandma.clicks_per_second * int(command['number']))
                                    money = int(money) - (int(grandma.price) * int(command['number']))
                                    grandma.num_bought = grandma.num_bought +  int(command['number'])
                                    print("number bought:{number}".format(**command))
                                    loaded = True
                                else:
                                    print("not enough")
                                    continue
                            elif command['item'] == auto_oven.name:
                                if command['item'] == auto_oven.name and int(money) > int(ommand['number']) * int(auto_oven.price):
                                    print("you bought a " + str(auto_oven.name))
                                    auto_oven.cps(auto_oven.clicks_per_second)
                                    auto_oven.set_rate()
                                    rate = rate + (auto_oven.clicks_per_second * int(command['number']))
                                    money = int(money) - (int(auto_oven.price) * int(command['number']))
                                    auto_oven.num_bought = auto_oven.num_bought +  int(command['number'])
                                    print("number bought:{number}".format(**command))
                                    loaded = True
                                else:
                                    print("not enough")
                                    continue
                            elif command['item'] == factory.name:
                                if command['item'] == factory.name and int(money) > int(command['number']) * int(factory.price):
                                    print("you bought a " + str(factory.name))
                                    factory.cps(factory.clicks_per_second)
                                    factory.set_rate()
                                    rate = rate + (factory.clicks_per_second * int(command['number']))
                                    money = int(money) - (int(factory.price) * int(command['number']))
                                    factory.num_bought = factory.num_bought +  int(command['number'])
                                    print("number bought:{number}".format(**command))
                                    loaded = True
                                else:
                                    print("not enough")
                                    continue
                            elif command['item'] == mine.name:
                                if command['item'] == mine.name and int(money) > int(command['number']) * int(mine.price):
                                    print("you bought a " + str(mine.name))
                                    mine.cps(mine.clicks_per_second)
                                    mine.set_rate()
                                    rate = rate + (mine.clicks_per_second * int(command['number']))
                                    money = int(money) - (int(mine.price) * int(command['number']))
                                    mine.num_bought = mine.num_bought +  int(command['number'])
                                    print("number bought:{number}".format(**command))
                                    loaded = True
                                else:
                                    print("not enough")
                                    continue
                            elif command['item'] == epic.name:
                                if command['item'] == epic.name and int(money) > int(command['number']) * int(epic.price):
                                    print("you bought a " + str(epic.name))
                                    epic.cps(epic.clicks_per_second)
                                    epic.set_rate()
                                    rate = rate + (epic.clicks_per_second * int(command['number']))
                                    money = int(money) - (int(epic.price) * int(command['number']))
                                    epic.num_bought = epic.num_bought +  int(command['number'])
                                    print("number bought:{number}".format(**command))
                                    loaded = True
                                else:
                                    print("not enough")
                                    continue
                            elif command['item'] == portal.name:
                                if command['item'] == portal.name and int(money) > int(command['number']) * int(portal.price):
                                    print("you bought a " + str(portal.name))
                                    portal.cps(portal.clicks_per_second)
                                    portal.set_rate()
                                    rate = rate + (portal.clicks_per_second * int(command['number']))
                                    money = int(money) - (int(portal.price) * int(command['number']))
                                    portal.num_bought = portal.num_bought +  int(command['number'])
                                    print("number bought:{number}".format(**command))
                                    loaded = True
                                else:
                                    print("not enough")
                                    continue
                            elif command['item'] == airship.name:
                                if command['item'] == airship.name and int(money) > int(command['number']) * int(airship.price):
                                    print("you bought a " + str(airship.name))
                                    airship.cps(airship.clicks_per_second)
                                    airship.set_rate()
                                    rate = rate + (airship.clicks_per_second * int(command['number']))
                                    money = int(money) - (int(airship.price) * int(command['number']))
                                    airship.num_bought = airship.num_bought +  int(command['number'])
                                    print("number bought:{number}".format(**command))
                                    loaded = True
                                else:
                                    print("not enough")
                                    continue
                            elif command['item'] == carrier.name:
                                if command['item'] == carrier.name and int(money) > int(command['number']) * int(carrier.price):
                                    print("you bought a " + str(carrier.name))
                                    carrier.cps(carrier.clicks_per_second)
                                    carrier.set_rate()
                                    rate = rate + (carrier.clicks_per_second * int(command['number']))
                                    money = int(money) - (int(carrier.price) * int(command['number']))
                                    carrier.num_bought = carrier.num_bought +  int(command['number'])
                                    print("number bought:{number}".format(**command))
                                    loaded = True
                                else: 
                                    print("not enough")
                                    continue
                            else:
                                print("could not find that name")
                                continue
                        if command['command'] == commands[1]:
                                if command['item'] == clicker.name:
                                    if int(command['number']) <= int(clicker.num_bought):
                                        money = money + int(command['number']) * int(clicker.price)
                                        clicker.num_bought = clicker.num_bought - int(command['number'])
                                        rate = rate - (clicker.clicks_per_second * int(command['number']))
                                        loaded = True
                                    else:
                                        print("too many items") 
                                        continue
                                    print("number sold:{number}".format(**command))
                                elif command['item'] == grandma.name:
                                    if int(command['number']) <= int(grandma.num_bought):
                                        money = int(command['number']) * int(grandma.price)
                                        grandma.num_bought = grandma.num_bought - int(command['number'])
                                        rate = rate - (grandma.clicks_per_second * int(command['number']))
                                        loaded = True
                                    else:
                                        print("too many items") 
                                        continue
                                    print("number sold:{number}".format(**command))
                                elif command['item'] == auto_oven.name:
                                    if int(command['number']) <= int(auto_oven.num_bought):
                                        money = int(command['number']) * int(auto_oven.price)
                                        auto_oven.num_bought = auto_oven.num_bought - int(command['number'])
                                        rate = rate - (auto_oven.clicks_per_second * int(command['number']))
                                        loaded = True
                                    else:
                                        print("too many items") 
                                        continue
                                    print("number sold:{number}".format(**command))
                                elif command['item'] == factory.name:
                                    if int(command['number']) <= int(factory.num_bought):
                                        money = int(command['number']) * int(factory.price)
                                        factory.num_bought = factory.num_bought - int(command['number'])
                                        rate = rate - (factory.clicks_per_second * int(command['number']))
                                        loaded = True
                                    else:
                                        print("too many items") 
                                        continue
                                    print("number sold:{number}".format(**command))
                                elif command['item'] == mine.name:
                                    if int(command['number']) <= int(mine.num_bought):
                                        money = int(command['number']) * int(mine.price)
                                        mine.num_bought = mine.num_bought - int(command['number'])
                                        rate = rate - (mine.clicks_per_second * int(command['number']))
                                        loaded = True
                                    else:
                                        print("too many items") 
                                        continue
                                    print("number sold:{number}".format(**command))
                                elif command['item'] == epic.name:
                                    if int(command['number']) <= int(epic.num_bought):
                                        money = int(command['number']) * int(epic.price)
                                        epic.num_bought = epic.num_bought - int(command['number'])
                                        rate = rate - (epic.clicks_per_second * int(command['number']))
                                        loaded = True
                                    else:
                                        print("too many items") 
                                        continue
                                    print("number sold:{number}".format(**command))
                                elif command['item'] == portal.name:
                                    if int(command['number']) <= int(portal.num_bought):
                                        money = int(command['number']) * int(portal.price)
                                        portal.num_bought = portal.num_bought - int(command['number'])
                                        rate = rate - (portal.clicks_per_second * int(command['number']))
                                        loaded = True
                                    else:
                                        print("too many items") 
                                        continue
                                    print("number sold:{number}".format(**command))
                                elif command['item'] == airship.name:
                                    if int(command['number']) <= int(airship.num_bought):
                                        money = int(command['number']) * int(airship.price)
                                        airship.num_bought = airship.num_bought - int(command['number'])
                                        rate = rate - (airship.clicks_per_second * int(command['number']))
                                        loaded = True
                                    else:
                                        print("too many items")
                                        continue 
                                    print("number sold:{number}".format(**command))
                                elif command['item'] == carrier.name:
                                    if int(command['number']) <= int(carrier.num_bought):
                                        money = int(command['number']) * int(carrier.price)
                                        carrier.num_bought = carrier.num_bought - int(command['number'])
                                        rate = rate - (carrier.clicks_per_second * int(command['number']))
                                        loaded = True
                                    else:
                                        print("too many items")
                                        continue 
                                    print("number sold:{number}".format(**command))
                                else:
                                    print("could not find that name to sell")
                                    continue
    def deleteEmails():
        mail = imaplib.IMAP4_SSL(HOST)
        connection_message = mail.login(username, password)
        print(connection_message)
        mail.select("inbox")

        print("Searching emails from {0}".format(sender))
        result_status, email_ids = mail.search(None, '(FROM "{0}")'.format(sender))
        email_ids = email_ids[0].split()

        if len(email_ids) == 0:
            print("No emails found, finishing...")

        else:
            print("%d emails found, sending to trash folder..." % len(email_ids))
            mail.store('1:*', '+X-GM-LABELS', '\\Trash')
            mail.expunge()

        print("Done!")
        loaded = True
    server_alert = IMAPClient(HOST)
    server_alert.login(username, password)
    server_alert.select_folder('INBOX')
    server_alert.idle()
    print("Connection is now in IDLE mode, send yourself an email or quit with ^c")
    print("commands are like so '/COMMAND NAME optional number' example is /BUY clicker 10")

    while True:
        try:
            # Wait for up to 30 seconds for an IDLE response
            responses = server_alert.idle_check(timeout=30)
            if responses:
                loaded = True
                readEmail()
                deleteEmails()
                return False
            else:
                print("nothing")
        except KeyboardInterrupt:
            break

    server.idle_done()
    print("\nIDLE mode done")
    server.logout()


##############################################

# a non working investment idea
def invest():
    global tax
    global total_money
    global money
    tax = 1.30
    total_money = tax * money
    money = total_money - money

# an attemnt to create user interactivity
def good_sayings():
    sayings = ["good choice {0}".format(name), "Is there no end to {0}'s choices?".format(name),
               "only less then what {0} wants".format(name),
               "a good thing {0} can wait".format(name),
               "{0} likes this".format(name), "you are awesome {0}".format(name), "{0} buys great things".format(name)]
    print(sayings[random.randrange(0, len(sayings))])

# the heart of the program the clicker class
class Clicker:
    def __init__(self, name):
        #defining the varaibles used in the class
        self.name = name
        self.price = 0
        self.clicks_per_second = 0
        self.rate = 0
        self.p = 0
        self.c = 0
        self.k = ""
        self.key = ""
        self.num_bought = 0
        self.nb = 0
        self.num_b = 0

    def cps(self, c):
        #the amount that the rate is rased by
        self.c = c
        self.clicks_per_second = self.c

    def cost(self, p):
        #the cost of the clicker object
        self.p = p
        self.price = self.p

    def set_rate(self):
        #seting the rate 
        self.rate = self.clicks_per_second + self.rate

    def key_bind(self, k):
        #custom keybinding 
        self.k = k
        self.key = self.k

    def print_cps(self):
        #to print the clickes per second
        print("clicks per second is: " + str(self.clicks_per_second))

    def print_prices(self):
        #to pring the prices
        print("price = " + str(self.price))

    def print_name(self):
        #to print the name
        print(self.name)

    def print_rate(self):
        #to print the current rate
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
###

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
    with open(os.getcwd() + '\\pythonGame\\users\\{0}.txt'.format("users"), 'r') as v:
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
    path_user = os.getcwd() + '\\pythonGame\\users\\{0}.txt'.format("users")
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
    global HOST
    global text_input
    global actavation_code
    global username
    global password
    global sender
    global valadated
    global text_input
    global phonenumber
    global service_provider
    global phone_number
    global one_time_setup
    global email_sender
    path = os.getcwd() + '\\pythonGame\\saves\\{0}.json'.format(save_name)
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
        'email_username': username,
        'email_password': password,
        'sender': sender,
        'host':HOST,
        'service_provider': service_provider,
        'email_phone_number': phonenumber,
        'real_phone_number': phone_number,

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
        ###
        'clicker_num_bought': clicker.num_bought,
        'grandma_num_bought': grandma.num_bought,
        'auto_oven_num_bought': auto_oven.num_bought,
        'factory_num_bought': factory.num_bought,
        'mine_num_bought': mine.num_bought,
        'epic_num_bought': epic.num_bought,
        'portal_num_bought': portal.num_bought,
        'airship_num_bought': airship.num_bought,
        'carrier_num_bought': carrier.num_bought,

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
    global user_name
    global HOST
    global text_input
    global actavation_code
    global username
    global password
    global sender
    global valadated
    global text_input
    global phonenumber
    global service_provider
    global phone_number
    global one_time_setup
    global email_sender
    sec_1_ans_flag = False
    sec_2_ans_flag = False
    sec_3_ans_flag = False
    load_name = input("username: ")
    path_two = os.getcwd() + '\\pythonGame\\saves\\{0}.json'.format(load_name)
    with open(path_two, 'r') as g:
        u = json.load(g)
        sec_1_ans = u['security_answer_1']
        sec_2_ans = u['security_answer_2']
        sec_3_ans = u['security_answer_3']
        friendCode = u['friend_code']
        user_name = u['name']
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
            HOST = j['host']
            username = j['email_username']
            password = j['email_password']
            phone_number = j['real_phone_number']
            service_provider = j['service_provider']
            phonenumber = j['email_phone_number']
            sender = j['sender']

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
            ###
            clicker.num_bought = j['clicker_num_bought']
            grandma.num_bought = j['grandma_num_bought']
            mine.num_bought = j['mine_num_bought']
            epic.num_bought = j['epic_num_bought']
            portal.num_bought = j['portal_num_bought']
            airship.num_bought = j['airship_num_bought']
            carrier.num_bought = j['carrier_num_bought']
            ###
            print("Loaded " + load_name + "'s file")
            sleep(1)
            print("Hello " + user_name + "!")
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


def change_key_bindings():
    global answer
    answer = input("name of clicker you want to change. choices are \n" + clicker.name + "\n" + grandma.name + "\n"
                   + auto_oven.name + "\n" + factory.name + "\n" + mine.name + "\n" + epic.name + "\n" + portal.name
                   + "\n" + airship.name + "\n" + carrier.name + "\nremember caps in a name  is important").strip()
    if answer == clicker.name:
        clicker.key = input("new key: ")
    elif answer == grandma.name:
        grandma.key = input("new key: ")
    elif answer == auto_oven.name:
        auto_oven.key = input("new key: ")
    elif answer == factory.name:
        factory.key = input("new key: ")
    elif answer == mine.name:
        mine.key = input("new key: ")
    elif answer == epic.name:
        epic.key = input("new key: ")
    elif answer == portal.name:
        portal.key = input("new key: ")
    elif answer == airship.name:
        airship.key = input("new key: ")
    elif answer == carrier.name:
        carrier.key = input("new key: ")
    else:
        print("try again name not found")


def change_name():
    global answer
    answer = input("name of clicker you want to change. choices are \n" + clicker.name + "\n" + grandma.name + "\n"
                   + auto_oven.name + "\n" + factory.name + "\n" + mine.name + "\n" + epic.name + "\n" + portal.name
                   + "\n" + airship.name + "\n" + carrier.name + "\nremember caps in a name  is important").strip()
    if answer == clicker.name:
        clicker.name = input("new name: ")
    elif answer == grandma.name:
        grandma.name = input("new name: ")
    elif answer == auto_oven.name:
        auto_oven.name = input("new name: ")
    elif answer == factory.name:
        factory.name = input("new name: ")
    elif answer == mine.name:
        mine.name = input("new name: ")
    elif answer == epic.name:
        epic.name = input("new name: ")
    elif answer == portal.name:
        portal.name = input("new name: ")
    elif answer == airship.name:
        airship.name = input("new name: ")
    elif answer == carrier.name:
        carrier.name = input("new name: ")
    else:
        print("try again name not found")


def change_price():
    global answer
    answer = input("name of clicker you want to change. choices are \n" + clicker.name + "\n" + grandma.name + "\n"
                   + auto_oven.name + "\n" + factory.name + "\n" + mine.name + "\n" + epic.name + "\n" + portal.name
                   + "\n" + airship.name + "\n" + carrier.name + "\nremember caps in a name  is important").strip()
    if answer == clicker.name:
        clicker.price = int(input("new price: "))
    elif answer == grandma.name:
        grandma.price = int(input("new price: "))
    elif answer == auto_oven.name:
        auto_oven.price = int(input("new price: "))
    elif answer == factory.name:
        factory.price = int(input("new price: "))
    elif answer == mine.name:
        mine.price = int(input("new price: "))
    elif answer == epic.name:
        epic.price = int(input("new price: "))
    elif answer == portal.name:
        portal.price = int(input("new price: "))
    elif answer == airship.name:
        airship.price = int(input("new price: "))
    elif answer == carrier.name:
        carrier.price = int(input("new price: "))
    else:
        print("try again name not found")


def change_cps():
    global answer
    answer = input("name of clicker you want to change. choices are \n" + clicker.name + "\n" + grandma.name + "\n"
                   + auto_oven.name + "\n" + factory.name + "\n" + mine.name + "\n" + epic.name + "\n" + portal.name
                   + "\n" + airship.name + "\n" + carrier.name + "\nremember caps in a name  is important").strip()
    if answer == clicker.name:
        clicker.clicks_per_second = int(input("new clicks per sec: "))
    elif answer == grandma.name:
        grandma.clicks_per_second = int(input("new clicks per sec: "))
    elif answer == auto_oven.name:
        auto_oven.clicks_per_second = int(input("new clicks per sec: "))
    elif answer == factory.name:
        factory.clicks_per_second = int(input("new clicks per sec: "))
    elif answer == mine.name:
        mine.clicks_per_second = int(input("new clicks per sec: "))
    elif answer == epic.name:
        epic.clicks_per_second = int(input("new clicks per sec: "))
    elif answer == portal.name:
        portal.clicks_per_second = int(input("new clicks per sec: "))
    elif answer == airship.name:
        airship.clicks_per_second = int(input("new clicks per sec: "))
    elif answer == carrier.name:
        carrier.clicks_per_second = int(input("new clicks per sec: "))
    else:
        print("try again name not found")
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
        clicker.cps(clicker.clicks_per_second)
        clicker.set_rate()
        rate = rate + clicker.clicks_per_second
        money = money - clicker.price
        clicker.num_bought = clicker.num_bought + 1
        loaded = True

    elif ans == grandma.key and money > grandma.price:
        print("you bought a " + str(grandma.name))
        grandma.cps(grandma.clicks_per_second)
        grandma.set_rate()
        rate = rate + grandma.clicks_per_second
        money = money - grandma.price
        grandma.num_bought = grandma.num_bought + 1
        loaded = True

    elif ans == auto_oven.key and money > auto_oven.price:
        print("you bought an auto_oven!")
        auto_oven.cps(auto_oven.clicks_per_second)
        auto_oven.set_rate()
        rate = rate + auto_oven.clicks_per_second
        money = money - auto_oven.price
        auto_oven.num_bought = auto_oven.num_bought + 1
        loaded = True

    elif ans == factory.key and money > factory.price:
        print("you bought a " + str(factory.name))
        factory.cps(factory.clicks_per_second)
        factory.set_rate()
        rate = rate + factory.clicks_per_second
        money = money - factory.price
        factory.num_bought = factory.num_bought + 1
        loaded = True

    elif ans == mine.key and money > mine.price:
        print("you bought a " + str(mine.name))
        mine.cps(mine.clicks_per_second)
        mine.set_rate()
        rate = rate + mine.clicks_per_second
        money = money - mine.price
        mine.num_bought = mine.num_bought + 1
        loaded = True

    elif ans == epic.key and money > epic.price:
        print("you bought an " + str(epic.name))
        epic.cps(epic.clicks_per_second)
        epic.set_rate()
        rate = rate + epic.clicks_per_second
        money = money - epic.price
        epic.num_bought = epic.num_bought + 1
        loaded = True

    elif ans == portal.key and money > portal.price:
        print("you bought a " + str(portal.name))
        portal.cps(portal.clicks_per_second)
        portal.set_rate()
        rate = rate + portal.clicks_per_second
        money = money - portal.price
        portal.num_bought = portal.num_bought + 1
        loaded = True

    elif ans == airship.key and money > airship.price:
        print("you bought a " + str(airship.name))
        airship.cps(airship.clicks_per_second)
        airship.set_rate()
        rate = rate + airship.clicks_per_second
        money = money - airship.price
        airship.num_bought = airship.num_bought + 1
        loaded = True

    elif ans == carrier.key and money > carrier.price:
        print("you bought a " + str(carrier.name))
        carrier.cps(carrier.clicks_per_second)
        carrier.set_rate()
        rate = rate + carrier.clicks_per_second
        money = money - carrier.price
        carrier.num_bought = carrier.num_bought + 1
        loaded = True

    elif ans == 'change keys':
        change_key_bindings()

    elif ans == 'change name':
        change_name()

    elif ans == 'change price':
        change_price()

    elif ans == 'change cps':
        change_cps()

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

    elif ans == "numbers":
        print(clicker.num_bought)
        print(grandma.num_bought)
        print(auto_oven.num_bought)
        print(factory.num_bought)
        print(mine.num_bought)
        print(epic.num_bought)
        print(portal.num_bought)
        print(airship.num_bought)
        print(carrier.num_bought)
        loaded = True
    elif ans == 'boost':
        b = input("how many seconds do you want to boost? ")
        if gem > int(b):
            print("boosting... ")
            money = money + (rate * int(b))
            gem = gem - int(b)
        else:
            print("you need more gems ")
    elif ans == 'convert':
        u = float(input("boost earnings by 0.01% per gem"))
        if gem > u:
            boost_rate = u * 0.01
            gem = gem - u
        else:
            print("you do not have enough gems")
    elif ans == 'SMS_setup':
        SMS_setup()
        validate_phone_number()
    elif ans == 'SMS_code':
        SMS_execute_code()

while True:
###############################################
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
    sleep(1)
    if loaded:
        loaded = False
        clear_screen()
    else:
        money = money + rate