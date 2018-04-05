
def printing_produce_orders(day, txt):
    """takes a file, separates the product names, amount, and price"""
    print day
    the_file = open(txt)
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

        print "Delivered {} {}s for total of ${}".format(
            count, melon, amount)
    the_file.close()
    
printing_produce_orders("Day 1", "um-deliveries-20140519.txt")
printing_produce_orders("Day 2", "um-deliveries-20140520.txt")
printing_produce_orders("Day 3", "um-deliveries-20140521.txt")


# print "Day 2"
# the_file = open("um-deliveries-20140520.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[1]
#     amount = words[2]

#     print "Delivered {} {}s for total of ${}".format(
#         count, melon, amount)
# the_file.close()


# print "Day 3"
# the_file = open("um-deliveries-20140521.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[1]
#     amount = words[2]

#     print "Delivered {} {}s for total of ${}".format(
#         count, melon, amount)
# the_file.close()
