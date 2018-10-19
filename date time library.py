#Demonstration of the datetime library

from datetime import datetime

#what the time is atm?
#assigning a variable the current data & time
now = datetime.now()
print(datetime.now())
# we can even extract year month and day and hour and minute and seconds
print(now.year)
print(now.month)
print (now.day)
print (now.hour)
print (now.minute)
print (now.second)

print("\n or add different styles or something:")

print ('%s-%s-%s' % (now.year, now.month, now.day))
print ('%s/%s/%s'%(now.month,now.day,now.year))
print ('%s:%s:%s'%(now.hour,now.minute,now.second))
