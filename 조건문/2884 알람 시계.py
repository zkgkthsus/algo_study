hour, minute = map(int,input().split())
if minute >= 45:
    minute -= 45
else:
    hour -= 1
    if hour < 0:
        hour = 24 + hour
    minute = 60 + (minute - 45)
print(hour, minute)