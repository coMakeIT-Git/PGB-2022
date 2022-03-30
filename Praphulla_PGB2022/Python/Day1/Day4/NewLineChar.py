def remove_newlines(fname):
    fname = input("\n Enter a valid file name in the format 'filename.txt': ")
    f = open(fname).readlines()
    return [s.rstrip('\n') for s in f]
print(remove_newlines("fname"))