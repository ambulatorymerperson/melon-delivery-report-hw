
def printing_produce_orders(day, txt):
    """takes a file, separates the product names, amount, and price"""
    #prints first argument
    print day
    #creates variable 'file' which is an opened text passed as an argument 
    #when the function is called
    the_file = open(txt)
    #for loop to traverse through each line in the file
    for line in the_file:
        #gets rid of white space at the end of each line
        line = line.rstrip()
        #separates the elements of the string
        words = line.split('|')
        #prints a statement which takes the first, second, and third element of string
        print "Delivered {} {}s for total of ${}".format(
            words[0], words[1], words[2])
    #closes the file    
    the_file.close()
#calls the function, passing in the relevent files with named days
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
