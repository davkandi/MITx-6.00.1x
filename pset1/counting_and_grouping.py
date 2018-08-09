def item_order(order):
    countsalad = order.count('salad')
    counthamburger = order.count('hamburger')
    countwater = order.count('water')
         
    return 'salad:' + str(countsalad) + ' hamburger:' + str(counthamburger) + ' water:' + str(countwater)
