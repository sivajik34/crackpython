months=["jan","feb","march"]
count=0
for month in months:
    print(count,month)
    count=count+1
for count,month in enumerate(months, start=1):
    print(count,month)
