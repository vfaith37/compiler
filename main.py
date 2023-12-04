# main.py
from parser import parser
from validator import validate_code

def compile_code(code):
    if not validate_code(code):
        return None

    try:
        result = parser.parse(code)
        return result
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == '__main__':
    code = "500 / 0.8"

    if compile_code(code) is not None:
        print(f"The square of the number of footsteps is: {compile_code(code) ** 2}")
