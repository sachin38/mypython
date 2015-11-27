from sys import argv #imports argv from command

script, filename = argv #Here first argv is named script and seond argv is named filename

txt = open(filename) #this will open file which you gave as argument

print "Here's your file %r:" % filename #this will print name  file which you gave as argv
print txt.read() #this will print the file which you gave as argv

print "I'll also ask you to type it again:" #print the phrase to type it again
file_again = raw_input(">") #this wil again ask for file name

txt_again = open(file_again) #open the file which you gave name of

print txt_again.read() #this will print file which you gave name of

