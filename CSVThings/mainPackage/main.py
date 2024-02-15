# main.py

from utilsPackage.utils import *

# Call the function and store what it returns 
#  in a variable called data

if __name__ == "__main__":
    data = read_CSV_file()
    print ("# of rows in dataset:", len(data))
    #print first and last rows in data
    print(data[0])
    print(data[-1])
    # I want a list comprehension expression
    # to pull out all the collision TYpes into a set
    # modify this expression to exclude the blank collision type
    collisionType = {myData[6] for myData in data}
    print ("# of collision type:", len(collisionType))
    print(collisionType)