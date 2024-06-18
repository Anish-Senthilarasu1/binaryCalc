var = input('Give Num ')
var = int(var)
convert = []

while True:
    convert.append(var%2)
    main = var/2
    var = (int(main))
    if var == 0:
        break

reverse = convert.reverse()
print(convert)


