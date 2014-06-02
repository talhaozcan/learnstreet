'''ahmet'''
'''learnstreet happynum'''
def happynum(num):
    while True:
        if len(str(num)) != 1:          
            temp=0
            for i in range(0,len(str(num))):
                temp = temp+ (int(str(num)[i]))**2
            num = temp
        else:
            break
    if int(num) == 1 :
        return 'Happy Number'
    else:
        return 'Unhappy Number'    
