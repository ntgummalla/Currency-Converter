import requests #to make requests to API

def convert_currency():
    input_curr = input("Enter the currency you would like to convert: ").upper()
    desired_curr = input("Enter your desired currency: ").upper()

    while True:
        try:
            amount = float(input("Enter the amount: "))
        except:
            print("The amount must be a numeric value ")
            continue

        if not amount > 0:
            print("Invalid input: Amount must be greater than zero ")
            continue
        else:
            break
    
    # using API to give current currency value, conversion rates, etc.
    url = f"https://api.apilayer.com/fixer/convert?to={desired_curr}&from={input_curr}&amount={amount}"

    payload = {}
    headers= {
    "apikey": "Dc7hvcZ53lslQsCMlU4qlyWFY1WZOJey"
    }
    response = requests.request("GET", url, headers=headers, data = payload) # response from API
    status_code = response.status_code # response of status code should be 200 for no error

    if status_code != 200: # checking for error
        result = response.json()
        print("Error response: " + str(result))
        quit()

    result = response.json() # if there is no error
    print("Conversion Result: " + str(result["result"]))

if __name__ == "__main__": # calling our convert_currency function
    convert_currency()
