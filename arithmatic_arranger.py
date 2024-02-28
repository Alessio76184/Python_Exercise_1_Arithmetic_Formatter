def arithmetic_arranger(problems, show_answers=False):
  # Check if there are too many problems
  if len(problems) > 5:
    return  "Error: Too many problems."

  # Defining the paramiter for the arrangement
  first_line = ''
  second_line = ''
  dividers = ''
  results = ''
  max_length = 0

  for problem in problems:
    # Split the problem into numbers and operator
    number1, operation, number2 = problem.split()
    
    # Check if the numbers have only digits
    if not number1.isdigit() or not number2.isdigit():
      return "Error: Numbers must only contain digits."
      
    # Check if the numbers has never more than 4 digits
    if len(number1) > 4 or len(number2) > 4:
      return "Error: Numbers cannot be more than four digits."
    
    number1 = int(number1)
    number2 = int(number2)
    
    number1_length = len(str(number1))
    number2_length = len(str(number2))

    # Determine the maximum length among the two numbers
    max_number_length = max(number1_length, number2_length)

    # Set the maximum length of the problem including operator
    max_length = max_number_length + 2

    # Check for the operator validity and calculate the result of the operation
    if operation =="+":
      result = number1 + number2
    elif operation =="-":
      result = number1 - number2
    else:
      return "Error: Operator must be '+' or '-'."

    # Determining the max length based on which one is the bigger number
    if number1_length > number2_length:
      max_length = number1_length + 2
    else :
      max_length = number2_length + 2

    # Format first number placement | rjust is the allightment which in this case is to the right but there are others as well (ljust(), rjust(), center())
    first_line += str(number1).rjust(max_length) + "    "

    # Format operator and second number
    second_line += operation + str(number2).rjust(max_number_length + 1) + "    "

    # Format divider
    dividers += "-" * max_length + "    "

    # Format result
    results += str(result).rjust(max_length) + "    "

    # Feed entire format to the arranged_problems for printing
    arranged_problems = first_line.rstrip() + "\n" + second_line.rstrip() + "\n" + dividers.rstrip()

    # If the show_answers is True, add the results to the arranged_problems
    if show_answers:
        arranged_problems += "\n" + results.rstrip()
      
  return arranged_problems
