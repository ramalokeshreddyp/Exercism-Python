def response(hey_bob):
    message= hey_bob.strip()

    # silence
    if message == "":
        return "Fine. Be that way!"

    # yelling (letters, no lowercase,at least one letter)
    is_yelling=message.isupper()

    # question
    is_question=message.endswith("?")

    if is_yelling and is_question:
        return "Calm down, I know what I'm doing!"
    if is_yelling:
        return "Whoa, chill out!"
    if is_question:
        return "Sure."

    return "Whatever."
    
