def countEmail():
    # This first line is provided for you
    counter = {}
    max = 0
    email = None
    name = input("Enter file:")
    if len(name) < 1 : name = "mbox-short.txt"
    handle = open(name)
    for line in handle:
        if line.startswith("From:"):
            line = line.split()
            try:
                if line[1] not in counter: counter[line[1]] = 1
                else: counter[line[1]] = counter[line[1]] + 1
            except: next
    for key in counter:
        if max == 0 or counter[key] > max: 
            max = counter[key]
            email = key
    print(email, max)

## if you want to test locally run > python counter.py
if __name__ == "__main__":
    countEmail()
