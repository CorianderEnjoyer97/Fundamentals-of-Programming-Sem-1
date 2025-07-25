#Name: Sam Tao Kien
#ID: 00000040604
#Cohort: DH123
#Fundamentals of programming assignment II
#Question 2.

#Write a python program that record on blood pressure of recorded patients.

def main():
  patient_data=[]
  total_bp=0
  count=0


#Start the program with the list of options for user to choose
  while True:
      print("Hello, what whould you like to do today?")
      print("---------------------------------------------------------------------------------------")
      print("1.Add a patient's blood pressure.")
      print("2.Remove a patient's blood pressure, given its position.")
      print("3.Remove a patient's blood pressure, given its value.")
      print("4.Display all blood pressure readings.")
      print("5.Display the sum and average of all blood pressure readings.")
      print("6.Display all the blood pressure readings, sorted in ascending order.")
      print("7.Display the blood pressure which has a value more than 120 mm Hg.")
      print("Q.Quit.")
      print("")
      print("")

#request user to key in option after the listing
      choice=input("Enter the number '1-7' or press 'Q' to Quit:  ")

#Using 'if' condition on every option, and instruct program to operate based on given choice

#If user choose '1'
#Program to ask for patient's blood pressure(in systolic)
      if choice == '1':
          print("")
          print("")
          bp=int(input("Enter the patient's blood pressure (in systolic)(mm Hg): "))
          patient_data.append(bp)
          print("Successfully added to the list.")
          print("")
          print("")


#If user choose '2'
#Program asked to input the position, and remove it from the list based on the position given.
      elif choice == '2':
          print("")
          print("")
          pos=eval(input("Please enter the position number you wish to remove:"))
          if pos<=len(patient_data):
              print(patient_data[pos-1], " mm Hg has removed from the list.")
              print("")
              print("")
              del patient_data[pos-1]
          else:
              print("this patient was not in the list.")
          print("")
          print("")


#If user choose '3'
#Program ask user to input the value, and remove it from the list based on the value given.
      elif choice == '3':
          print("")
          print("")
          val=int(input("Please enter the blood pressure value you wish to remove:"))
          for bp in patient_data:
              if val in patient_data:
                  print(val, " mm Hg has removed from the list.")
          patient_data.remove(val)
          print("")
          print("")


#If user choose '4'
#Program asked to list all the readings.
      elif choice == '4':
          print("")
          print("")
          print("This is your list:")
          for bp in patient_data:
              print("This is a row of patient's blood pressure --> Blood Pressure: {} mm Hg".format(bp))
          print("")
          print("")


#If user choose '5'
#Program asked to calculate the sum and average from the list, and display both calculations.
      elif choice == '5':
          print("")
          print("")
          for bp in patient_data:
              total_bp = total_bp + bp
              count=count+1
              bp_ave= total_bp/count
          print("The total bp from the list is: {} mm Hg.".format(total_bp))
          print("The average of bp from the list is: {0:0.2f} mm Hg.".format(bp_ave))
          print("")
          print("")

#If user choose '6'
#Program asked to arrange all the readings, and display in ascending order.
      elif choice == '6':
          print("")
          print("")
          patient_data.sort()
          print("The list has been sorted.")
          for bp in patient_data:
              print("This is a row of patient's blood pressure --> Blood Pressure: {} mm Hg".format(bp))
          print("")
          print("")


#If user choose '7'
#Program asked to list out the blood pressure that has a value larger than 120 mm Hg.
      elif choice == '7':
          print("")
          print("")
          for bp in patient_data:
              if bp >= 120.0:
                  print ("Patients that has higher bp value than 120 mm Hg are :{} mm Hg".format(bp))
          print("")
          print("")
                  

#If user choose 'Q'
#Program asked to be closed.
      elif choice == 'q':
          print("")
          print("")
          print("Thank you for using.I will now be shutting down.")
          break


#If user type other than the options given
#Program ask user to re-type the answer
      else :
          print("")
          print("")
          print("Invalid option. Please re-type your choice again.")
          print("")
          print("")


main()