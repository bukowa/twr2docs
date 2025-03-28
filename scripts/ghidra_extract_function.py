import ghidra
import ghidra.util.UndefinedFunction.findFunction
import os


def collect_and_save_functions():
    output_file = "ghidra_functions2.txt"

    refs = getReferencesTo(toAddr(0x10c987f0))
    decomp = ghidra.app.decompiler.DecompInterface()
    decomp.openProgram(currentProgram)
    valid_function_count = 0  # Counter for valid functions

    with open(output_file, "w") as f:
        for ref in refs:
            func = getFunctionContaining(ref.getFromAddress())

            if not func:
                func = ghidra.util.UndefinedFunction.findFunction(currentProgram, ref.getFromAddress(), monitor)

            decomp_results = decomp.decompileFunction(func, 30, monitor)

            if decomp_results.decompileCompleted():
                fn_code = decomp_results.getDecompiledFunction().getC()
                valid_function_count += 1  # Increment valid function count
                f.write("\n### FUNCTION START ###\n")
                f.write(fn_code + "\n### FUNCTION END ###\n\n")
            else:
                f.write("\n### DECOMPILATION FAILED ###\n")
                f.write("Decompilation failed for {} at {}\n".format(func.getName(), func.getEntryPoint()))

        f.write("\nTotal valid functions processed: {}\n".format(valid_function_count))

    print("Results saved to:", os.path.abspath(output_file))


collect_and_save_functions()
