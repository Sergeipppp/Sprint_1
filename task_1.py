time = '1h 45m,360s,25m,30m 120s,2h 60s'
lst = time.replace(' ',',')
lst = lst.split(',')
new_time = 0
for i in lst:
    if 'h' in i:
        i = int(i.replace('h','')) * 60
        new_time += i
    elif 'm' in i:
        i = int(i.replace('m',''))
        new_time += i
    elif 's' in i:
        i = int(i.replace('s','')) // 60
        new_time += i
print(new_time)