
import os
import subprocess
import time 

if os.name == "nt":  # активация ansi
    os.system("color")

def ping(hostname, delay, quantity):
  loop = 0
  while True:
    try:
      loop += 1
      time.sleep(delay)
      if loop > quantity: return f"заданная остановка ({loop-1})"
      result = subprocess.run(
                ["ping", "-n", "1", hostname],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,)
      response = result.returncode
      #response = os.system(f"ping -n 1 {hostname}")
      if response == 0:
        print(f"[{loop}]\033[34m ответ сервера: \033[35m {response} \033[0m | \033[32m @{hostname} доступен! \033[0m")
      else:
        print(f"[{loop}]\033[34m ответ сервера: \033[35m {response} \033[0m | \033[33m @{hostname} недоступен! \033[0m")
    except KeyboardInterrupt: return "внешнее прерывание"

while True:
  try:
    ip_input = input("ip: ")
    delay_input = float(input("delay: "))
    quantity_ping_input = int(input("quantity: "))
  except ValueError: print("число вводи нормально да"); continue
  except KeyboardInterrupt: break
  else:
    _ping = ping(ip_input, delay_input, quantity_ping_input)
    print(f"\033[31m{_ping}\033[0m"), time.sleep(2)


