from sales_record import sales   #was add as the list sales will be use in the for loop

#for i in sales:
#    print (f"RESUMEN DE VENTAS DEL DIA\n \n producto: {i['name']}")

def fun_sumary():
    print("\nRESUMEN DE VENTAS DEL DIA")
    for i in sales:
        print (f"\nProducto: {i['name']}")
        print (f"Cantidad total vendida: {i['total']}\n")