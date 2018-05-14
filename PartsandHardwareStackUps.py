""" Parts & Hardware Stack-Up Dictionaries """

print("Parts & Hardware Stack-Up Dictionaries running...\n")

#List parts and hardware below as dictionaries

#this is all made up purely for demonstration...

parts = {
    'motorA':1,
    'motorB':1,
    'bracketA':2,
    'bracketB':2,
    'newNamePlate':1
}

hardwareStackUpA = {
    'bolt-A':1,
    'washer-A':7,
    'bushing-A':1,
    'bushing-A':1,
    'nut-A': 1,
}

hardwareStackUpB = {
    'bolt-B':1,
    'washer-B':1,
    'nut-B':1,
}

hardwareStackUpC = {
    'bolt-C':1,
    'washer-C':2,
    'bushing-C':3,
    'nut-C':1,
}

hardwareStackUpMixed1 = {
    'bolt-A':2,
    'bushing-B':4,
    'washer-C':4,
    'nut-B':1
}

hardwareStackUpMixed2 = {
    'bolt-C':2,
    'bushing-A':4,
    'washer-A':4,
    'nut-B':1
}

#Create list of dictionaries for looping

stackUps = [
    parts,
    hardwareStackUpA,
    hardwareStackUpB,
    hardwareStackUpC,
    hardwareStackUpMixed1,
    hardwareStackUpMixed2
]


print("\nStack-ups successfully loaded\n")

