def diviser(a , b) :
    try:
      return a / b 
    except ZeroDivisionError :
       print("b must not be 0")
       return 0.0
    except TypeError :
       print("les values must be numbers")  
       return 0.0 
    finally :
       print("Opération terminée")
 
diviser(10 , 2)
diviser(10 , 0)
diviser(10 , "2")
