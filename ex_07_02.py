fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    line = line.strip("X-DSPAM-Confidence:")
    line = float(line)
    count = count + 1
    total = total + line
print('Average spam confidence:', total/count)
