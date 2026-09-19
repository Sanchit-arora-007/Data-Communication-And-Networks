def hamming(data):
    m = len(data)
    r = 0

    while 2 ** r < m + r + 1:
        r += 1

    n = m + r
    code = ['0'] * n

    j = 0
    for i in range(1, n + 1):
        if i & (i - 1):
            code[i - 1] = data[j]
            j += 1

    for p in range(r):
        pos = 2 ** p
        parity = 0

        for i in range(1, n + 1):
            if i & pos:
                parity ^= int(code[i - 1])

        code[pos - 1] = str(parity)

    return ''.join(code)


data = input("Enter data bits: ")
code = hamming(data)

print("Hamming Code:", code)

pos = int(input("Enter error position (0 for no error): "))

if pos != 0:
    code = list(code)
    code[pos - 1] = '1' if code[pos - 1] == '0' else '0'
    code = ''.join(code)

    print("Received Code:", code)

    error = 0
    r = 0

    while 2 ** r < len(code) + 1:
        r += 1

    for p in range(r):
        parity = 0
        pos = 2 ** p

        for i in range(1, len(code) + 1):
            if i & pos:
                parity ^= int(code[i - 1])

        if parity:
            error += pos

    if error:
        print("Error at position:", error)

        code = list(code)
        code[error - 1] = '1' if code[error - 1] == '0' else '0'

        print("Corrected Code:", ''.join(code))
    else:
        print("No error detected.")