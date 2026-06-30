import requests

WEBHOOK_URL = "https://discord.com/api/webhooks/1477413896418754732/bsZ5tOHoAWCf1WqhYhvnMeJHYQXTrGmb3Q0uDtlarnkza__vVrXsJxa6eFd3dyZlemqu"
URL = "http://ipinfo.io/ip"  # replace with the website you want

try:
    response = requests.get(URL, timeout=10)
    response.raise_for_status()

    # Send the returned text directly to Discord
    requests.post(
        WEBHOOK_URL,
        data={"content": response.text}
    )

    print("sent")

except Exception as e:
    print(f"Error: {e}")
