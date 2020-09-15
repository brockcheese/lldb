import lldb

def capitalize(debugger, command, result, internal_dict):
    target = str(debugger.GetSelectedTarget())
    print "FT_" + target.upper()

def __lldb_init_module(debugger, internal_dict):
    debugger.HandleCommand('command script add -f capitalize.capitalize capitalize')
