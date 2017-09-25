import sys

for filename in sys.argv[1:]:  # for each file listed on the command line
    with open(filename, 'r') as f:  # open the file
        for line in f:  # for each line in the file
            print(line)  # print the line
