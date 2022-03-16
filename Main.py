from urllib import  request
import json


# Get Data and save as a list
def getData():
    with request.urlopen("https://mach-eight.uc.r.appspot.com/") as httpRequest:
        data = httpRequest.read().decode(encoding='UTF-8')
        data = json.loads(data)
        data = data["values"]
        return data


# Validate Number to be an valid Integer
def validateNumber(number):
        try:
            number = int(number)
            return number
        except ValueError:
            return False
  
           
# Algorithm to find matches between players       
def algorithm(data,number):
    match = False
    for i in range(len(data) - 1):
        for j in range( i + 1, len(data) - 1):
            playerA = data[i]
            playerB = data[j]
            if int(playerA["h_in"]) + int(playerB["h_in"]) == number:
                match = True
                print(f'{playerA["first_name"]} {playerA["last_name"]}         {playerB["first_name"]} {playerB["last_name"]}')
    if match == False:
        print("No matches found")


# Function to valid data and run algorithm
def getPairs(number):  
    data = getData()
    number = validateNumber(number)
    if number:
        algorithm(data,number)


if __name__ == "__main__":
    while True:
        number = input("Number: ")
        if validateNumber(number):
            getPairs(number)
            quit()
        else: print("Please, Enter a valid Number (Integer)")
