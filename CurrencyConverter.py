from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
import currency_converter


choices = ["USD", "EUR", "GBP", "JPY", "CHF", "MXN", "CAD"]
completer = WordCompleter(choices)


def run_converter():
   while True:
      # Select starting currency
      print("\n *** Menu *** \nChoose from the following options below:")
      print(choices)
      session = PromptSession()
      result = session.prompt("What is your starting currency? ", completer=completer)

      if result not in choices:
         print("Invalid currency choice.")
         continue


      # Select converted currency
      session_two = PromptSession()
      result_two = session_two.prompt("What is your new desired currency? ", completer=completer)

      if result not in choices:
         print("Invalid currency choice.")
         continue


      while True:
         # Select numerical value of currency
         start_curr = input("Enter amount: ")
         try:
            start_curr = float(start_curr)
            # Genereates numerical conversion of currency
            if start_curr >= 0:
               break            
            else:
               print("Amount cannot be negative. Please enter a positive value.")
         except ValueError:
            print("Invalid amount. Please enter a number.")
      

      # Perform conversion
      c = currency_converter.CurrencyConverter()
      converted_curr = c.convert(start_curr, result, result_two)
      print(f"You entered {start_curr} {result}. The converted amount is {converted_curr} {result_two}.")

      # Continue
      run_again()


def run_again():
   close_app = input("Would you like to convert another amount? (Y/N)").upper()

   if close_app == "Y":
      run_converter()
   elif close_app == "N":
      print("See you later!")
      exit()
   else:
      print("Invalid choice!")
      run_again()


run_converter()