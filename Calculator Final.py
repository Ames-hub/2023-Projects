print("// = Rounded Division\n/ = Unrounded division\n* = Multiplication\n- = Subtraction\n+ = Addition\n** = Exponent\n% = Modulus")
problem = input("Enter a problem: ")

for i in problem:
    if i == "x":
        problem = problem.replace("x", "*")
for i in problem:
    if i.isalpha():
        exit("Error: Letters not allowed")

print(eval(problem))