weight = input("") 
if weight[-2:] in ["kg"]:
  poung = (eval(weight[0:-2])) * 2.2046
  print ("".format(poung))
elif weight[-2:] in ["pd"]:
  kg = (eval(weight[0:-2])) / 2.2046
  print("".format(kg))
else:
  print("")
