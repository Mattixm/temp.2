daysinweek= ["monday", "tuesday", "wednesday", "thrusday", "friday", "saturday", "sunday"]
print('input monday temp below')
mon= input()
print('input tuesday temp below')
tues = input()
print('input wednesday temp below')
wed= input()
print('input thursday temp below')
thursday=input()
print('input friday temp below')
fri= input()
print('input saturday temp below')
sat= input()
print('input sunday temp below')
sun= input()
weekdays= [mon, tues,wed, thursday,fri,sat,sun]
counter= -1
for daysinweek in daysinweek:
    counter= counter+1
    print(daysinweek, " tempurature is", weekdays[counter])