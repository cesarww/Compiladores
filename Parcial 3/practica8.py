import dis

bytecode_print_empty = compile("print('')", "", "exec")
print("Bytecode for print(''):")
print(bytecode_print_empty.co_consts[0])

# Mostrar opcodes
print("\nOpCodes:")
dis.dis(bytecode_print_empty)

bytecode_print_plus_val = compile("print(''+val)", "", "exec")
print("\nOpCodes for print(''+val):")
dis.dis(bytecode_print_plus_val)

bytecode_input = compile("input()", "", "exec")
print("\nOpCodes for input():")
dis.dis(bytecode_input)

bytecode_Input = compile("Input('')", "", "exec")
print("\nOpCodes for Input(''):")
dis.dis(bytecode_Input)

bytecode_Input = compile("Input('')", "", "exec")
print("\nOpCodes for Input(''):")
dis.dis(bytecode_Input)

bytecode_c_assignment = compile("c=a+b", "", "exec")
print("\nOpCodes for c=a+b:")
dis.dis(bytecode_c_assignment)

bytecode_if_statement = compile("if a<b: c=a+b", "", "exec")
print("\nOpCodes for If a<b: c=a+b:")
dis.dis(bytecode_if_statement)