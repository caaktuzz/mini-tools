
import os 
import time
import datetime 


def calc_time(time_now, time_end) :
  def check_days_in_month_and_year(year_number, month_number): # счёт дней в месяце и проверка на високосный год
      if month_number in (1, 3, 5, 7, 8, 10, 12): days_in_month = 31
      if month_number in (4, 6, 9, 11): days_in_month = 30

      if month_number == 2: # проверка на високосный год и счёт дней в феврале
        if (year_number % 4 == 0 and year_number % 100 != 0) or (year_number % 400 == 0): days_in_year = 366; days_in_month = 29
        else: days_in_year = 365; days_in_month = 28

      if (year_number % 4 == 0 and year_number % 100 != 0) or (year_number % 400 == 0): days_in_year = 366
      else: days_in_year = 365

      return days_in_year, days_in_month

  time_now_list = [time_now[0:4], time_now[5:7], time_now[8:10], time_now[11:13], time_now[14:16], time_now[17:19]] # разделение строки текущего времени на элементы
  time_end_list = [time_end[0:4], time_end[5:7], time_end[8:10], time_end[11:13], time_end[14:16], time_end[17:19]] # разделение строки конечного времени на элементы

  if time_now_list >= time_end_list: return None
  
  remain_list = [int(time_end_list[0])-int(time_now_list[0]), int(time_end_list[1])-int(time_now_list[1]), int(time_end_list[2])-int(time_now_list[2]), int(time_end_list[3])-int(time_now_list[3]), int(time_end_list[4])-int(time_now_list[4]), int(time_end_list[5])-int(time_now_list[5])] # оставшееся количество секунд в днях, часах, минутах и сек
  
  print(remain_list, '\n') # это технический вывод, потом уберу, забей

  # заём времени
  def days_in_prev_month(year, month):
      if month == 1:
          return check_days_in_month_and_year(year - 1, 12)
      return check_days_in_month_and_year(year, month - 1)
  
  if remain_list[5] < 0: remain_list[4] -= 1; remain_list[5] += 60
  if remain_list[4] < 0: remain_list[3] -= 1; remain_list[4] += 60
  if remain_list[3] < 0: remain_list[2] -= 1; remain_list[3] += 24
  if remain_list[2] < 0: remain_list[1] -= 1; remain_list[2] += days_in_prev_month(int(time_end_list[0], int(time_end_list[1])))[1]
  if remain_list[1] < 0: remain_list[0] -= 1; remain_list[1] += 12 

  years =   str(remain_list[0])
  months =  str(remain_list[1])
  days =    str(remain_list[2])
  hours =   str(remain_list[3])
  minutes = str(remain_list[4])
  seconds = str(remain_list[5])

  if remain_list[0] < 10:   years = f"0{years}"
  if remain_list[1] < 10:  months = f"0{months}"
  if remain_list[2] < 10:    days = f"0{days}"
  if remain_list[3] < 10:   hours = f"0{hours}"
  if remain_list[4] < 10: minutes = f"0{minutes}"
  if remain_list[5] < 10: seconds = f"0{seconds}"

  return tuple((years, months, days, hours, minutes, seconds))

while True:
  remain_time = calc_time(str(datetime.datetime.now())[:-7], "2026-12-08 00:00:00")
  if remain_time is None: print("time_is_up"); break
  print("years:",remain_time[0], "months:",remain_time[1], "days:",remain_time[2], " hours:",remain_time[3], " minutes:",remain_time[4], "seconds:",remain_time[5], end='\r', flush=True)
  time.sleep(1 - time.time() % 1)


