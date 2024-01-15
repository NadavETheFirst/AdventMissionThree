with open('inputs.txt','r') as inputs:
    lines = inputs.read().lower().split("\n")

i =0
for line in inputs:
    i+=1
    print(f"line {i}: {line}")