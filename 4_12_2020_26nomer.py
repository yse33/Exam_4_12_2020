#exercise 1
def calculate(build_price, sell_price, volume):
    win = (sell_price-build_price) * volume
    print(win)
bp = float(input("Enter build price: "))
sp = float(input("Enter sell price: "))
v = int(input("Enter volume: "))
calculate(bp, sp, v)

#exercise 2
def wash_hands(tpd, months):
    total_times = tpd * months * 30
    seconds = 21 * total_times
    minutes = seconds / 60
    print(int(minutes), "minutes")
tpd = int(input("How many times per day do you wash your hands: "))
months = int(input("How many months did you do that for: "))
wash_hands(tpd, months)

    

