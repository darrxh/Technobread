from datetime import datetime
import json


class Cpu:
    def __init__(self):
        #Base info variables
        self.brand ="N/A"
        self.model ="N/A"
        self.cores ="N/A"
        self.threads ="N/A"
        self.base_clock ="N/A"
        self.boost_clock = "N/A"
        #Extra info variables
        self.release_date ="N/A"
        self.benchmark_percentage ="N/A"
        self.rank ="N/A"
        self.integrated_graphics = "N/A"
        self.url = "N/A"
        self.price = "N/A"
        self.wattage = "N/A"


    def add_cpu(self):

        self.brand = str(input("Brand?  "))
        self.model = str(input("Model?  "))
        self.cores = int(input("Number of Cores?    "))
        self.threads = int(input("Number of Threads?    "))
        self.base_clock = float(input("Base clock speed?     "))
        self.boost_clock = float(input("Boost Clock speed?     "))
        self.release_date = str(input("Release Quarter?  (Q* ****     "))
        self.benchmark_percentage = int(input("Benchmark percentage?    "))
        self.rank = int(input("Rank?"))
        self.integrated_graphics = bool(input("Integrated Graphics? True or False   "))
        self.url = str(input("URL?     "))
        self.price = int(input("Price?     "))
        self.wattage = int(input("Wattage? TDP?      "))


class Gpu:
    def __init__(self):
        #Base info variables
        self.brand ="N/A"
        self.model ="N/A"
        self.rank ="N/A"
        self.benchmark ="N/A"
        self.vram ="N/A"
        #Extra info variables
        self.url = "N/A"
        self.base_clock = "N/A"
        self.wattage = "N/A"
        self.price = "N/A"


class Ram:
    def __init__(self):
        #Base info variables
        self.brand = "N/A"
        self.model = "N/A"
        self.size ="N/A"
        self.speed = "N/A"
        #Extra info variables
        self.rank = "N/A"
        self.benchmark = "N/A"
        self.url = "N/A"
        self.price = "N/A"

def append_component(new_part):
    print ("Adding component...")
    with open('Logs/database_adder_error_log.txt', 'a') as database:
        json_string = json.dumps(new_part.__dict__)
        database.write(json_string + "\n")
    print ("Component added! \n")

def main():
    while True:
        print("Which part to add(input x to exit)? CPU | GPU | RAM | MOBO | SSD | HDD | PSU | CASE \n")
        part_category = str(input()).lower()
        if (part_category == 'x'):
            print ("Program exited.")
            break

        elif (part_category == 'cpu'):
            new_cpu = Cpu()
            new_cpu.add_cpu()
            append_component(new_cpu)

        elif (part_category == 'gpu'):
            add_gpu()
        elif (part_category == 'ram'):
            add_ram()
        elif (part_category == 'mobo'):
            add_mobo()
        elif (part_category == 'ssd'):
            add_ssd()
        elif (part_category == 'hdd'):
            add_hdd()
        elif (part_category == 'psu'):
            add_psu()
        elif (part_category == 'case'):
            add_case()

        else:
            print ("Invalid entry")
            with open('Logs/database_adder_error_log.txt','a') as log:
                now = datetime.now()
                now = str(now)
                log.write(now + ":  Error \n")


main()
