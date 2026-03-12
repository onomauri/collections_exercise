sales = [] #selected becouse allow us to add a dictionary inside 
def sales_reg ():

    try:
        name = input("Enter the product name: ")
        cost = float(input("enter the price of the produt: "))
        while cost <= 0:
             print("Error: valor invalido.")
             cost = float(input("enter the price of the produt: "))

        amount = int(input("enter the quantity of the product: "))
        while amount <= 0:
            print("Error: Debe agregar minimo un producto")    
            amount = float(input("enter the price of the produt: "))

        total = cost*amount
        print(f"The total amout is: {total}")


        sale = {                             #use to store the information from the user 
            "name": name,
            "cost" : cost,
            "amount" : amount,
            "total" : total
        }
        sales.append(sale) #code to save the dictionary inside the list 
        #print(sale)
    except ValueError:
           print("favor ingrese un valor numerico")
