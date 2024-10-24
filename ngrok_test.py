# import ngrok python sdk
import ngrok
import time

# Establish connectivity
listener = ngrok.forward(3000, domain="teaching-terribly-gelding.ngrok-free.app", authtoken_from_env=True)

# Output ngrok url to console
print(f"Ingress established at {listener.url()}")

# Keep the listener alive
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Closing listener")