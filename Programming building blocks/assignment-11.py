interest_year=input('Enter the year of interest: ')
highest=-1
lowest=999999999
expectancies=[]
highest_interest=-1
lowest_interest=999999999


with open('life-expectancy.csv') as lines:
    for index, line in enumerate(lines):
        if index==0:
            continue

        line=line.strip().split(',')
        expectancy=float(line[3])

        if expectancy>highest:
            highest=expectancy
            country_h=line[0]
            year_h=line[2]
        
        if expectancy<lowest:
            lowest=expectancy
            country_l=line[0]
            year_l=line[2]

        if interest_year==line[2]:
            expectancies.append(int(expectancy))
            if expectancy>highest_interest:
                highest_interest=expectancy
                country_interest_h=line[0]
        
            if expectancy<lowest_interest:
                lowest_interest=expectancy
                country_interest_l=line[0]
        

print(f'The overall max life expectancy is: {highest} from {country_h} in {year_h}')
print(f'The overall min life expectancy is: {lowest} from {country_l} in {year_l}')
print()

print(f'For the year {interest_year}: ')
print(f'The average life expectancy across all countries was {sum(expectancies)/len(expectancies):.2f}')
print(f'The max life expectancy was in {country_interest_h} with {highest_interest}')
print(f'The max life expectancy was in {country_interest_l} with {lowest_interest}')
