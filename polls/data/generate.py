import random
import sys

def main(args):

    number = int(args[0])

    ticket_formatting = "Detta är ticket #{}."
    product_formatting = "Product{}"

    filename_products = "{}_products.txt".format(number)
    filename_tickets = "{}_tickets.txt".format(number)

    text_sizes = [1,2,5,7,12]

    product_list = [product_formatting.format(num) for num in range(number)]

    ticket_list = []
    for ticket_number in range(number):
        repetiontions = random.choice(text_sizes)
        text = repetiontions*ticket_formatting.format(ticket_number)
        ticket_list.append(text)

    with open(filename_products, 'w') as fp:
        fp.write('\r\n'.join(product_list))

    with open(filename_tickets, 'w') as fp:
        fp.write('\r\n'.join(ticket_list))

if __name__ == "__main__":
    main(sys.argv[1:])
