def melon_listing(day, my_file):
    print "Day %s" % day
    for line in my_file:
        line = line.rstrip()
        words = line.split(',')
        
        melon = words[0]
        count = words[1]
        amount = words[2]
        
        print "Delivered %s %ss for a total of: $%s" % (count, melon, amount)
    my_file.close()
    print

melon_listing(1,open("um-deliveries-20140519.csv"))
melon_listing(2,open("um-deliveries-20140520.csv"))
melon_listing(3,open("um-deliveries-20140521.csv"))