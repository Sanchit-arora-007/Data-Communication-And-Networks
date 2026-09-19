FLAG = "01111110"


def bit_stuff(data):
    stuffed = ""
    count = 0

    for bit in data:
        stuffed += bit

        if bit == "1":
            count += 1

            if count == 5:
                stuffed += "0"
                count = 0
        else:
            count = 0

    return stuffed


def bit_destuff(data):
    destuffed = ""
    count = 0
    i = 0

    while i < len(data):
        bit = data[i]
        destuffed += bit

        if bit == "1":
            count += 1

            if count == 5:
                if i + 1 < len(data) and data[i + 1] == "0":
                    i += 1
                count = 0
        else:
            count = 0

        i += 1

    return destuffed


data = input("Enter an 8-bit data stream: ")

if len(data) != 8 or any(bit not in "01" for bit in data):
    print("Invalid input!")
    print("Please enter exactly 8 bits containing only 0 and 1.")

else:
    stuffed_data = bit_stuff(data)

    final_frame = FLAG + stuffed_data + FLAG

    print("\nSender Side:")
    print("Original data stream :", data)
    print("Flag pattern         :", FLAG)
    print("After bit stuffing   :", stuffed_data)
    print("Final data to send   :", final_frame)

    received_stuffed_data = final_frame[len(FLAG):-len(FLAG)]

    received_data = bit_destuff(received_stuffed_data)

    print("\nReceiver Side:")
    print("Received frame       :", final_frame)
    print("After removing flags :", received_stuffed_data)
    print("After de-stuffing    :", received_data)

    if received_data == data:
        print("\nData received correctly!")
    else:
        print("\nError in data transmission!")