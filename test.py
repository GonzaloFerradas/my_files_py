try:
    num = int(input("Ingresa un número: "))
    print ("9/ {} = {}".format(num,9/num))
excep Exception as e:
    print("Ocurrio el siguiente error: ", type(e).__name__)