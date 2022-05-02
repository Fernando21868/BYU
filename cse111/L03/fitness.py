# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime


def main():
    # Get the user's gender, birthdate, height, and weight.
    gender = input('Please enter your gender (M or F): ')
    birthday = input('Enter your birthdate (YYYY-MM-DD): ')
    pounds = int(input('Enter your weight in U.S. pounds: '))
    inches = int(input('Enter your height in U.S. inches: '))
    # Call the compute_age, kg_from_lb, cm_from_in,
    # body_mass_index, and basal_metabolic_rate functions
    # as needed.
    age = compute_age(birthday)
    weight = kg_from_lb(pounds)
    height = m_from_in(inches)
    bmi = body_mass_index(weight, height)
    bmr = basal_metabolic_rate(gender, weight, height, age)
    # Print the results for the user to see.
    print(f'Age (years): {age}')
    print(f'Weight (kg): {weight}')
    print(f'Height (cm): {height}')
    print(f'Body mass index: {bmi}')
    print(f'Basal metabolic rate (kcal/day): {bmr}')
    pass


def compute_age(birth_str):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored
        as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the
    # person's birthdate in years.
    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
        (birthdate.month == today.month and
            birthdate.day > today.day):
        years -= 1

    return years


def kg_from_lb(pounds):
    """Convert a mass in pounds to kilograms.
    Parameter pounds: a mass in U.S. pounds.
    Return: the mass in kilograms.
    """
    return pounds*0.45359237


def kg_from_stone(stones):
    """Convert a mass in pounds to stones.
    Parameter pounds: a mass in British stones.
    Return: the mass in kilograms.
    """
    return stones*6.35029


def m_from_in(inches):
    """Convert a length in inches to centimeters.
    Parameter inches: a length in inches.
    Return: the length in centimeters.
    """
    return inches*0.0254


def body_mass_index(weight, height):
    """Compute and return a person's body mass index.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
    Return: a person's body mass index.
    """
    return (10_000*weight)/(height**2)


def basal_metabolic_rate(gender, weight, height, age):
    """Compute and return a person's basal metabolic rate.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
        age: a person's age in years.
    Return: a person's basal metabolic rate in kcals per day.
    """
    if gender.upper() == 'M':
        return 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age
    elif gender.upper() == 'F':
        return 447.593 + 9.247 * weight + 3.098 * height - 4.330 * age
    else:
        return 0


# Call the main function so that
# this program will start executing.
main()
