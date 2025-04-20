from tabulate import tabulate
Objective={} #Dictionary for objective function variables eg: {'x':2,'y':7,'z':9}
num_vars=int(input("Enter the number of variables: "))
for i in range(num_vars):
    var_name=input(f"Variable {i+1} name: ")
    coeff=float(input(f"coeffecient for {var_name}: "))
    Objective[var_name]=coeff #maps coeff to the variable
obj_type=input("Enter optimization type (max/min): ")
print(tabulate(Objective.items(), headers=["Variable", "Coefficient"], tablefmt="presto", colalign=("center", "center")))
#print(Objective)

Constraints=[] #List for constraint info
num_const=int(input("Enter the number of constraints:"))
for i in range(num_const):
    print(f"\n======Constraint {i+1}======")
    Constraint={}
    for var in Objective:    # "Variable coefficients"
        Constraint[var]=float(input(f"Coefficient for {var}:"))
    Constraint["type"]=input("Choose constraint type (<=, >=, =) ")
    Constraint["rhs"]=float(input("Enter Right-hand side vale: "))
    Constraint["name"]=input("What is this constraint for? (e.g., time, cost, resources): ")
    Constraints.append(Constraint)
print(Constraints)

