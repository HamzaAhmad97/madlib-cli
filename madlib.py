import re


def greet():
    print(
        "Hello, good day!\nI want you to build me a video game by entering whatever you like based on the describtions in between the curly brackets.\n**************************************************************************************************************************"
    )


def read_template(pth):

    try:
        with open(pth) as f:
            script = f.read()
    except FileNotFoundError as err:
        raise err

    return script


def parse_template(text):
    string = "It was a {Adjective} and {Adjective} {Noun}."
    parts = tuple(map(lambda itm: itm.strip("{}"), re.findall(r"{\w+}", string)))
    stripped = re.sub(r"{\w+}", "{}", string)
    return (stripped, parts)


def merge(text, parts):
    result = text.format(*parts)
    return result


def wrtie_response(response):
    try:
      with open('assets/response.txt','w') as f:
        f.write(response)
    except FileNotFoundError:
      print('file not found')


if __name__ == "__main__":
    read_template("assets/dark_and_stormy_night_template.txt")
    parse_template("It was a {Adjective} and {Adjective} {Noun}.")
    merge("It was a {} and {} {}.", ("dark", "stormy", "night"))
    wrtie_response("It was a dark and stormy night.")
