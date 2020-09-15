list_tuple = (2, 123.4567, 10000, 12345.67)

print("file_{:03}: ".format(list_tuple[0]), "{0:5,.2f},".format(list_tuple[1]),
      format(list_tuple[2], "3.2e"),",", format(list_tuple[3], "3.2e"))
