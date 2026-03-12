from sales_record import sales

#sum funtion was defined to add up all the total values getting store in the diccionary 

def sum_t():
    sum_total = sum(i["total"] for i in sales) 
    print (f"El total recaudado es de: {sum_total}\n")
