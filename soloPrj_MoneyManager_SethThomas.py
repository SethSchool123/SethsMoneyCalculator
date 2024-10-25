#Seth's Money Manager 
#----------------------------------------------------- ADDITIONAL INFO
def NEVERCALL_addiional_COLOR():

    #FROM https://gist.github.com/rene-d/9e584a7dd2935d0f461904b9f2950007
    print("\033[31mHello, world!\033[0m") #EXAMPLE RED 
    print("\033[0;32mHello, world!") #EXAMPLE GREEN - SIMPLER
    # Add infront ^^^

    #ANSI color codes
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    END = "\033[0m"

#----------------------------------------------------- Fake loading screen
for x in range(0,10000):
    #print(f"Hello {x}")
    print("Loading: %s:"% x)



#----------------------------------------------------- Defined functions below

#----------------------- Main Screen Function
def main_screen():
    print("\033[0;32m:.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.")
    print("                                       ")
    print("┏┓   ┓ ╹   ┳┳┓          ┳┳┓            ") #Initial loading display
    print("┗┓┏┓╋┣┓ ┏  ┃┃┃┏┓┏┓┏┓┓┏  ┃┃┃┏┓┏┓┏┓┏┓┏┓┏┓") 
    print("┗┛┗ ┗┛┗ ┛  ┛ ┗┗┛┛┗┗ ┗┫  ┛ ┗┗┻┛┗┗┻┗┫┗ ┛ ")
    print("                     ┛            ┛    ")
    print("___________________________________________________________\n")

    print("Welcome to Seth's Money Manager, what would you like to do?\n___________________________________________________________") #Main Screen Display

    print("1) Simple Calculator\n2) Calculate Yearly Income\n3) Tally Expenses")

    choice = int(input("Your Selection?: "))

    return choice 
#----------- selection functions
def simple_calculator(value_calc_1, value_calc_2):

    value_calc_3 = value_calc_1 + value_calc_2

    print(f"{value_calc_1} + {value_calc_2} is: {value_calc_3}")
    
    input("Enter anything to return to the main menu: ")

def yearly_income():
    print("\033[1;36m:.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.")
    print("┏┓  ┓   ┓       ┓┏      ┓    ┳          ")
    print("┃ ┏┓┃┏┓┏┃┏┓╋┏┓  ┗┫┏┓┏┓┏┓┃┓┏  ┃┏┓┏┏┓┏┳┓┏┓")
    print("┗┛┗┻┗┗┗┻┗┗┻┗┗   ┗┛┗ ┗┻┛ ┗┗┫  ┻┛┗┗┗┛┛┗┗┗ ")
    print("                          ┛             ")

    weekly_pay = float(input("Enter your weekly pay: "))
    
    yearly_income = weekly_pay * 52
    
    print(f"Your yearly income is: {yearly_income}")

    input("Enter anything to return to the main menu: ")

def tally_expenses():
    print("\033[0;35m:.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.")
    print("┏┳┓  ┓┓    ┏┓            ")
    print(" ┃ ┏┓┃┃┓┏  ┣ ┓┏┏┓┏┓┏┓┏┏┓┏")
    print(" ┻ ┗┻┗┗┗┫  ┗┛┛┗┣┛┗ ┛┗┛┗ ┛")
    print("        ┛      ┛         ")
    budget = float(input("Enter your budget: "))
    
    expenses = [] #initialize that one loop I need!
    
    for expense_num in range(1, 4): #Index number stuff
        expense = float(input(f"Enter expense price {expense_num}: ")) #The {i} WAS is to prompt for the range, its where the enter expense 1, expense 2 and expense 3 come from
        expenses.append(expense)
    
    print(f"Your expenses cost: {expenses}")
    
    total_expenses = sum(expenses)
    
    remaining_budget = budget - total_expenses
    
    print(f"Total expenses: {total_expenses}")
    print(f"Remaining budget: {remaining_budget}")
    if total_expenses < remaining_budget:
        print("You have enough money to cover these purchases!")
    elif total_expenses == budget: #do budget and not remaining budget, duh
        print("You have just enough money to cover these purchasses!")
    elif total_expenses > remaining_budget:
        print("You do not have enough money to cover these purchasses!")
    

    input("Enter anything to return to the main menu: ")
    
#----------------------------------------------------- misc

# print("┏┓   ┓ ╹   ┳┳┓          ┳┳┓            ") #Initial loading display
# print("┗┓┏┓╋┣┓ ┏  ┃┃┃┏┓┏┓┏┓┓┏  ┃┃┃┏┓┏┓┏┓┏┓┏┓┏┓") 
# print("┗┛┗ ┗┛┗ ┛  ┛ ┗┗┛┛┗┗ ┗┫  ┛ ┗┗┻┛┗┗┻┗┫┗ ┛ ")
# print("                     ┛            ┛    ")

#----------------------------------------------------- Choices. 


while True:
    choice = main_screen()

    if choice == 1: 
        print("\033[0;31m:.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.")
        print("___________________________________________________________\n")
        print("┏┓•     ┓    ┏┓  ┓   ┓       ")
        print("┗┓┓┏┳┓┏┓┃┏┓  ┃ ┏┓┃┏┓┏┃┏┓╋┏┓┏┓")
        print("┗┛┗┛┗┗┣┛┗┗   ┗┛┗┻┗┗┗┻┗┗┻┗┗┛┛ ")
        print("      ┛                      ")
        value_calc_1 = float(input("Enter the first number: "))
        value_calc_2 = float(input("Enter the second number: "))
        simple_calculator(value_calc_1, value_calc_2)
    elif choice == 2:
        print("___________________________________________________________\n")
        # Calculate Yearly Income
        yearly_income()
    elif choice == 3:
        print("___________________________________________________________\n")
        # Tally Expenses
        tally_expenses()

    
