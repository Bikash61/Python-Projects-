import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "Wait ! Don't Worry life is all about ups and downs we can solve all the problems "


def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response
