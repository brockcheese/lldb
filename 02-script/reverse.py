import lldb

def reverse(debugger, command, result, internal_dict):
    target =  str(debugger.GetSelectedTarget())
    if target:
        print "FT_" + target[::-1]

def __lldb_init_module(debugger, internal_dict):
    debugger.HandleCommand('command script add -f reverse.reverse reverse')
