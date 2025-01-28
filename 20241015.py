#
#    01010101    01010101
#    01010011    00110101
#    01001011    00101101
#    01000111    00011101
#    00100111    00011011
#    00010111    00010111
#    00001111    00001111

#   01000000
#   00100000
#   00010000
#   00001000
#   00000100
#   00000010
#   00000001

#%%
def stringIsInRightFormat(string: str) -> bool:
    checkingZeroes = True
    for element in string:
        if checkingZeroes:
            if element == "1":
                checkingZeroes = False
        else:
            if element == "0":
                return False
    return True

#%%
stringIsInRightFormat("0111")  # True

#%%
string = "100"

def minimumSteps(myString: str) -> int:
    changes = 0
    while not stringIsInRightFormat(myString):
        print(f'starting with the string {myString}')
        for i, element in enumerate(myString):
            if element == "0":
                if myString[i-1] == "1":
                    myString[i-1] = "0"
                    myString[i] = "1"
                    changes += 1
                    print(f'changed the string to {myString}')
    return changes

# %%
minimumSteps('100')  # 1
#%%
def minimumSteps(myString: str) -> int:
    changes = 0
    myString = list(myString)  # Convert the string to a list of characters
    
    while not stringIsInRightFormat("".join(myString)):  # Join list back into string for the function check
        print(f'starting with the string {"".join(myString)}')
        
        for i, element in enumerate(myString):
            if element == "0" and i > 0 and myString[i-1] == "1":  # Check boundary to avoid out of range error
                myString[i-1] = "0"
                myString[i] = "1"
                changes += 1
                print(f'changed the string to {"".join(myString)}')
                
    return changes
# %%

minimumSteps('01010101')  # 1
# %%
def minimumSteps(s: str) -> int:
        total_steps = 0
        ones_count = 0
        
        for char in s:
            if char == '1':
                ones_count += 1
            else:  # char == '0'
                total_steps += ones_count
        
        return total_steps
# %%
