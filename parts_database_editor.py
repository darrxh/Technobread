import re
#from pcpartpicker import API
import json

#api = API()

"""
parts_list = ['cpu',
              'video-card',
              'memory',
              'motherboard',
              'case',
              'power-supply',
              'ssd',
              'hhd',
              'monitor',
              'cooler']
"""

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

#MODIFY TO CREATE CORRECT JSON FORMAT
def append_part(part):
    if (has_duplicates(part)):
        return
    with open("Data/main_data/" + part.category + "_data.json", "r") as database:
        part_list = json.load(database)
        database.close()
    part_list.append(part.__dict__)
    with open("Data/main_data/" + part.category + "_data.json", "w") as database:
        json.dump(part_list, database, indent=2)

    print("Append successful!")


#TEST THIS FUNCTION BUT FIX append_part FUNCTION FIRST
def has_duplicates(new_part):
    with open("Data/main_data/" + new_part.category + "_data.json", "r") as database:
        data_list = json.load(database)
        database.close()
    if (not data_list): #List cannot have duplicates if list is empty
        return False
    for each_part in data_list:
        if (new_part.reference_name == each_part["reference_name"]):
            print("Duplicate found.")
            return True
    #No duplicates = return False
    return False


def ask_for_category():
    while True:
        print("Which part to add(input number above part | 0 to exit)?\n 1  |  2  |  3  |  4   |  5  |  6  |  7  |   8\nCPU | GPU | RAM | MOBO | SSD | HDD | PSU | CASE")
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
            return category_index


def manual_add_part():

    category_dict = {1: Cpu(),
                     2: Gpu(),
                     3: Ram(),
                     4: Mobo(),
                     5: Ssd(),
                     6: Hdd(),
                     7: Psu(),
                     8: Case()}

    while True:
        category_key = ask_for_category() #Function to prompt user for input corresponding to category dict key
        if (category_key == 0):  #pass and exit function if user inputs and function returns 0
            print("Exiting Manual Add.")
            return
        new_part = category_dict[category_key] #create instance of corresponding parts
        new_part.add_inputs()
        append_part(new_part)



def threadripper_match(cpu_name):

    cpu_name = simplify_string(cpu_name)
    if ("THREADRIPPER" in cpu_name):
        model_number = cpu_name.replace("THREADRIPPER", "")
    elif ("RYZENTR" in cpu_name):
        model_number = cpu_name.replace("RYZENTR", "")

    cpu_name = "Ryzen Threadripper" + model_number
    return cpu_name
"""
def pcpp_data_update():

    for part in parts_list:
        print ("Retrieving " + part + " object...")
        part_object = api.retrieve(part)
        print ("Part object retrieved... \n creating JSON text"
        json_text = part_object.to_json()
        with open("Data/" + str(part) + "_Data_PCPP.json","w") as database:
            print ("Crea,ting/Writing text file...")
            database.writ,e(json_text + "\n")
            print ("Write ,successful")

    print ("PcPartPicker Parts files updated")

def ub_data_update():

    print ("coming soon")



def has_duplicates(list):
    for element in list:
        if (list.count(element) > 1):
            return True
    return False
"""

def common_part_counter():

    with open("Data/cpu_Data_PCPP.json","r") as pcpp_data:
        json_string_pcpp = pcpp_data.read()
        data_list_pcpp = json.loads(json_string_pcpp)
    with open("Data/cpu_Data_UB.json","r") as ub_data:
        json_string_ub = ub_data.read()
        data_list_ub = json.loads(json_string_ub)

    ub_list = []
    pcpp_list = []
    common_list = []
    ub_remainders_list = []
    pcpp_remainders_list = []

    for pcpp_index in data_list_pcpp:
        pcpp_list.append(str(pcpp_index['model']))
    for ub_index in data_list_ub:
        ub_list.append(str(ub_index['Model']))

    #Sort and remove duplicates
    ub_list.sort()
    pcpp_list.sort()
    ub_list = list(dict.fromkeys(ub_list))
    pcpp_list = list(dict.fromkeys(pcpp_list))


    print("Number of Elements in UB List:  " + str(len(ub_list)))
    print("Number of Elements in PCPP List:   " + str(len(pcpp_list)))

    for ub_index in ub_list:
        for pcpp_index in pcpp_list:
            if (ub_index.lower() == pcpp_index.lower()):
                common_list.append(str(ub_index))


    print (has_duplicates(common_list))

    print ("Elements in common: " + str(len(common_list)))

    with open("Data/common_cpu_list.txt","w") as common_cpu_list:
        for part in common_list:
            common_cpu_list.write(str(part) + "\n")


    for pcpp_index in pcpp_list:
        is_different = True
        for common_index in common_list:
            if (common_index == pcpp_index):
                is_different = False
        if (is_different):
            pcpp_remainders_list.append(pcpp_index)

    for ub_index in ub_list:
        is_different = True
        for common_index in common_list:
            if (common_index == ub_index):
                is_different = False
        if (is_different):
            ub_remainders_list.append(ub_index)



    print ("Remaining elements in UB file:  " + str(len(ub_remainders_list)))
    with open ("Data/remainders_ub.txt", "w") as remainders_ub:
        for part in ub_remainders_list:
            remainders_ub.write(str(part) + "\n")

    print ("Remaining elements in PCPP file: " + str(len(pcpp_remainders_list)))
    with open("Data/remainders_pcpp.txt", "w") as remainders_pcpp:
        for part in pcpp_remainders_list:
            remainders_pcpp.write(str(part) + "\n")



def main():
    manual_add_part()

main()
