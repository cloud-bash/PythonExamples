filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = filenames.copy()
for index, file in enumerate(newfilenames):
    if file[len(file)-3:] == "hpp":
        newfilenames.insert(index, file[:len(file) - 2])
        newfilenames.remove(file)

print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]
#Example found in Coursera: Google IT Automation with Python
