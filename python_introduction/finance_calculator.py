monIncome = input("Enter your monthly income: ")
totalExpenses = input("Enter your total monthly expenses: ")
MI=int(monIncome)
TE=int(totalExpenses)

MonthlySavings =  MI - TE

ProjectedSavings = MonthlySavings * 12 + (MonthlySavings * 12 * 0.05)

print ("Your monthly savings are $",MonthlySavings,".Projected savings after one year, with interest, is: $",int(ProjectedSavings),".")