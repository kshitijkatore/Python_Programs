# classify a persons age group: Child(<13), Teeenager(13 - 19), Adult(20 -59) , Senior(60+)

age = int(input("Provide me an age: "))

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior")
