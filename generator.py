import random

def generate_arithmetics():
    operation = random.choice(['+', '-', '*', '/'])
    
    operand1 = random.randint(1, 100)
    operand2 = random.randint(1, 100)
    

    if operation == '+':
        problem = f"{operand1} + {operand2} = "
        answer = operand1 + operand2
    elif operation == '-':
        problem = f"{operand1} - {operand2} = "
        answer = operand1 - operand2
    elif operation == '*':
        problem = f"{operand1} * {operand2} = "
        answer = operand1 * operand2
    else:
        # whole numbers only
        while operand1 % operand2 != 0:
            operand1 = random.randint(1, 100)
            operand2 = random.randint(1, 100)
        problem = f"{operand1} / {operand2} = "
        answer = operand1 // operand2
    
    return problem, answer

# Generate 5 algebra problems
for _ in range(5):
    problem, answer = generate_arithmetics()
    print(problem)