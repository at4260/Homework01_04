def payment(opened_file):
    for line in opened_file:
        words = line.split(",")
        melon_cost = 1.00
        cust_expected = float(words[2]) * melon_cost
        cust_paid = float(words[3])
        if cust_paid > cust_expected:
            print "%s has overpaid" % words[1]
        elif cust_paid < cust_expected:
            print "%s has UNDERPAID" % words[1]
        else:
            pass

payment(open("customer_orders_04.csv"))