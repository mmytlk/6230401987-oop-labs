name_tuple = (2, 10, 11, 3)
print("{:30} {}".format("input filenames are", name_tuple))

list_file = []
for n in name_tuple:
    f = 'file_{:04d}'.format(n)
    list_file.append(f)
print("{:30} {}".format("zero padded filenames", (list_file)))

sorting = sorted(list_file)
print("{:30} {}".format("sorted filenames are", (sorting)))
