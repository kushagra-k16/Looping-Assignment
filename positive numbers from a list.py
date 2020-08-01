def positive_numbers():
        ch ='y'
        while ch == "y" or ch == "Y":
                a =[]
                k =0
                n = int(input("Enter the number of terms you want to enter:"))
                for i in range(0,n):
                        x = eval(input("Enter the terms:"))
                        a.append(x)
                print('List entered =', a)
                while(k < len(a)): 
                        if a[k] >= 0:
                                print(a[k], end = ",")  
                        k += 1
                print('\n')
                ch = input("Do you wish to continue??(y/n)")
positive_numbers()
                                
                
