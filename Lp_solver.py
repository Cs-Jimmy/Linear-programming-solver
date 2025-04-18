
Objective_function={}
num_vars=int(input("Enter the number of variables: "))
for i in range(num_vars):
    var_name=input("Variable name: ")
    coeff=float(input(f"coeffecient for {var_name}: "))
    Objective_function[var_name]=coeff #maps coeff to the variable
obj_type=input("Enter optimization type (max/min): ")
print(Objective_function)

