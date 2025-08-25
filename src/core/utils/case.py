def to_snake(camel_string: str, *, treat_digits_as_capitals: bool = False) -> str:
    """Converts a camel case or pascal case string to snake case.

    Args:
        camel_string:
            String in camel case or pascal case format. For example myVariable.
        treat_digits_as_capitals:
            Whether to treat digits as capitals. For example myVariable2 would become my_variable_2
            rather than my_variable2.

    Returns:
        The string in snake case format. For example my_variable.
    """

    def check_character(c: str) -> str:
        if c.isupper() or (treat_digits_as_capitals and c.isdigit()):
            return f"_{c}"
        else:
            return c

    return "".join([check_character(c) for c in camel_string]).lstrip("_").lower()
