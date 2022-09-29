import numpy
import StudentList
import pandas

rollNo = []
studentName= []
subject = ['English,''Hindi,''Maths,''SST,''Science']
_subject =['English', 'Hindi','Maths', 'SST','Science']
marks = []

#Excel file creation
def studentDatabase(wantToAddSubjectsHere = False, repeatIndex = 0):
    if wantToAddSubjectsHere:
        repeatIndex = len(rollNo)
    colWithDataDf = pandas.DataFrame({'RollNo':pandas.Series(rollNo,dtype=str),
                                      'Student':pandas.Series(studentName,dtype=str),
                                      'Subject':pandas.Series(numpy.repeat([subject],repeatIndex)),
                                      'Marks':pandas.Series([*marks],dtype=str)
                                    })
    return colWithDataDf
with pandas.ExcelWriter("Students.xlsx") as writer:
    studentDatabase().to_excel(writer,sheet_name='Sarthak',index=False)

#Get student name from the list
def GetName(tempVal):
       studentName.append(StudentList.studentList[tempVal])

#Enter and verify data
def InputData(enteringSubjectMarks = False,subjectIndex = 0, rollNumberSelected = 0):

        #Entering Roll No
        if not enteringSubjectMarks:
            #Entering the roll no. in the string format
            tempValR = ''
            tempValR = input('\n' + 'Enter the Roll No: ' + str(tempValR)).replace(' ','')
            if rollNo.__contains__(str(tempValR)):
                print('The Roll no '+str(tempValR)+' is already present in the list! Please enter another roll number')
                InputData()
            #Check if the roll number is an integer only
            while not tempValR.isnumeric() or int(tempValR) > len(StudentList.studentList):
                tempValR = ''
                tempValR = input('The Roll No. should be a integer/whole number only and the value should not be blank and also it should be less than '+str(len(StudentList.studentList)+1)+': ' + str(tempValR)).replace(' ','')
                if rollNo.__contains__(str(tempValR)):
                    print('The Roll no ' + str(tempValR) + ' is already present in the list! Please enter another roll number')
                    InputData()

            #After entering correct roll no. append it in the original list
            rollNo.append(str(tempValR));GetName(int(tempValR)-1)
            print('Roll No. ' + tempValR + ' belongs to: ' + StudentList.studentList[int(tempValR) - 1]+'\n')
            #if everything is correct then enter the "entering marks state" and save the value of roll no. in the rollNumberSelected variable
            rollNumberSelected = tempValR
            enteringSubjectMarks = True
            global tempMarks
            tempMarks = []

        #Entering Subject's marks
        if enteringSubjectMarks == True and subjectIndex < len(_subject):
            tempVal = ''
            #Entering the subject marks in the string format and check if the entered marks are in correct format or not
            try:
               tempVal = float(input('Enter the subject marks of '+str(StudentList.studentList[int(rollNumberSelected)-1])+' in '+_subject[subjectIndex] +': ' + str(tempVal)).replace(' ','')+'\n')

            except ValueError:
               print('Please enter the marks in integer/decimal form only and also do not leave the value blank!\n')
               InputData(True,subjectIndex,rollNumberSelected)

            else:
                #Increase the subject index to enter the marks of next subject according to the sequence in the subject list and append the marks in the marks list
                subjectIndex+=1
                tempMarks.append(str(tempVal).replace('[]',''))
                if subjectIndex == len(_subject):
                    #appending the temporary list into the original marks list
                    marks.append(str(tempMarks).replace('[','').replace(']','').replace("'",''))

                    # #writing the data into the Excel file and saving file
                    _writer = pandas.ExcelWriter('Students.xlsx', engine='openpyxl', mode='a', if_sheet_exists='overlay')
                    worksheet = _writer.sheets['Sarthak']

                    worksheet.column_dimensions['B'].width = 22
                    worksheet.column_dimensions['C'].width = 35
                    worksheet.column_dimensions['D'].width = 25

                    studentDatabase(True).to_excel(_writer, sheet_name='Sarthak',index=False)
                    _writer.save()

                    print('File Saved Successfully!')

                    #Check if all the values from the text file are entered
                    if len(rollNo) == len(StudentList.studentList):
                        print('\nAll values entered, please check the excel file created in the current folder!')
                        exit(0)

                    else:
                        #calling the function again with all values reset to append new data
                        InputData()
                else:
                  #Recurse the function until the marks of all the subjects are entered
                  InputData(True, subjectIndex,rollNumberSelected)
InputData()