def cost_return(cost, count):
    return("total cost is" + str(cost*count))

cost = 50
count = 2

with_return = cost_return(cost, count)
print(with_return)