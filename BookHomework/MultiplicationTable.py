y = 1
z = 1
Output = []

while y < 13:
    x = 1
    while x < 13:
        z = x*y
        Output.append(z)
        x = x + 1
    print(Output)
    y =  y + 1
    Output = []