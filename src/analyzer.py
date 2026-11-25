from zxcvbn import zxcvbn


def analyze_password(password):
    """
    Analyze the strength of a password using zxcvbn.
    """

    result = zxcvbn(password)

    score = result["score"]
    guesses = result["guesses"]

    feedback = result["feedback"]

    warning = feedback["warning"]
    suggestions = feedback["suggestions"]

    return {
        "score": score,
        "guesses": guesses,
        "warning": warning,
        "suggestions": suggestions
    }