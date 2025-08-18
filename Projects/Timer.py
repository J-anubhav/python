import time

my_time = int(input("Enter the time in secods: "))

for counter in reversed(range(1, my_time+1)):
    seconds = counter % 60
    minutes = int(counter/60) %60
    hours = int(counter/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("time's up!!")