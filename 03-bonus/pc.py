import lldb

def pc(debugger, command, result, internal_dict):
    args = command.split(" ")
    for x in range(int(args[0])):
        debugger.HandleCommand('process continue')

def __lldb_init_module(debugger, internal_dict):
    debugger.HandleCommand('command script add -f pc.pc pc')
