TQ_list = ["甲","乙","丙","丁","戊","己","庚","辛","壬","癸"]
DZ_list = ["子","丑","寅","卯","辰","巳","午","未","申","酉","戌","亥"]

user_month = input("Please enter your birth month: ")

try:
    #Birth Month Part    
    if 1 <= month_count <= 12 :
        print("Input accepted!\n")
        
        TQ_month = ((TQ_year * 2) + TQ_year) % 10
        if TQ_month != 0:
            Mnum_TQ = TQ_month - 1 
            月天千 = TQ_list[Mnum_TQ]
        else:
            月天千 = TQ_list[-1]

        Mnum_DZ = month_count - 1
        月地支 = DZ_Mlist[Mnum_DZ]

        print("Your lunar month is" + " " + 月天千 + 月地支 + "月")  
    else:
        print("Invalid Month!\n")

except ValueError:
    print("Invalid input! Please enter again.\n")
    



