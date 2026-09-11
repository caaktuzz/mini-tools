
import time
import random
import string



def randKey():
    quantity = int(input("quantity: "))
    password = ""
    pass_pr = []
    for j in range(quantity):
      pass_pr.append(random.randint(0, 9))
      pass_pr.append(random.choice(string.ascii_letters))
      password = f"{str(password)+str(pass_pr[j])}"
      print(f"\r {password}", end="", flush=False)
      time.sleep(0.1)
    print("\nresolut :",password)


def emailCode(): 
  email_code = ""
  for _int in range(4): 
    email_code += str(random.randint(0, 9))
  print(email_code)

def randPassword():
  password = ""
  for j in range(random.randint(8, 12)):
    a = random.randint(0, 2)
    special_characters = ['!','@','#','$','%','^','&','*','+','-']
    if a == 0: password += str(random.randint(0, 9))
    elif a == 1: password += special_characters[random.randint(0, 9)]
    else: password += random.choice(string.ascii_letters)
  print(password)


