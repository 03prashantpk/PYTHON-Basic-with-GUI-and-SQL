# Day 3 Questions
print("\nDay 3 Questions")
#print("Available Question No's are 1 \n")

print("Find Relationship \n")

# Enter User Name
name = input("Enter Name: ")

# Enter Name to Verify 
your_name = "Prashant"

# Enter Student Name to Verify 
student_name = "Kuldeep"

# Enter Friend Name to Verify 
friend_name = "Asif"

#break line
print("\n")
if name == your_name:
    # Verify User Name 
    print("Yes, It is your Name")

# Check if he/she is a Student
elif name == student_name:
    print("He is your Student")

# Check if he/she is a Friend
elif name == friend_name:
    print("He is your Friend")

else:
    # No relations found with entered Name
    print("Found No Relation with Entered name")

print("\n")
