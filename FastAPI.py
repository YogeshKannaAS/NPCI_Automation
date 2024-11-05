import requests
import pandas as pd
import time
df = pd.read_excel(".\Tamil validation sept25.xlsx")
print(df)
input_column = 'VOICE INPUT'
output_column = 'Output'
i=0
# # Iterate over each row in the DataFrame
for index, row in df.iterrows():
    sentence = row[input_column]
    print(sentence)
    # Define the parameters for the request
    param = {
        'sentence': sentence,
        'language': 'Tamil'
    }
    # Set up the request payload and headers
    payload = param
    headers = {
      'Content-Type': 'application/x-www-form-urlencoded',
      'Accept': 'application/json'
    }
    # Send the POST request
    url = "http://183.82.7.228:9375/"
    response = requests.request("POST", url, headers=headers, data=payload)
    i=i+1
    print(i,"response",response)
    # Store the response in the DataFrame
    print(response.text)
    df.at[index, output_column] = response.text
  
    time.sleep(1)
    
# Save the updated DataFrame back to the Excel file
df.to_excel("./FastAPIresponse_TamilSept25.xlsx", index=False)
print("Responses have been written to the Excel file.")