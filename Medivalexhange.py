from multiprocessing.util import log_to_stderr

lotTogram = 13.3
poundsTolot= 32
talentTopounds = 20

talent = float(input("Enter Talets"))
Pound = float(input("Enter Pound"))
Lots = float(input("Enter Lots"))





total_lots=(talent * 20 *32) + (Pound *32) + Lots
totalgrams=total_lots * 13.3


kilograms = int(totalgrams // 1000)
grams = totalgrams % 1000

print("The total mass in kilograms is", kilograms)
print("The total mass in grams is" , grams)
