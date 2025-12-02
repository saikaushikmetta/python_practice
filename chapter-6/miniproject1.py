# Mini Project – Countdown Timer (with 1-second gap)
# Goal:
# Print a countdown before something “exciting” happens (like “Launching...” or
# “Happy New Year!”).
# Concepts Used: for loop, range(), and the time module.
import time

print("Countdown starting...")

for i in range(5, 0, -1):   # starts at 5, goes to 1
    print(i)
    time.sleep(1)           # wait for 1 second

print("🎉 Launching...! 🎉")
