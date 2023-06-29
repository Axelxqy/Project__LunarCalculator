#Setting limiters for checks to ensure the input is correct (filter)

TQ_list = ["甲","乙","丙","丁","戊","己","庚","辛","壬","癸"]
DZ_list = ["子","丑","寅","卯","辰","巳","午","未","申","酉","戌","亥"]

user_year = input("Please enter your Birth Year: ")


try:
    word_count = int(user_year)
    if len(user_year) != 4:
        print("Input Accepted!\n")

        #Use Modulo (%) to get remainder of the number  
        TQ_year = (word_count - 3) % 10
        DZ_year = (word_count - 3) % 12

        #Formula to find the correct lunar year
        if TQ_year != 0:
            temp_num = TQ_year - 1
            年天千 = TQ_list[temp_num]
        else:
            年天千 = TQ_list[-1]

        if DZ_year != 0:
            temp_num = DZ_year - 1
            年地支 = DZ_list[temp_num]
        else:
            年地支 = DZ_list[-1]

        print("Your lunar year is" + " " + 年天千 + 年地支 + "年")  
        
        
    else:
        print("Only 4 numbers are acceptable!\n")
        
except ValueError:
    print("Invalid input! Please enter again.\n")            












     