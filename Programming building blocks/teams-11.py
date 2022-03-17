names=[]
titles=[]
ids=[]
salaries=[]
with open('hr_system.txt') as lines:
    for line in lines:
        line=line.strip()
        line=line.split()
        names.append(line[0])
        titles.append(line[2])
        ids.append(line[1])
        salaries.append(line[3])



for i in range(len(names)):
    paycheck=float(salaries[i])/24
    if titles[i]=='Engineer':
        paycheck+=1000
    print(f'{names[i]} (ID: {ids[i]}), {titles[i]} - ${paycheck:.2f}')