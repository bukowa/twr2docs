import re
from r2doclib.parsecfunc import extract_function_params_from_code

def extract_function_params(code: str):
    """
    Extracts the parameters passed to any function starting with 'FUN_' from the given code string.
    """
    # _params = re.findall(r'FUN_\w+\s*\(([^)]+)\)', code)[0].replace('\n', '').split(",")
    # _params = [_params.strip() for _params in _params]
    # Adjusted regex to capture everything inside the parentheses correctly
    _params = re.findall(r'FUN_\w+\s*\(([^)]+)\)', code)[0]

    # Split by commas that are outside quotes
    params = re.split(r',\s*(?=(?:[^"]*"[^"]*")*[^"]*$)', _params)
    if len(params) < 5:
        print('s')

    return _params

def _extract_functions_from_ghidra_dump(_filepath):
    """
    Extract functions from the Ghidra dump.
    A file which has multiple functions separated by
    ### FUNCTION START ###
    ### FUNCTION END ###
    """
    with open(_filepath, "r") as f:
        content = f.read()

    _functions = content.split("\n### FUNCTION START ###\n")
    _functions = [fn.split("\n### FUNCTION END ###\n")[0] for fn in _functions if "### FUNCTION END ###" in fn]
    return _functions


def make_conditions_markdown():
    """
    Given ghidra extracted function list, create a markdown file
    with properly documented conditions from the dump.
    """


if __name__ == '__main__':
    print("Extracting functions from Ghidra dump")
    filepath = "./data/events.txt"
    functions = _extract_functions_from_ghidra_dump(filepath)
    for func in functions:
        # Extract function parameters
        params = extract_function_params_from_code(func)
