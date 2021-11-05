#This loop goes through each row in the table
#  and gets a requested field value

for row in rows:
    currentCity = row.getValue(inField)
    print currentCity
