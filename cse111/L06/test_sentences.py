from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase, get_adverb
import random
import pytest


def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["two", "some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners


def test_get_noun():
    # 1. Test the single noun.
    single_nouns = ["bird", "boy", "car", "cat", "child",
                    "dog", "girl", "man", "rabbit", "woman"]
    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.

    for _ in range(20):

        # Call the get_noun function which
        # should return a single noun.
        word = get_noun(1)

        # Verify that the word returned from get_noun
        # is one of the words in the single_nouns list.
        assert word in single_nouns

    # 2. Test the plural nouns.

    plural_nouns = ["birds", "boys", "cars", "cats", "children",
                    "dogs", "girls", "men", "rabbits", "women"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(20):

        # Call the get_noun function which
        # should return a plural noun.
        word = get_noun(2)

        # Verify that the word returned from get_noun
        # is one of the words in the plural_nouns list.
        assert word in plural_nouns


def test_get_verb():
    # 1. Test the past verbs
    past_verbs = ["drank", "ate", "grew", "laughed", "thought",
                  "ran", "slept", "talked", "walked", "wrote"]
    for i in range(20):
        word = get_verb(2, "past")
        assert word in past_verbs

    # 2. Test the present single verbs
    present_verbs_single = ["drinks", "eats", "grows", "laughs", "thinks",
                            "runs", "sleeps", "talks", "walks", "writes"]
    for i in range(20):
        word = get_verb(1, "present")
        assert word in present_verbs_single

    # 3. Test the present plural verbs
    present_verbs_plural = ["drink", "eat", "grow", "laugh", "think",
                            "run", "sleep", "talk", "walk", "write"]
    for i in range(20):
        word = get_verb(2, "present")
        assert word in present_verbs_plural

    # 4. Test the future verbs
    future_verbs = ["will drink", "will eat", "will grow", "will laugh",
                    "will think", "will run", "will sleep", "will talk",
                    "will walk", "will write"]
    for i in range(20):
        word = get_verb(2, "future")
        assert word in future_verbs


def test_get_preposition():
    # 1. Test the get_preposition function
    prepositions = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite",
                    "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]
    for i in range(20):
        word = get_preposition()
        assert word in prepositions


def test_get_prepositional_phrase():
    # 1. Test the get_prepositional_phrase function
    prepositions = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite",
                    "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]
    single_determiners = ["a", "one", "the"]
    plural_determiners = ["two", "some", "many", "the"]
    single_nouns = ["bird", "boy", "car", "cat", "child",
                    "dog", "girl", "man", "rabbit", "woman"]
    plural_nouns = ["birds", "boys", "cars", "cats", "children",
                    "dogs", "girls", "men", "rabbits", "women"]

    # This loop will repeat the statements inside it 10 times.
    for i in range(10):
        single_phrase = get_prepositional_phrase(1).split(" ")
        plural_phrase = get_prepositional_phrase(2).split(" ")

        # Verify that the length of single_phrase and
        # plural_phrase is equal to 3
        assert len(single_phrase) == 3
        assert len(plural_phrase) == 3

        # Verify that the words returned from single_phrase
        # are contained in prepositions, single_determiners,
        # single_nouns
        assert single_phrase[0] in prepositions
        assert single_phrase[1] in single_determiners
        assert single_phrase[2] in single_nouns

        # Verify that the words returned from plural_phrase
        # are contained in prepositions, plural_determiners,
        # plural_nouns
        assert plural_phrase[0] in prepositions
        assert plural_phrase[1] in plural_determiners
        assert plural_phrase[2] in plural_nouns


def test_get_adverb():
    # 1. Test the get_adverb function
    adverbs = ["quickly", "slowly", "prettily", "madly", "eagerly",
               "fiercely", "tiredly", "instantly", "carefully", "loudly",
               "blindly", "randomly"]
    for i in range(20):
        word = get_adverb()
        assert word in adverbs


    # Call the main function that is part of pytest so that the
    # computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
