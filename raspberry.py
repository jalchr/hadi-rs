from time import sleep
from termcolor import colored, cprint
import RepeatedTimer as scheduler

balance = 0.0
pulseGenerator = None
pulses = 0

def getPulses():
    global pulses
    pulses = pulses + 10

def KW_meter_emulator():
    # Sends pluses every millisecond
    print("starting KW meter emulator...")
    global pulseGenerator
    # it auto-starts, no need of rt.start()  
    pulseGenerator = scheduler.RepeatedTimer(1, getPulses) 


def view_balance():
    cprint("Balance: " + str(balance), 'blue')

def view_consumption():
    cprint("Consumption: " + str(pulses), 'red')

def refill(amount):
    global balance
    # Get current balance
    # Add new amount
    balance = float(amount) + balance
    cprint("Refilled successfully", 'green')
    

def start_refill():
    print("Please enter refill code")
    code = input()
    if code == 'abc':
        amount = 100
    elif code== 'xyz':
        amount = 200
    refill(amount)
    view_balance()

def getCommand():
     text = input()
     while text != 'r' and text != 'b' and text != 'q' and text != 'p':        
        cprint('Please enter valid commands: r => refill, b => view balance, p => view consumption, q => quit', 'red')   
        text = input()
     return text

def main():
    print("Initializing...")
    KW_meter_emulator()

    cprint('Press any key to start', 'green', attrs=['blink'])   
    cprint('Please enter valid commands: r => refill, b => view balance, p => view consumption, q => quit', 'green')
    
    command = getCommand()
    if command == 'r':
        start_refill()
    elif command == 'b':
        view_balance()
    elif command == 'p':
        view_consumption()
    elif command == 'q':
       print("Quit")
       return

    pulseGenerator.stop()
    print("Stopping KW meter emulator")
    print("")
    print("-------------------------------------")
    print("")

main()