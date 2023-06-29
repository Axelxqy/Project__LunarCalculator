#Ask user to input DAY, MONTH, YEAR and TIME of birth 
#Calculate all the possibilities
#print out 农历时间

#Setting limiters for checks to ensure the input is correct (filter)


from datetime import datetime

def calculate_total_days(year_start, month_start, day_start, year_end, month_end, day_end):
    start_date = f"{year_start}-{month_start}-{day_start}"
    end_date = f"{year_end}-{month_end}-{day_end}"
    start_datetime = datetime.strptime(start_date, '%Y-%m-%d')
    end_datetime = datetime.strptime(end_date, '%Y-%m-%d')
    total_days = ((end_datetime - start_datetime).days + 1)
    return total_days

TG_list = ["甲","乙","丙","丁","戊","己","庚","辛","壬","癸"]
DZ_Ylist = ["子","丑","寅","卯","辰","巳","午","未","申","酉","戌","亥"]
DZ_Mlist = ["寅","卯","辰","巳","午","未","申","酉","戌","亥","子","丑"]


user_year = int(input("Please enter your Birth Year (Year 1900 and above): "))
user_month = int(input("Please enter your birth month (Month 1-12): "))
user_day = int(input("Please enter your birth date (Day 1-31): "))
user_time = int(input("Please enter your birth time (0-23): "))


#Birth Year Part
if user_year >= 1900:
    print("Year Input Accepted!\n")
    #Use Modulo (%) to get remainder of the number  
    TG_year = (user_year - 3) % 10
    DZ_year = (user_year - 3) % 12

    #Formula to find the correct lunar year using the lists
    if TG_year != 0:
        Ynum_TG = TG_year - 1
        年天干 = TG_list[Ynum_TG]
    else:
        年天干 = TG_list[-1]

    if DZ_year != 0:
        Ynum_DZ = DZ_year - 1
        年地支 = DZ_Ylist[Ynum_DZ]
    else:
        年地支 = DZ_Ylist[-1]

    print("Your lunar year is" + " " + 年天干 + 年地支 + "年")        
else:
   print("Invalid Year Input!\n")
 
#Birth Month Part    
if 1 <= user_month <= 12 :
    print("Month Input Accepted!\n")
    lunar_month = ((TG_year * 2) + user_month) % 10
    if lunar_month != 0:
        Mnum_TG = lunar_month - 2
        月天干 = TG_list[Mnum_TG]
    else:
        月天干 = TG_list[-1]

    Mnum_DZ = user_month - 2
    月地支 = DZ_Mlist[Mnum_DZ]

    print("Your lunar month is" + " " + 月天干 + 月地支 + "月")  
else:
    print("Invalid Month Input!\n")

#Birth Date Part
#Figuring the year groups
if 1 <= user_day <= 31:
    print("Date Input Accepted!\n")
    last2_num = user_year % 100

    #Getting 基数
    if user_year >= 1900:
        if 1900 <= user_year <= 1999:
            基数 = (last2_num + 3) * 5 + 55 + (last2_num - 1) // 4

        elif 2000 <= user_year <= 2099:
            基数 = (last2_num + 7) * 5 + 15 + (last2_num + 19) // 4

    #Simplifing 基数
    if 基数 > 60:
        基数 = 基数 - 60

    #Calculating total days
    year_start = user_year   
    month_start = 1  
    day_start = 1   
    year_end = user_year   
    month_end = user_month   
    day_end = user_day     

    total_days = calculate_total_days(year_start, month_start, day_start, year_end, month_end, day_end)

#Preparing lunar_day for 天天干 and 天地支
    lunar_day = 基数 + total_days
    while lunar_day > 60:
        if lunar_day > 60:
            lunar_day = lunar_day - 60
        
    Dnum_TG = lunar_day % 10
    Dnum_DZ = lunar_day % 12

    if Dnum_TG != 0:
        Dnum_TG = Dnum_TG - 1
        天天干 = TG_list[Dnum_TG]
    else:
        天天干 = TG_list[-1] 
        
    if Dnum_DZ != 0:
        Dnum_DZ = Dnum_DZ - 1
        天地支 = DZ_Ylist[Dnum_DZ]
    else:
        天地支 = DZ_Ylist[-1]

    print("Your lunar date is" + " " + 天天干 + 天地支 + "天")  
else:
    print("Invalid Date Input!\n")

#Birth Time Part
if 0 <= user_time <= 23:
    print("Time Input Accepted!\n")

    if user_time == 23 or user_time == 0:
       时地支 = DZ_Ylist[0]
    elif user_time == 1 or user_time == 2:
        时地支 = DZ_Ylist[1]
    elif user_time == 3 or user_time == 4:
        时地支 = DZ_Ylist[2]
    elif user_time == 5 or user_time == 6:
        时地支 = DZ_Ylist[3]
    elif user_time == 7 or user_time == 8:
        时地支 = DZ_Ylist[4]
    elif user_time == 9 or user_time == 10:
        时地支 = DZ_Ylist[5]
    elif user_time == 11 or user_time == 12:
        时地支 = DZ_Ylist[6]
    elif user_time == 13 or user_time == 14:
        时地支 = DZ_Ylist[7]
    elif user_time == 15 or user_time == 16:
        时地支 = DZ_Ylist[8]
    elif user_time == 17 or user_time == 18:
        时地支 = DZ_Ylist[9]
    elif user_time == 19 or user_time == 20:
        时地支 = DZ_Ylist[10]
    elif user_time == 21 or user_time == 22:
        时地支 = DZ_Ylist[11]

    TG_index = TG_list.index(天天干) + 1
    DZ_index = DZ_Ylist.index(时地支) + 1
    
    Tnum_TG = TG_index * 2 + DZ_index - 2

    if Tnum_TG > 10:
        Tnum_TG = Tnum_TG % 10 
    
    if Tnum_TG != 0:
        Tnum_TG = Tnum_TG - 1
        时天干 = TG_list[Tnum_TG]
    else:
        时天干 = TG_list[-1] 

    print("Your lunar time is" + " " + 时天干 + 时地支 + "时")
else:
    print("Invalid Time Input!\n")

print("")        
print("Your 八字 is" + " " + 年天干 + 年地支 + "年" + " " + 月天干 + 月地支 + "月" + " " + 天天干 + 天地支 + "天"
      + " " + 时天干 + 时地支 + "时")