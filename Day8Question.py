# Day 8 Questions

# Question 1 - CI Calculation
import math
print("\nDay 2 Questions")
print("Available Question No's are 1, 2, 3 and 4 \n")

show_question = int(input("Enter Q.no: "))

# Question 1 starts here....

if show_question ==1:
    '''
    Write a Python program to count the number of strings where the string length 
    is 2 or more and the first and last character are same from a given list of 
    strings. 
    '''

    def match_words(words):  
      ctr = 0  
      
      for word in words:  
        if len(word) > 1 and word[0] == word[-1]:  
          ctr += 1  
      return ctr  
      
    print(match_words(['abc', 'zyz', 'abc', '13331']))  

# Question -2 starts here....

elif show_question ==2:
    '''
    Create a tuple of number and print sum of all elements.
    '''

    #Tuple assigned
    tuplee = (10,8,9,8,3,4)
    print("Tuple Values:", tuplee)

    # Sum and Output of the Tuples
    sum_of_tuple = sum(tuplee)
    print("The sum of Tuples are: ", sum_of_tuple)

#question 3 starts here...

elif show_question == 3:
    '''
    Write a python program to remove duplicate from a list
    '''

    my_list = [1,2,2,3,1,4,5,1,2,6]
    myFinallist = []
    for i in my_list:
        if i not in myFinallist:
            myFinallist.append(i)
    print(list(myFinallist))

