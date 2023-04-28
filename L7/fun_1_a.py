def acronym(words):
    return words[0][0] + acronym(words[1:]) if words else ""


if __name__ == "__main__":
    print(acronym(["Zakład", "Ubezpieczeń", "Społecznych"]))
