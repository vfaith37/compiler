from lexer import lexer
from parser import parser
from validator import validate_code


def interpret(expression):
    # Tokenize the expression
    lexer.input(expression)
    # Get the parsed result
    parsed_result = parser.parse(expression)

    # Validate the expression
    if validate_code(expression):
        try:
            # Return the result of the parsed expression
            return parsed_result
        except Exception as e:
            print(f"Interpreter Error: {e}")
    else:
        print("Interpreter Error: Validation failed.")
        return None


# Example usage
if __name__ == "__main__":
    expression = input("Enter a mathematical expression: ")
    result = interpret(expression)

    if result is not None:
        print(f"Result: {result}")
