import random


def dad_joke(request, state_machine):
    paths = (
        "billPath",
        "calendarPath",
        "chickenPath",
        "clydesdalePath",
        "dentistPath",
        "forrestPath",
        "holywaterPath",
        "imDadPath",
        "lifesaversPath",
        "paperPath",
        "peanutsPath",
    )
    return random.choice(paths)
