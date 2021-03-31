from art import logo

def add(n1, n2):
  """creamos la suma"""
  return n1 + n2
def minus(n1, n2):
  """creamos la resta"""
  return n1 - n2
def times(n1, n2):
  """creamos la multiplicación"""
  return n1 * n2
def div(n1, n2):
  """creamos la división"""
  return n1 / n2
operations = {
  "+" : add,
  "-" : minus,
  "*" : times,
  "/" : div
}
def calculator():
  print(logo)
  n1 = float(input("Ingresa el primer numero: "))
  for o in operations:
    print(o)

  again = True

  while again: 
    choose = input("Qué tipop de operación quieres?: ")
    n2 = float(input("Ingresa el segundo numero: "))
    calculation_function = operations[choose]
    answer = calculation_function(n1, n2)

    print(f"{n1} {choose} {n2} = {answer}")

    if input(f"Quieres cotinuar usando {answer}? o escribe 'n' para comenzar una nueva operación ") == "y":
      n1 = answer
    else: 
      again = False
      calculator()

calculator()