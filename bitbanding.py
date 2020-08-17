port_address_base = {
    "GPIOA" : 0x42000000,
    "GPIOB" : 0x42000400,
    "GPIOC" : 0x42000800,
    "GPIOD" : 0x42000C00,
    "GPIOE" : 0x42001000,
    "GPIOF" : 0x42001400,
    "GPIOG" : 0x42001800,
    "GPIOH" : 0x42001C00,
    "GPIOI" : 0x42002000,
    "GPIOJ" : 0x42002400,
    "GPIOK" : 0x42002800
}

port_address_index = {
    "A" : "GPIOA",
    "B" : "GPIOB",
    "C" : "GPIOC",
    "D" : "GPIOD",
    "E" : "GPIOE",
    "F" : "GPIOF",
    "G" : "GPIOG",
    "H" : "GPIOH",
    "I" : "GPIOI",
    "J" : "GPIOJ",
    "K" : "GPIOK"
}

sf_register_base = {
    "MODER" : 0x40020000,
    "OTYPER": 0x40020004,
    "OSPEEDR" : 0x40020008,
    "PUPDR" : 0x4002000c,
    "IDR" : 0x40020010,
    "ODR" : 0x40020014,
    "BSRR" : 0x40020018,
    "LCKR" : 0x4002001c,
    "AFRL" : 0x40020020,
    "AFRH" : 0x40020024
}

sf_register_index = [
    "MODER", "OTYPER", "OSPEEDR", "PUPDR", "IDR",
    "ODR", "BSRR", "LCKR", "AFRL", "AFRH"
]

port_list = [
    'A', 'B', 'C', 'D', 'E',
    'F', 'G', 'H', 'I', 'J', 'K'
]

def bit_band_calculator(port_pin_dict, sf_register):
    sf_register_address = sf_register_base.get(sf_register)
    alias_region_base = port_pin_dict.get('port_base_address')
    bit_band_region_base = 0x40000000
    region_base_offset =  sf_register_address - bit_band_region_base
    pin_number = int(port_pin_dict.get('pin_number'))
    bit_band_address = alias_region_base + (region_base_offset * 0x20) + (pin_number * 0x4)
    port_name = port_pin_dict.get('port_name')
    print("Bit Band Address for " + port_name + ", Pin number " + str(pin_number)
        + " and SF Register " + sf_register + " is " + str(hex(bit_band_address)))

def get_port_pin(pin_name):
    if pin_name[0].upper() != 'P':
        return 1
    elif pin_name[1].upper() not in port_list:
        return 2
    elif len(pin_name) == 4 and int(pin_name[2]) > 1:
        return 3
    elif len(pin_name) > 4:
        return 4
    elif len(pin_name) == 4 and int(pin_name[3]) > 5:
        return 5
    else:
        port_name = port_address_index.get(pin_name[1])
        port_base_address = port_address_base.get(port_name)
        if len(pin_name) == 3:
            pin_number = pin_name[2]
        else:
            pin_number = (int(pin_name[2]) * 10) + int(pin_name[3])
    port_pin_dict = {
        "port_name" : port_name,
        "port_base_address" : port_base_address,
        "pin_number" : pin_number
    }

    return port_pin_dict

if __name__ == "__main__":
    print("===================================")
    print("-----Bit Band Address Generator----")
    print("------------Version 1.0------------")
    
    while True:
        pin_name = input("Enter pin name (e.g. PA5, PB13 etc., q to quit): ")
        
        if pin_name.upper() == "Q":
            print("Program Quit Successfully.")
            exit()

        port_pin_dict = get_port_pin(pin_name)

        if port_pin_dict == 1 or port_pin_dict == 4 or port_pin_dict == 5:
            print("Incorrect pin name/number. Exiting Program.")
            exit()
        elif port_pin_dict == 2:
            print("Incorrect port name. Exiting Program.")
            exit()
        
        print('---')
        
        print("Choose SF Register: ")
        print("00. MODER")
        print("01. OTYPER")
        print("02. OSPEEDR")
        print("03. PUPDR")
        print("04. IDR")
        print("05. ODR")
        print("06. BSRR")
        print("07. LCKR")
        print("08. AFRL")
        print("09. AFRH")

        sf_register_choice = int(input("Enter choice: "))
        sf_register = sf_register_index[sf_register_choice]
        
        print('---')
        print("You have selected: ")
        print("Port: " + port_pin_dict.get('port_name'))
        print("Pin Number: " + str(port_pin_dict.get('pin_number')))
        print("SF Register: " + sf_register_index[sf_register_choice])
        
        confirmation = input("Confirm for calculation (y/n): ")
        if confirmation == 'y':
            bit_band_calculator(port_pin_dict, sf_register)
            print('---')
        else:
            print("Restarting input process...")
