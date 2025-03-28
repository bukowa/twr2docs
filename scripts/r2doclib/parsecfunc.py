import pycparser
from pycparser import c_ast


class FuncCallVisitor(c_ast.NodeVisitor):
    def __init__(self):
        self.functions = []

    def visit_FuncCall(self, node):
        """
        Visits a function call node in the AST.
        Extracts the function name and arguments if the function starts with 'FUN_'.
        """
        if isinstance(node.name, c_ast.ID) and node.name.name.startswith('FUN_'):
            func_name = node.name.name
            args = self.extract_args(node.args)
            self.functions.append((func_name, args))

    def extract_args(self, args_node):
        """
        Extracts arguments from a function call node and returns them as a list.
        """
        args = []
        if args_node:
            for arg in args_node.children():
                # Extract argument value from the node
                arg_node = arg[1]
                if isinstance(arg_node, c_ast.UnaryOp):
                    args.append(arg_node.expr.name)
                # if isinstance(arg_node, c_ast.Constant):
                #     args.append(arg_node.value)
                elif isinstance(arg_node, c_ast.ID):
                    args.append(arg_node.name)
                # else:
                #     args.append(str(arg_node))
                else:
                    args.append(arg_node.value)
        return args


def extract_function_params_from_code(code: str):
    """
    Extracts function names and their parameters from the provided C code.

    Args:
        code (str): The C code to be parsed.

    Returns:
        list: A list of tuples containing function names and their arguments.
    """
    # Parse the C code into an AST
    parser = pycparser.CParser()
    ast = parser.parse(code)

    # Create a visitor instance to visit function call nodes
    visitor = FuncCallVisitor()
    visitor.visit(ast)

    return visitor.functions
