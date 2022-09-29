# opening the file and reading data
my_file = open("StudentNames.txt", "r")
data = my_file.read()

data_into_list = str(data).replace('\t','').split('\n')

studentList = data_into_list
data_into_list_new = {'Roll No '+str(i+1)+' belongs to':data_into_list[i] for i in range(0, len(data_into_list))}

print('\nYou can can refer to the following names along with the roll numbers given below:')
print(str(data_into_list_new).replace('{','').replace("'",'').replace('}',''))

my_file.close()