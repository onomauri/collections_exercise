## main document use as the principal where all the funtions are convine to make the proyect works importing them form the different files of the proyect

from sales_record import sales_reg as fs
from sales_record import sales
from sumary import fun_sumary
from calculation_of_totals import sum_t

confirmation = "no" #created to work as a condition to keep the program working till the user decide to finish

while confirmation != "yes":   #this comparison operator was choose to make sure only an specific word break the loop
    fs()
    confirmation = input("Ingrese 'yes' para finalizar, de lo contrario oprima presione enter: ").lower() 
fun_sumary()

#--------------only for practice---------------#
#for sale in sales: 
#    print(sale["name"])

#for sale in sales:
#    print(sale)

#sum_total = sum(sale["total"] for sale in sales)
#print(sum_total)

#sum_total = sum(i["total"] for i in sales)
#print(f"Total recaudado: {sum_total}")
#--------------only for practice---------------#

sum_t()

