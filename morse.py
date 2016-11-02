morse_dict = {
'a':[1,3],
'b':[3,1,1,1],
'c':[3,1,3,1],
'd':[3,1,1],
'e':[1],
'f':[1,1,3,1],
'g':[3,3,1],
'h':[1,1,1,1],
'i':[1,1],
'j':[1,3,3,3],
'k':[3,1,3],
'l':[1,3,1,1],
'm':[3,3],
'n':[3,1],
'o':[3,3,3],
'p':[1,3,3,1],
'q':[3,3,1,3],
'r':[1,3,1],
's':[1,1,1],
't':[3],
'u':[1,1,3],
'v':[1,1,1,3],
'w':[1,3,3],
'x':[3,1,1,3],
'y':[3,1,3,3],
'z':[3,3,1,1]
}

for key, value in morse_dict.items():
    s = ''
    for index in range(len(value)):
        s += "echo 1 > /sys/class/gpio/gpio2/value\nsleep %s\necho 0 > /sys/class/gpio/gpio2/value\n" % str(value[index])
        if index < len(value)-1:
            s += "sleep 1\n"
        else:
            s += "sleep 3\n"
    with open(key,'w') as f:
        f.write(s)
