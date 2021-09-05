# import standard devviation 
from standardDeviation import calculateStandardDeviation

# function to create list from the given file
def createListFromFile(filename):
    fname = filename

    try:
        fhand = open(fname)           # opening the file and storing the control to fhand
    except:
        # Printing in case of error in the file 
        print("can't open the file!!: " + fname)      
        exit()
    #intialization of object list
    objectList = []                   

    for line in fhand:
        if(line[-1] == "\n"):
            line = line[:-1]
        #Spliting records based on the 
        records = list(map(float, line.split(",")))
        for record in records:
            objectList.append(record) 
    #return the list formed
    return objectList
