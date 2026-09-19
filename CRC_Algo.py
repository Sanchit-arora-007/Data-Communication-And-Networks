def xor(a, b):
    result = ""
    for i in range(1, len(b)):
        result += "0" if a[i] == b[i] else "1"
    return result


def divide(data, divisor):
    pick = len(divisor)
    temp = data[:pick]

    while pick < len(data):
        if temp[0] == "1":
            temp = xor(divisor, temp) + data[pick]
        else:
            temp = xor("0" * pick, temp) + data[pick]
        pick += 1

    if temp[0] == "1":
        temp = xor(divisor, temp)
    else:
        temp = xor("0" * pick, temp)

    return temp


# SENDER
data = input("Enter data bits: ")
divisor = input("Enter divisor bits: ")

appended_data = data + "0" * (len(divisor) - 1)
remainder = divide(appended_data, divisor)

codeword = data + remainder

print("\n--- SENDER ---")
print("Original Data :", data)
print("CRC Remainder :", remainder)
print("Transmitted Data :", codeword)


# RECEIVER
received = input("\nEnter received data bits: ")

remainder = divide(received, divisor)

print("\n--- RECEIVER ---")
print("Received Data :", received)
print("Remainder :", remainder)

if "1" in remainder:
    print("Error detected in received data!")
else:
    print("No error detected.")
    print("Decoded Data :", received[:len(received) - len(divisor) + 1])
