def simple_interest(principal,interest,time):
    return (principal*interest*time)/100

if__name__ =="__main__":
    p = int(input("Enter principal amt"))
    i = float(input("Enter interest"))
    t = int(input("Enter time in months"))

    print("Simple interest is:",simple_interest(p,i,t))