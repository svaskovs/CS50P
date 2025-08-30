import requests
import sys

api_key = "[Insert your API key here]"

try:
    if len(sys.argv) > 1:
        bcToBuy = float(sys.argv[1])
    else:
        sys.exit("Missing command-line argument")
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    o = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey="+api_key)
except requests.RequestException:
    sys.exit("API error")

price = float(o.json()["data"]["priceUsd"])
print(f"${bcToBuy * price:,.4f}")