# list to store file lines
lines = []
# read file
with open(r"E:\demos\files\sample.txt", 'r') as fp:
    # read an store all lines into list
    lines = fp.readlines()

# Write file
with open(r"E:\demos\files\sample.txt", 'w') as fp:
    # iterate each line
    for number, line in enumerate(lines):
        # delete line 5 and 8. or pass any Nth line you want to remove
        # note list index starts from 0
        if number not in [4, 7]:
            fp.write(line)