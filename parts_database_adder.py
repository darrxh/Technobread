from datetime import datetime


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



class Gpu:
    def __init__(self):
        self.brand ="N/A"
        self.model ="N/A"
        self.rank ="N/A"
        self.benchmark ="N/A"
        self.vram ="N/A"
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





def main():
    while True:
        print("Which part to add(input x to exit)? CPU | GPU | RAM | MOBO | SSD | HDD | PSU | CASE /n")
        part_category = str(input()).lower()
        if (part_category == 'x'):
            break

        elif (part_category == 'cpu'):
            add_cpu()
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
            with open('/Logs/database_adder_error_log.txt','a') as log:
                log.write('huh')
            



main()




