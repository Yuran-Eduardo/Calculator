from art import logo

print(logo)

#functons 
def add(n1,n2):
  return n1 + n2

def sub(n1,n2):
  return n1 - n2

def multiply(n1,n2):
  return n1 * n2

def divide(n1,n2):
  return n1 / n2

operations = {
  "+": add,
  "-": sub,
  "*": multiply,
  "/": divide
}

def calculator():
  
  num1 = float(input("What's the first Number?: "))
  for symbol in operations:
    print(symbol)

  cont = True
  while cont:
    operation_symbol = input("Pick an operation:")
    num2 = float(input("What's the next Number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1,num2) 
        
    print(f"{num1} {operation_symbol} {num2} = {answer}")
  
    if input(f"Type 'y' to continue calculating with {answer}, or the 'n' to Exit: ") == 'y':
      num1 = answer
    else:
      cont = False
      calculator()
      
calculator()