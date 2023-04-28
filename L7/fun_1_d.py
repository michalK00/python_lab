def make_alpha_dict(text):
    return {letter: [word for word in text.split() if letter in word]
            for letter in list(text.replace(" ", ""))}


if __name__ == "__main__":
    print(make_alpha_dict("on i ona"))
