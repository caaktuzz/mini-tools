import time
import datetime
import os





def loading() :
    while True:
      try: # чёрточки
        print(f"\r | ", end="", flush=True),time.sleep(0.3)
        print(f"\r / ", end="", flush=True),time.sleep(0.3)
        print(f"\r ─ ", end="", flush=True),time.sleep(0.3)
        print(f"\r \\ ", end="", flush=True),time.sleep(0.3)
        print(f"\r | ", end="", flush=True),time.sleep(0.3)
        print(f"\r / ", end="", flush=True),time.sleep(0.3)
        print(f"\r ─ ", end="", flush=True),time.sleep(0.3)
        print(f"\r \\ ", end="", flush=True),time.sleep(0.3)
      except KeyboardInterrupt: break 


def loading2() :
    while True:
      try: # спецсимволы
        print(f"\r @ ", end="", flush=True),time.sleep(0.3)
        print(f"\r # ", end="", flush=True),time.sleep(0.3)
        print(f"\r $ ", end="", flush=True),time.sleep(0.3)
        print(f"\r % ", end="", flush=True),time.sleep(0.3)
        print(f"\r ^ ", end="", flush=True),time.sleep(0.3)
        print(f"\r & ", end="", flush=True),time.sleep(0.3)
        print(f"\r * ", end="", flush=True),time.sleep(0.3)
      except KeyboardInterrupt: break 


def loading3() :
    while True:
      try: # стрелочки
        print(f"\r ⬆ ", end="", flush=True),time.sleep(0.3)
        print(f"\r ⬈ ", end="", flush=True),time.sleep(0.3)
        print(f"\r ⮕ ", end="", flush=True),time.sleep(0.3)
        print(f"\r ⬊ ", end="", flush=True),time.sleep(0.3)
        print(f"\r ⬇ ", end="", flush=True),time.sleep(0.3)
        print(f"\r ⬋ ", end="", flush=True),time.sleep(0.3)
        print(f"\r ⬅ ", end="", flush=True),time.sleep(0.3)
      except KeyboardInterrupt: break 

def loading4():
  while True:
    try: # точки
      print(f"\r .", end="", flush=True),time.sleep(0.3)
      print(f"\r ..", end="", flush=True),time.sleep(0.3)
      print(f"\r ...", end="", flush=True),time.sleep(0.3)
      print(f"\r     ", end="", flush=True),time.sleep(0.3)
    except KeyboardInterrupt: break 

def loading5():
  while True: 
   try: # английсикй алфавит
    bukvary = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    bukva = 0
    while bukva < len(bukvary):
      print("\r", bukvary[bukva], end="", flush=True), time.sleep(0.1)
      bukva += 1
   except KeyboardInterrupt: break


"""
# В одной строке. 0-100%. задержка - 0.01
for a in range(101):
  print(f"\r{a}%", end="", flush=True)
  a += 1
  time.sleep(0.01)
"""

"""
# Загрузка 0-100%. Шаг: 10%. Задержка: 0.5
for i in range(11):
    print(f"\rЗагрузка: {i * 10}%", end="", flush=True)
    time.sleep(0.5)
print("\nГотово!")
"""

"""
# Актуальное время вплоть до миллисекунд 
while True: 
    time_now = str(datetime.datetime.now())[11:-4].replace('.',':')
    print(f"\r{time_now}", end="", flush=True), time.sleep(0.01)
"""