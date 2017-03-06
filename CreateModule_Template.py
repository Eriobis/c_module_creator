import sys
import time

filename = sys.argv[1]
date = time.strftime("%d/%m/%Y")

print("Creating " + filename + ".c ...")
print("Creating " + filename + ".h ...")

fc = open(filename + ".c","w")
fh = open(filename + ".h","w")

#Write the .c file

fc.write("/****************************************\n\n")
fc.write("File name     : " +filename + ".c\n")
fc.write("Author        : Simon Benoit \n")
fc.write("Creation date : " + date + "\n\n")
fc.write("****************************************/\n\n")

fc.write("\
//****************************************INCLUDE******************************************// \n\n")
fc.write("#include \"" + filename + ".h\"\n\n")
fc.write("\
//****************************************DEFINES******************************************// \n\n\
//****************************************Global Constants*********************************// \n\n\
//****************************************Global Variables*********************************// \n\n\
//****************************************Function Prototypes******************************// \n\n\
//****************************************Local Function***********************************// \n\n\
//****************************************Global Function**********************************// \n\n\
//****************************************Interrupts Handler*******************************// \n\n")


#Write the header file
fh.write("/****************************************\n\n")
fh.write("File name     : " + filename + ".h\n")
fh.write("Author        : Simon Benoit \n")
fh.write("Creation date : " + date + "\n\n")
fh.write("****************************************/\n\n")

fh.write("#ifndef __" + filename.upper() + "_H\n")
fh.write("#define __" + filename.upper() + "_H\n\n\n")
fh.write  ("//****************************************INCLUDE******************************************// \n\n\
//****************************************DEFINES******************************************// \n\n\
//****************************************Global Constants*********************************// \n\n\
//****************************************Global Variables*********************************// \n\n\
//****************************************Global Function Prototype************************// \n\n")
fh.write("#endif // __" + filename.upper() + "_H\n")

fc.close()
fh.close()
