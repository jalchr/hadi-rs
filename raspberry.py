from time import sleep
from termcolor import colored, cprint
import RepeatedTimer as scheduler

balance = 0.0
pulseGenerator = None

def turn_off():
    print()
    cprint("***************************", 'red')
    cprint("* Turning OFF electricity *", 'red')
    cprint("***************************", 'red')
    print()

def turn_on():
    print()
    cprint("__________________________", 'blue')
    cprint("| Turning ON electricity |", 'blue')
    cprint("|________________________|", 'blue')
    print()

def warn_on_low_balance():
    cprint(f"Warning: your balance is {balance}, please refill", 'magenta')


def simulate_power_consumption():
    global balance
    balance = balance - 10
    save_balance()
    if 0 < balance <= 20:
        warn_on_low_balance()
    elif balance <= 0:
        turn_off()
        global pulseGenerator
        pulseGenerator.stop()
        cprint('Please enter valid commands: r => refill, b => view balance, q => quit', 'white')

def KW_meter_emulator():   
    # Sends pluses every millisecond
    print("Initiate KW meter emulator...")
    global pulseGenerator
    # it auto-starts, no need of rt.start()  
    pulseGenerator = scheduler.RepeatedTimer(2, simulate_power_consumption)
    pulseGenerator.stop() 

def KW_meter_start():
    global pulseGenerator
    pulseGenerator.start()

def view_balance():
    cprint("Balance: " + str(balance), 'blue')

def save_balance():
    with open("balance.txt", "w") as text_file:
        print(f"{balance}", file=text_file)

def load_balance():
    # reads the balance from the file
    text_file = open("balance.txt", "r", encoding='utf-8')
    value = text_file.read()
    global balance
    balance = int(float(value))

def refill(amount):
    global balance   
    was_empty = balance == 0
    # Add new amount
    balance = float(amount) + balance
    save_balance()
    cprint("Refilled successfully", 'green')    
    if was_empty:
        turn_on()
        KW_meter_start()

def start_refill():
    print("Please enter refill code: try 'abc'= 100, 'xyz'= 200")
    code = input()
    if code == 'abc':
        amount = 100
    elif code== 'xyz':
        amount = 200
    else:
        cprint('Invalid refill code', 'red')
        return
    refill(amount)
    view_balance()

def check_for_refill():
    global balance
    if balance <= 0:
        cprint('Out of balance, refill required', 'red')   
    while balance <=0 :
        start_refill()

def getCommand():
     cprint('Please enter valid commands: r => refill, b => view balance, q => quit', 'white')    
     text = input()
     while text != 'r' and text != 'b' and text != 'q' and text != 'p':        
        cprint('Please enter valid commands: r => refill, b => view balance, q => quit', 'red')   
        text = input()
     return text

def main():
    print("Initializing...")
    KW_meter_emulator()
    load_balance()
    check_for_refill()    
    KW_meter_start()
    
    command = getCommand()

    # continuous run until 'q' is hit
    while True:        
        if command == 'r':
            start_refill()
            command = getCommand()
        elif command == 'b':
            view_balance()
            command = getCommand()
        elif command == 'q':
            print("Quit")
            break

    pulseGenerator.stop()
    print("Stopping KW meter emulator")
    print("")
    print("-------------------------------------")
    print("")

main()