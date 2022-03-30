from pathlib import Path
fname = input("\n Enter a valid file name in the format 'filename.txt': ")
count = 0
with open(fname, 'r') as f:
    content = f.read()
    print("\t", content)
    for line in fname:
        words = line.split()
        count += len(words)
print("\n Number of words in the given file are:", count)
