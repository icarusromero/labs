invoices = open('CupcakeInvoices.csv')

# for line in invoices:
#     print(line)

# for line in invoices:
#     listed = line.split(',')
#     print(listed[2])

# for line in invoices:
#     listed = line.split(',')
#     listed[3] = float(listed[3])
#     listed[4] = float(listed[4])
#     sum = listed[3] * listed[4]
#     print(sum)

def final_total(inv):
    sums = []
    for line in invoices:
        listed = line.split(',')
        listed[3] = float(listed[3])
        listed[4] = float(listed[4])
        total = listed[3] * listed[4]
        sums.append(total)
    sum = 0
    ele = 0
    while(ele < len(sums)):
        sum = sum + sums[ele]
        ele += 1
    print(sum)

final_total(invoices)

invoices.close()