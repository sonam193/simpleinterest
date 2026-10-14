
def simple_interest(principal, interest, time):
    return (principal * interest * time) / 100

if __name__ == "__main__":
    p = float(input("Enter principal amount: "))
    i = float(input("Enter rate of interest: "))
    t = float(input("Enter time in months: "))

    print("Simple interest is:", simple_interest(p, i, t))
