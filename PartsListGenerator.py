#Part List Generator


'''import'''
import matplotlib as plt
import pandas as pd


'''import parts and hardware stack-ups'''
#see this file for list of stack-ups
from PartsandHardwareStackUps import *


'''function'''
def multiplyDict(hardwareStackUpDict,howManyHardwareStackUps):
    for hardware in hardwareStackUpDict:
        hardwareStackUpDict[hardware] = hardwareStackUpDict[hardware]
        
        
'''stack-up occurances?'''
#multiplyDict(stackUpName, quantity)     <---example
multiplyDict(parts,3)                 
multiplyDict(hardwareStackUpA,6) 
multiplyDict(hardwareStackUpB,4)                    
multiplyDict(hardwareStackUpC,19)    
multiplyDict(hardwareStackUpMixed1,10)       
multiplyDict(hardwareStackUpMixed2,4)  


'''Generate Part List'''
# establish master parts list
partsList = {}

# compile new dictionary parts list
print("compile the parts list from the stack-ups: ")
for stackUp in stackUps:
    for key,value in stackUp.items():
        if key in partsList:
            # if true, add to the current existing key
            partsList[key] += value
            ##print(str(value) + " added to the existing key: " + key)
        else:
            # if not true, create new key and initialize value
            partsList[key] = value
            ##print(str(value) + " added to the new key: " + key)
    #print(partsList)
print("\n")


# pretty print the parts list
def prettyPrintPartsList(masterPartsList):
    print("pretty print the parts list: ")
    #print(masterPartsList)

##    print('\n')
##    for key, value in masterPartsList.items():
##        print(key + "," + str(value))

    print('\n')
    sortedPartsList = sorted(partsList.items())
    for x in sortedPartsList:
       print(x)

    
prettyPrintPartsList(partsList)


'''Export to Excel'''
partsList = pd.Series(partsList)
writer = pd.ExcelWriter('Parts List.xlsx')
partsList.to_excel(writer, 'Sheet1')
writer.save()
print('successfully exported into an excel file')


'''Visualization'''
partsList.rename(index='part',columns={'gty'})
partsListFig = partsList.plot.barh()
