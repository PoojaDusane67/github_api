import pandas as pd
import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")
data = response.json()

df = pd.DataFrame(data)
d=df[["id","namme","email"]]

print(df)