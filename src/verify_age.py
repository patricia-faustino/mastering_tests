def verify_age(age):
    if age < 18:
        raise ValueError("You must be 18 or older to use this service")
    return "Allowed Access"