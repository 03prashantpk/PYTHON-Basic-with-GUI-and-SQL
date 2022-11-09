# Pyhton File Handling

# Append File
f = open("Experimental Files/demofile3.txt", "a")

# Write Content On file
f.write("Now the file has more content!\n")

# Save and Close File
f.close()

# Open Read File
f = open("Experimental Files/demofile3.txt", "r")
print(f.read()) 
f.close()

# Overwrite the file (W)
f = open("Experimental Files\demofile3.txt", "w")
f.write("Content Replaced in txt file.\n")
f.close()


# Open Read File After Replacing Content
f = open("Experimental Files/demofile3.txt", "r")
print("\n")
print(f.read()) 
f.close()


