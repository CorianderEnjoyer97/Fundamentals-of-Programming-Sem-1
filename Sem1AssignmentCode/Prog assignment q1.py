#Name: Sam Tao Kien
#ID: 00000040604
#Cohort: DH123
#Fundamentals of programming assignment II
#Question 1.
#Write a python program that save the name of recorded patients.


#Starting point of the program
def main():
  patient_list=[]
  count=0


#Start the program with the list of options for user to choose
  while True:
    print("Hello, what whould you like to do today?")
    print("-------------------------------------------------------------------------------------------")
    print("1.Add a patient's name.")
    print("2.Remove a patient's name, given its position.")
    print("3.Remove a patient's name, given its value.")
    print("4.Display all patients' name.")
    print("5.Search for a patient, report its position if found.")
    print("6.Display all the patients, sorted in ascending order.")
    print("7.Display the the total number of patients.")
    print("8.Display average number of name, longest name and shortest name.")
    print("Q.Quit.")
    print("")
    print("")


#request user to key in option after the listing
    choice=input("Enter the number '1-8' or press 'Q' to Quit:  ")
#Using 'if' condition on every option, and instruct program to operate based on given choice


#If user choose '1'
#Program to ask for patient's name.
    if choice == '1':
      print("")
      print("")
      name=input("Enter patient's name:").upper()
      if name not in patient_list:
          patient_list.append(name)
          print("Successfully added to the list.")
          print("")
          print("")
      else:
          print("The name has already in the list")
          print("")
          print("")


#If user choose '2'
#Program ask user to input the position, and remove it from the list based on the position given.
    elif choice == '2':
      print("")
      print("")
      pos=eval(input("Please enter the position number you wish to remove:"))
      if pos<=len(patient_list):
        print(patient_list[pos-1], " has removed from the list.")
        print("")
        print("")
        del patient_list[pos-1]
      else:
        print("this patient was not in the list.")
        print("")
        print("")


#If user choose '3'
#Program ask user to input the value, and remove it from the list based on the value given.
    elif choice == '3':
      print("")
      print("")
      val=input("Please enter the patient's name you wish to remove:").upper()
      if val in patient_list:
        print(val, " has removed from the list.")
        print("")
        print("")
        patient_list.remove(val)
      else:
        print("this patient was not in the list.")
        print("")
        print("")


#If user choose '4'
#Program asked to list all the names.
    elif choice == '4':
      print("")
      print("")
      print("This is your current patient list:")
      print(patient_list)
      print("")
      print("")


#If user choose '5'
#Program asked search the name given in the list and report its position if found.
    elif choice == '5' :
      print("")
      print("")
      fname= input("Please enter the name you wish to look for:").upper()
      if fname in patient_list:
        index = patient_list.index(fname)+1
        print("The name {} listed in position {}".format(fname,index))
        print("")
        print("")
      else:
        print("The name {} was not in the list".format(fname))
        print("")
        print("")


#If user choose '6'
#Program asked to arrange all the names, and display in ascending order.
    elif choice == '6':
      print("")
      print("")
      patient_list.sort()
      print("The names has been sorted.")
      print(patient_list)
      print("")
      print("")


#If user choose '7'
#Program asked to count and display the number of names in the list.
    elif choice == '7':
      print("")
      print("")
      print("There are {} names in the list".format(len(patient_list)))
      print("")
      print("")


#If user choose '8'
#Program asked to display the longest and shortest name, 
#and calculate the average number of names.
    elif choice == '8':
      print("")
      print("")
      longest_name = max(patient_list,key=len)
      shortest_name = min(patient_list,key=len)
      print("The longest name: {}".format(longest_name))
      print("The shortest name: {}".format(shortest_name))
      num = 0
      for name in patient_list:
        num += len(name)
        count=count+1
      average_name=num/count
      print("The average number of name is {0:0.2f}".format(average_name))
      print("")
      print("")


#If user choose 'Q'
#Program asked to be closed.
    elif choice == 'q':
      print("")
      print("")
      print ("Thank you for using.I will now be shutting down.")
      break


#If user type other than the options given
#Program ask user to re-type the option that needed
    else :
      print("")
      print("")
      print ("Invalid option. Please re-type your choice again.")
      print("")
      print("")

main()