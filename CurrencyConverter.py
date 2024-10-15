def run_Converter():
   while True:
      print("What currency are you starting with? ")
      choices = ["US Dollar", "Euro", "British Pound", "CA Dollar", "Yen", "Franc", "Peso"]
      

      start_curr = input("Enter amount: ")

      try:
         start_curr = float(start_curr)

         if start_curr >= 0:
            print(f"You entered {start_curr}. The converted amount is {converted_curr}.")
         else:
            print("Amount cannot be negative.")
            run_Converter()
      except ValueError:
         print("Invalid amount")

def converted_curr():
   print('test')

run_Converter()