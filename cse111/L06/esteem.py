def main():
    print_instructions()
    question_1 = calculate_score(input("""1. I feel that I am a person of worth, at least on an
    equal plane with others.
    Enter D, d, a, or A: """))
    question_2 = calculate_score(input("""2. I feel that I have a number of good qualities.
    Enter D, d, a, or A: """))
    question_3 = calculate_score(input("""3. All in all, I am inclined to feel that I am a failure.
    Enter D, d, a, or A: """), 'N')
    question_4 = calculate_score(input("""4. I am able to do things as well as most other people.
    Enter D, d, a, or A: """))
    question_5 = calculate_score(input("""5. I feel I do not have much to be proud of.
    Enter D, d, a, or A: """), 'N')
    question_6 = calculate_score(input("""6. I take a positive attitude toward myself.
    Enter D, d, a, or A: """))
    question_7 = calculate_score(input("""7. On the whole, I am satisfied with myself.
    Enter D, d, a, or A: """))
    question_8 = calculate_score(input("""8. I wish I could have more respect for myself.
    Enter D, d, a, or A: """), 'N')
    question_9 = calculate_score(input("""9. I certainly feel useless at times.
    Enter D, d, a, or A: """), 'N')
    question_10 = calculate_score(input("""10. At times I think I am no good at all.
    Enter D, d, a, or A: """), 'N')

    total_score = question_1+question_2+question_3+question_4 + \
        question_5+question_6+question_7+question_8+question_9+question_10

    print(f"Your score is {total_score}")
    print("""A score below 15 may indicate problematic low self-esteem.""")


def calculate_score(question, order='P'):
    if order == 'N':
        if question == 'D':
            return 3
        elif question == 'd':
            return 2
        elif question == 'a':
            return 1
        elif question == 'A':
            return 0
        else:
            return 0
    else:
        if question == 'D':
            return 0
        elif question == 'd':
            return 1
        elif question == 'a':
            return 2
        elif question == 'A':
            return 3
        else:
            return 0


def print_instructions():
    instructions = """
    This program is an implementation of the Rosenberg
    Self-Esteem Scale. This program will show you ten
    statements that you could possibly apply to yourself.
    Please rate how much you agree with each of the
    statements by responding with one of these four letters:

    D means you strongly disagree with the statement.
    d means you disagree with the statement.
    a means you agree with the statement.
    A means you strongly agree with the statement.
    """
    print(instructions)


if __name__ == "__main__":
    main()
