# Read sample_input file form current DIR
f = open("sample_input.txt", "r")
# Read Number of Employeee
emp_input = int(input())
# declaring dictionary  to store key pair values
input_entry = {}
array = []
# parsing the text file and storing into dictionary
# creating array of Price for further calculation
for data in f:
    data = data.replace('\n','')
    data = data.replace(" ","")
    split_data = data.split(':')
    if len(split_data) > 1:
        input_entry[split_data[1]] = split_data[0]
        int_calue = int(split_data[1])
        array.append(int_calue)

f.close()

out_file = open("sample_output.txt","w")
n = len(array)
# sorting the Array
for i in range(len(array)):
    for j in range(i + 1, len(array)):
        if array[i] > array[j]:
            temp = array[i]
            array[i]=array[j]
            array[j]=temp

if len(array) < emp_input:
    print ("no emp Exceeds ")

min_diff = array[n-1] - array[0]
index = 0
# finding the Sub Array size Emp
# whose difference of first and last should be min

for i in range (len(array) - emp_input + 1):
    if (array[i+emp_input-1] - array[i])< min_diff:
        min_diff = min(min_diff ,  array[i + emp_input - 1] - array[i])
        index= i

out_file.write("\n Here the goodies that are selected for distribution are: \n")
for i in range(emp_input):
    key = str(array[i])
    out_file.write(input_entry[key] + ":" + str(array[i]) + "\n")

out_file.write("\n the difference between the chosen goodie with highest price and the lowest price is : " + str(min_diff) + "\n ")
out_file.close()
