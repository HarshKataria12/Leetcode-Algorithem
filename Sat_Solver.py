# CNF formula as a list of lists, where each inner list is a clause
# A = 1, B = 2, C = 3, so (A OR NOT B) is [1, -2], (NOT A OR C) is [-1, 3], and (B OR NOT C) is [2, -3]
cnf_formula = [[1, -2], [-1, 3], [2, -3]]
# mapping of variable numbers to names for better readability
var_mapping = {1: True, 3: True}  # Example variable assignment

# function to check if a clause is satisfied by the current variable assignment
def is_clause_satisfied(clause, assignment):
    for literal in clause:
        var = abs(literal)
        is_positive = literal > 0
        if (is_positive and assignment.get(var, False)) or (not is_positive and not assignment.get(var, True)):
            return True
    return False
# function to check if the entire CNF formula is satisfied by the current variable assignment
def formula_satisfied(cnf_formula, assignment):
    return all(is_clause_satisfied(clause, assignment) for clause in cnf_formula)

def find_unit_clause(formula, assignment):

    for clause in formula:

        unassigned = []
        clause_true = False

        for lit in clause:

            var = abs(lit)

            if var in assignment:

                val = assignment[var]

                if (lit > 0 and val) or (lit < 0 and not val):
                    clause_true = True
                    break

            else:
                unassigned.append(lit)

        if not clause_true and len(unassigned) == 1:
            return unassigned[0]

    return None

# OUTPUTS
print("Formula satisfied:",
      formula_satisfied(cnf_formula, var_mapping))

print("Unit clause:",
      find_unit_clause(cnf_formula, var_mapping))