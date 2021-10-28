#print table

print("Degrees in Celcius" + "\t" + "Degrees in Fahrenheit")

for cel in range (0, 110, 10):
    #conversion formula and cast to int
    far = int(cel * (9/5) + 32)
    print("\t", cel, "\t\t\t", far)