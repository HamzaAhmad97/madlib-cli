import re


def read_template(pth):
    """
    This function takes a file path and returns it's content

    Parameters
    ---------
    pth : string
        The file path

    Exceptions
    ----------
    FileNotFoundException
        If the path is not valid or the file does not exist this function will raise a FileNotFoundException

    Returns
    -------
    string
        The content of the file
    """

    # Did not include a try except block since the provided test required the function to raise a FileNotFoundError
    with open(pth) as f:
        script = f.read()
    return script


def greet(pth):
    """
    This function takes a file path and prints a message in addition to the file's content

    Parameters
    ---------
    pth : string
        The file path

    Returns
    -------
    None
        This function does not return anything
    """
    print(
        f"\nHello, good day!\nI want you to build me a video game by entering whatever you like based on the describtions in between the curly brackets.\n**************************************************************************************************************************\n{read_template(pth)}\n"
    )


def parse_template(text):
    """
    This function takes a string that contains keywords wrapped within curly praces, it exctracts those keywords and returns them in a tuple, as it also returns the string with the keywords removed.

    Parameters
    ---------
    text : string
        The text containing special keywords contained within curly brackets, example: "The {Adjective} car is { Distance } meters away"

    Returns
    -------
    string
        The text with the keywords removed
    tuple
        A tuple containing the exctracted keywords
    """
    regex = r"(\{[^{}]+\})"
    parts = tuple(map(lambda itm: itm.strip("{}"), re.findall(regex, text)))
    stripped = re.sub(regex, "{}", text)
    return (stripped, parts)


def merge(text, parts):
    """
    This function takes a text containing empty curly brackets, and a tuple of strings, and replaces the curly brackets with the strings, then returns the new string

    Parameters
    ---------
    text : string
        The text containing empty curly brackets
    parts : tuple
        A tuple of strings

    Returns
    -------
    string
        A new string with the strings in place of the empty curly brackets
    """
    response = text.format(*parts)
    print(f"\nYour game's description is as follows:\n{response}")
    return response


def wrtie_response(response, pth):
    """
    This function takes string and writes it to a file given its path

    Parameters
    ---------
    response : string
        A piece of text
    pth : string
        The file of the path we want to write to

    Returns
    -------
    None
        This function does not return anything
    """
    with open(pth, "w") as f:
        f.write(response)


def get_parts(parts):
    """
    This function prompts the user to enter a number of responses. The number of inputs will equal the number of strings in the passed tuple

    Parameters
    ---------
    parts : tuple
        A tuple containing a number of strings

    Returns
    -------
    tuple
        This function returns a tuple of inputs (strings)
    """
    entered = []
    for part in parts:
        resp = input(f"{part} ==>  ")
        entered.append(resp)
    return tuple(entered)


if __name__ == "__main__":
    pth = "assets/story.txt"
    greet(pth)
    story = read_template(pth)
    stripped, parts = parse_template(story)
    entered = get_parts(parts)
    response = merge(stripped, entered)
    wrtie_response(response, pth)
