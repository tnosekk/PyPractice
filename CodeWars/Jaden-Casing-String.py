""" codewords: Kata "Jaden Casing Strings"""

not_jaden_cased = "How can mirrors be real if our eyes aren't real"


def jaden_case(text):
    j_list = text.split()
    j_text = [i.capitalize() for i in j_list]
    return " ".join(j_text)


print(jaden_case(not_jaden_cased))
