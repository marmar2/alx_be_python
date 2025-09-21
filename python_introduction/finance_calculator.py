monIncome = input("Enter your monthly income: ")
totalExpenses = input("Enter your total monthly expenses: ")
MI=int(monIncome)
TE=int(totalExpenses)

MonthlySavings =  MI - TE

ProjectedSavings = float(MonthlySavings) * 12 + (float(MonthlySavings) * 12 * 0.05)

print('Your monthly savings are $',MonthlySavings,'.')
print("Projected savings after one year, with interest, is: $",int(ProjectedSavings),".")