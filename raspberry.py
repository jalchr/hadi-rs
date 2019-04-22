from time import sleep
from termcolor import colored, cprint

balance = 0.0

def view_balance():
    cprint("Balance: " + str(balance), 'blue')

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
     while text != 'r' and text != 'b' and text != 'q':        
        cprint('Please enter valid commands: r => refill, b => view balance, q => quit', 'red')   
        text = input()
     return text

def main():
    print("Initializing...")
    sleep(2)    
    cprint('Press any key to start', 'green', attrs=['blink'])   
    cprint('Please enter valid commands: r => refill, b => view balance, q => quit', 'green')
    
    command = getCommand()
    if command == 'r':
        start_refill()
    elif command == 'b':
        view_balance()
    else:
       return

main()