import os

secret_token = os.getenv("API_TOKEN")

print(f'token = {secret_token}')

# to test
if secret_token == "123abc":
    print("correct")
else:
    print("incorrect")

    