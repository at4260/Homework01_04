print "******************************************"
file_melon_type = open("orders_by_type.csv")
melon_tallies = {"Musk":0, "Hybrid":0, "Watermelon":0, "Winter": 0}
for line in file_melon_type:
    data = line.split(",")
    melon_type = data[1]
    melon_count = int(data[2])
    melon_tallies[melon_type] += melon_count
melon_prices = { "Musk": 1.15, "Hybrid": 1.30, "Watermelon": 1.75, "Winter": 4.00 }
total_revenue = 0
for melon_type in melon_tallies:
    revenue = melon_prices[melon_type] * melon_tallies[melon_type]
    total_revenue += revenue
    print "We sold %d %s melons at %0.2f each for a total of %0.2f" % (melon_tallies[melon_type], melon_type, melon_prices[melon_type], revenue)
print "******************************************"
file_sales_type = open("orders_with_sales.csv")
online_sales = 0
phone_sales = 0
for line in file_sales_type:
    data = line.split(",")
    if data[1] == "0":
        online_sales += float(data[3])
    else:
        phone_sales += float(data[3])
print "Salespeople generated %0.2f in revenue." % phone_sales   
print "Internet sales generated %0.2f in revenue." % online_sales