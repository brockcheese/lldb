import lldb

def count(debugger, command, result, internal_dict):
    target =  str(debugger.GetSelectedTarget())
    if target:
        print len(target)

def __lldb_init_module(debugger, internal_dict):
    debugger.HandleCommand('command script add -f count.count count')
