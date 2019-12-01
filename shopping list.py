import time
while True:
  shoppingcart = []
  print ('Shopping Cart:')
  print('Your Shopping Cart is Empty!!!')
  print ('_'*50)
  items = int(input('How Many Items Do You Want To Add To Your Shopping Cart '))
  
  for x in range(items): 
    additem = input('Enter An Item To Add To Your Shopping Cart: ').title()
    shoppingcart.append(additem)
  print('_'*50)
  print ('Shopping Cart:')
  totalitems = len(shoppingcart)
  print (f"Items:{totalitems}")
  for item in shoppingcart:
    print(item)
  
  print ('Time To Check The Items Out!!!')
  exit(items)
  
  while len(shoppingcart) > 0:  
    checkout=input("Check an Item Out ").title()
    if checkout not in shoppingcart:
        print ('This Is Not An Item From The Shopping List')
    else:
        shoppingcart.remove(checkout)
        for item in shoppingcart:
            print(item)
            print('_'*50)
      
          
    
    
  print ('Done!!!')
  time.sleep(5)
  print ("Restarting...")
  time.sleep(5)
  print('_'*50)
  
    
    
  
