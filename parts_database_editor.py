import re
#from pcpartpicker import API
import json

PCPP_PARTS_LIST = ['cpu',
                  'video-card',
                  'memory',
                  'motherboard',
                  'case',
                  'power-supply',
                  'ssd',
                  'hhd',
                  'monitor',
                  'cooler']

#Takes string, removes all spaces and special characters/returns all letters in uppercase
def simplify_string(part_name):
    part_name = part_name.upper()
    return re.sub("[ -().]", "", part_name)

class Cpu:
    def __init__(self):
        self.category = "cpu"

    def add_inputs(self):
        #Base info variables
        self.brand = str(input("Brand?  "))
        self.model = str(input("Model?  "))
        self.reference_name = simplify_string((self.brand + self.model))
        self.cores = int(input("Number of Cores?    "))
        self.threads = int(input("Number of Threads?    "))
        self.base_clock = float(input("Base clock speed?     "))
        self.boost_clock = float(input("Boost Clock speed?     "))
        #Extra info variables
        self.release_date = str(input("Release Quarter?  (Q* ****     "))
        self.benchmark_percentage = int(input("Benchmark percentage?    "))
        self.integrated_graphics = bool(input("Integrated Graphics? True or False   "))
        self.url = str(input("URL?     "))
        self.price = int(input("Price?     "))
        self.wattage = int(input("Wattage? TDP?      "))

class Gpu:
    def __init__(self):
        self.category = "gpu"

    def add_inputs(self):
        #Base info variables
        self.brand = str(input("Brand?  "))
        self.model = str(input("Model?  "))
        self.reference_name = simplify_string((self.brand + self.model))
        self.vram = int(input("Video Memory?    "))
        #Extra info variables
        self.benchmark = int(input("Benchmark %?     "))
        self.url = str(input("URL?  "))
        self.price = int(input("Price?      "))
        self.wattage = int(input("Wattage? TDP?     "))


class Ram:
    def __init__(self):
        self.category = "ram"

    def add_inputs(self):
        #Base info variables
        self.brand = str(input("Brand?    "))
        self.model = str(input("Model?    "))
        self.reference_name = simplify_string((self.brand + self.model))
        self.size = int(input("Size GB?     "))
        self.speed = int(input("Speed MHz?    "))
        #Extra info variables
        self.benchmark = int(input("Benchmark %?    "))
        self.url = str(input("Pcpartpicker Link?     "))
        self.price = int(input("Price?     "))


class Mobo:
    def __init__(self):
        self.category = "mobo"

    def add_inputs(self):
        #Base info Variables
        self.brand = str(input("Brand?    "))
        self.model = str(input("Model?     "))
        self.reference_name = simplify_string((self.brand + self.model))
        #Extra info Variables
        self.form_factor = str(input("Form factor?    "))
        self.url = str(input("Pcpartpicker Link?     "))
        self.price = int(input("Price?     "))

class Hdd:
    def __init__(self):
        self.category = "hdd"

    def add_inputs(self):
        #Base info variables
        self.brand = str(input("Brand?    "))
        self.model = str(input("Model?    "))
        self.reference_name = simplify_string((self.brand + self.model))
        self.size = int(input("Capacity? (GB)   "))
        #Extra info variables
        self.speed = int(input("Speed (MB/s)    "))
        self.price = int(input("Price?    "))
        self.benchmark = int(input("Benchmark %?   "))

class Ssd:
    def __init__(self):
        self.category = "ssd"

    def add_inputs(self):
        #Base info Variables
        self.brand = str(input("Brand?    "))
        self.model = str(input("Model?    "))
        self.reference_name = simplify_string((self.brand + self.model))
        self.size = int(input("Capacity? (GB)   "))
        #Extra info variables
        self.speed = int(input("Speed (MB/s)    "))
        self.price = int(input("Price?    "))
        self.benchmark = int(input("Benchmark %?   "))

class Psu:
    def __init__(self):
        self.category = "psu"

    def add_inputs(self):
        #Base info variables
        self.brand = str(input("Brand?    "))
        self.model = str(input("Model?    "))
        self.reference_name = simplify_string((self.brand + self.model))
        self.wattage = int(input("Wattage?   "))
        self.eff_rating = str(input("Efficiency rating?    "))
        #Extra info variables
        self.form_factor = str(input("Form Factor?    "))
        self.price = int(input("Price?    "))
        self.date = str(input("Date?     "))

class Monitor:
    def __init__(self):
        self.category = "monitor"

    def add_inputs(self):
        #Base info variables
        self.brand = str(input("Brand?    "))
        self.model = str(input("Model?    "))
        self.reference_name = simplify_string((self.brand + self.model))
        self.size = int(input("Size?     "))
        self.refresh = int(input("Refresh rate?     "))
        #Extra info variables
        self.type = str(input("Type?    "))
        self.price = int(input("Price?    "))
        self.date = str(input("Date?    "))

class Case:
    def __init__(self):
        self.category = "case"

    def add_inputs(self):
        #Base info variables
        self.brand = str(input("Brand?    "))
        self.model = str(input("Model?    "))
        self.reference_name = simplify_string((self.brand + self.model))
        #Extra info variables
        self.form_factor = str(input("Model?    "))
        self.price = int(input("Price?    "))

def append_part(part):

    if (part_exists()):
        print ("Duplicate found.")
        return
    with open("Data/main_data/" + part.category + "_data.json", "r") as database:
        part_list = json.load(database)
        database.close()
    part_list.append(part.__dict__)
    with open("Data/main_data/" + part.category + "_data.json", "w") as database:
        json.dump(part_list, database, indent=2)
    print("Append successful!")

def remove_part(part_name, part):

    part.reference_name = simplify_string(str(input("Enter part to remove (Brand + Model) \n")))
    if not (part_exists(part)):
        print ("Part not found.")
        return

    with open("Data/main_data/" + part.category + "_data.json", "r") as database:
        part_list = json.load(database)
        database.close()
    for each_part in part_list:
        if (each_part["reference_name"] == part.reference_name):
            part_list.remove(each_part)
    with open("Data/main_data/" + part_category + "_data.json", "w") as database:
        json.dump(part_list, database, indent=2)
    print("Remove successful!")


def part_exists(part):

    with open("Data/main_data/" + part.category + "_data.json", "r") as database:
        data_list = json.load(database)
        database.close()
    if (not data_list): #List cannot have duplicates if list is empty
        return False
    for each_part in data_list:
        if (part.reference_name == each_part["reference_name"]):
            print("Duplicate found.")
            return True
    #No such part = return False
    return False

def ask_for_category():

    category_dict = {0: None
                     1: Cpu(),
                     2: Gpu(),
                     3: Ram(),
                     4: Mobo(),
                     5: Ssd(),
                     6: Hdd(),
                     7: Psu(),
                     8: Case()}
    while True:
        print("Which part to add/remove? (input number above part | 0 to exit)?\n 1  |  2  |  3  |  4   |  5  |  6  |  7  |   8\nCPU | GPU | RAM | MOBO | SSD | HDD | PSU | CASE")
        try:
            category_index = int(input()) #Ask for user to input int between 0 and number of categories in database
            if (category_index > 8 or category_index < 0):
                raise ValueError #Raise ValueError if number inputted is not between 0 and number of categories in database
        except ValueError:
            print("Error: Enter an Integer within the options.")    #Specify valueerror, reiterate to try again
        except Exception as other_error:
            print(other_error)
            with open('Logs/parts_database_errors.log', 'a') as log:    #Write to logs if different error occurs
                log.write(str(datetime.now()) + ":  " + str(other_error) + "\n")
                log.close()
        else:
            return category_dict[category_index]


def manual_add_part():

    while True:
        new_part = ask_for_category() #Function to prompt user for input corresponding to category dict key
        if (new_part is None):  #pass and exit function if user inputs and function returns 0
            print("Exiting Manual Add.")
            return
        new_part.add_inputs()
        append_part(new_part)

def manual_remove_part():

    while True:
        part = ask_for_category()
        if (part is None): #pass and exit function if user inputs and function returns 0
            print("Exiting Manual Remove. \n")
            return
        remove_part(part)


def pvpp_name_convert(category):


    conversion_dict ={ "cpu": "cpu",
                     "gpu": "video-card",
                     "ram": "memory",
                     "mobo": "motherboard",
                     "ssd": "ssd",
                     "hhd": "hhd",
                     "psu": "power-supply",
                     "case": "case",
                     "monitor": "monitor"}

    return conversion_dict[category]

def pcpp_data_update():

    pcpp_api = API()

    for category in PCPP_PARTS_LIST:
        print("Retrieving " + category + " object...")
        data_object = pcpp_api.retrieve(category)
        print("Part object retrieved... \n creating JSON text")
        with open ("Data/PCPP/" + category + "_PCPP_Data.json", "w") as database:
            print("Creating/Writing text file...")
            data_json = json.dump(data_object, database, indent=2)
            print("Write successful for " + category + " category. \n")
    print("PcPartPicker Parts files updated")


def main_data_update():
    part = ask_for_category()
    with open("Data/Main/" + part.category + "_main_data", "w") as database:


def main():

    if (input == "Edit JSON Data"):
        manual_add_part()
        manual_remove_part()

main()