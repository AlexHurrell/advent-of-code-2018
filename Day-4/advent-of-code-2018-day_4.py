f = open("day4input.txt","r") #opens file with name of "test.txt"
myList = []
for line in f:
    myList.append(line)
myList.sort()


guard_histogram = {}

guard_totals = {}

for entry in myList:
#    print(entry)
    my_variable = entry.split(' ')
#    print(my_variable)
    if my_variable[2] == "Guard":
        current_guard = my_variable[3]
        if current_guard not in guard_histogram:

            #print("adding guard " + str(my_variable[3]))
            guard_histogram[current_guard] = [0 for x in range(0,60)]
            guard_totals[current_guard] = 0

#            print(guard_histogram)
    if my_variable[2] == "falls":
        start = int(my_variable[1][3:5])


    if my_variable[2] == "wakes":
        end = int(my_variable[1][3:5])
        temp = guard_histogram[current_guard]
        for x in range(start, end):
            temp[x] += 1
        guard_histogram[current_guard] = temp
        guard_totals[current_guard] += end-start
#       if(current_guard == '#709')
#            print(guard_totals[current_guard])

max_value = 0

for entry in guard_totals:
    if guard_totals[entry] > max_value:
        max_value = guard_totals[entry]
        the_entry = entry

max_value2 = 0
max_value3 = 0

print(the_entry)
print(guard_totals[the_entry])


for i in range(0,len(guard_histogram[the_entry])):
    if guard_histogram[the_entry][i] > max_value2:
        max_value2 = guard_histogram[the_entry][i]
        print(guard_histogram[the_entry][i])
        max_value3 = i


print(max_value3)

print(int(the_entry[1:len(the_entry)]) * max_value3)

max_value2 = 0
max_value3 = 0

for the_entry in guard_histogram:
    for i in range(0,len(guard_histogram[the_entry])):
        if guard_histogram[the_entry][i] > max_value2:
            max_value2 = guard_histogram[the_entry][i]
            print(guard_histogram[the_entry][i])
            max_value3 = i
            guard = the_entry

print(int(guard[1:len(guard)]) * max_value3)
