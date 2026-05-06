# CNF formula as a list of lists, where each inner list is a clause
# A = 1, B = 2, C = 3, so (A OR NOT B) is [1, -2], (NOT A OR C) is [-1, 3], and (B OR NOT C) is [2, -3]
cnf_formula = [[1, -2], [-1, 3], [2, -3]]
# mapping of variable numbers to names for better readability
var_mapping = {1: True, 2: False, 3: True}

# function to check if a clause is satisfied by the current variable assignment
def is_clause_satisfied(clause, assignment):
    for literal in clause:
        var = abs(literal)
        is_positive = literal > 0
        if (is_positive and assignment.get(var, False)) or (not is_positive and not assignment.get(var, True)):
            return True
    return False

for clause in cnf_formula:
    print(is_clause_satisfied(clause, var_mapping)) # True, because A is True