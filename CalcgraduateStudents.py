#Calculates the percentages of graduate and undergraduate students.
graduates = input("Enter the number of graduate students enrolled in the class: ")
graduates = int(graduates)
undergraduates = input("Enter the number of undergraduates students enrolled in the class: ")
undergraduates = int(undergraduates)
totalenrolled = graduates + undergraduates
totalenrolled = int(totalenrolled)
percentofundergrad = (undergraduates/totalenrolled)*100
percentofundergrad = float(percentofundergrad)
percentofgrad = (graduates/totalenrolled)*100
percentofgrad = float(percentofgrad)
print("The percentage of undergraduates students is", percentofundergrad,"%")
print("The percentage of graduates students is", percentofgrad,"%" ) 

