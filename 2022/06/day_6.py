# Advent of Code 2022
# Day 6

def get_datastream():
    with open("input.txt", 'r') as file:
        datastream = file.read()
    return datastream

def get_packet_start_marker(list):
    for i in range(len(list)-3):
        list2 = list[i:i+4]
        duplicate = False
        for j in list2:
            if list2.count(j) > 1:
                duplicate = True
                break
        if duplicate is False:
            return i + 4

def get_msg_marker(list):
    for i in range(len(list)-13):
        list2 = list[i:i+14]
        duplicate = False
        for j in list2:
            if list2.count(j) > 1:
                duplicate = True
                break
        if duplicate is False:
            return i + 14
        
datastream = get_datastream()
first_packet_start_marker = get_packet_start_marker(datastream)
first_message_start_marker = get_msg_marker(datastream)
print(f"First start of packet marker detected at character: {first_packet_start_marker}")
print(f"First start of message marker detected at character: {first_message_start_marker}")