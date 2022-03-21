interest_year=input('Enter the year of interest: ')
highest=-1
lowest=999999999
expectancies=[]
highest_interest=-1
lowest_interest=999999999
largest_drop=0
country_largest_drop=''
year_largest_drop=0
country_input=input('Enter a country to show data: ')
country_input_list=[]

with open('Programming building blocks\life-expectancy.csv') as lines:
    for index, line in enumerate(lines):
        if index==0:
            continue
        line=line.strip().split(',')

        

        if country_input==line[0]:
            country_input_list.append(float(line[3]))

        if index==1:
            prev_expectancy=line[3]
            prev_country=line[0]
            next_expectancy=0
            next_country=''
        elif index>1:
            next_expectancy=line[3]
            next_country=line[0]

        if prev_country==next_country:
            if ((float(prev_expectancy)-float(next_expectancy))>0):
                number=float(prev_expectancy)-float(next_expectancy)
                if number>largest_drop:
                    largest_drop=number
                    country_largest_drop=line[0]
                    year_largest_drop=line[2]

        if index!=1:
            prev_expectancy=next_expectancy
            prev_country=next_country

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

print(f'Largest drop from one year to another: (Country: {country_largest_drop}, Year: {year_largest_drop}, Value: {largest_drop})')
print(f'Values of Country {country_input}: (Minimum: {min(country_input_list)}, Maximum: {max(country_input_list)}, Avarage: {sum(country_input_list)/len(country_input_list)})')