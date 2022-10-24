# import numpy


# a = numpy.asarray([ [1,2,3], [4,5,6], [7,8,9] ])
# numpy.savetxt("foo.csv", a, delimiter=",")
import csv

# csv header
fieldnames = ['', '1', '2', '3']

# csv data
rows = [
    {'': 1,
    '1': 1,
    '2': 0,
    '3': 0},
    {'': 2,
    '1': 0,
    '2': 0,
    '3': 1},
    {'': 3,
    '1': 1,
    '2': 1,
    '3': 0}
]

with open('countries.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
