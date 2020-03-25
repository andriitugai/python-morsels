import shlex

def tags_equal(s1, s2):
    """
    s1 and s2 are opening HTML tags.
    Return True if s1 and s2 have the same attributes with the same values.

    Examples:
        >>> tags_equal("<img src=cats.jpg height=40>", "<IMG SRC=Cats.JPG height=40>")
        True
        >>> tags_equal("<img src=dogs.jpg width=99>", "<img src=dogs.jpg width=20>")
        False
        >>> tags_equal("<p>", "<P>")
        True
        >>> tags_equal("<b>", "<p>")
        False
    """
    class Tag(object):
        def __init__(self, ohtml_tag):
            values = shlex.split(ohtml_tag[1:-1].lower())
            self.type = values[0]
            self.attributes = {}
            for attr in values[1:]:
                k, sep, v = attr.partition("=")
                if k not in self.attributes.keys():
                    self.attributes[k] = v

        def __eq__(self, other):
            return self.type == other.type and self.attributes == other.attributes


    return Tag(s1) == Tag(s2)


def main():
    print(tags_equal("<img src=cats.jpg height=40>", "<IMG SRC=Cats.JPG height=40>"))
    print(tags_equal("<img height=40 src=cats.jpg>", "<IMG SRC=Cats.JPG height=40>"))
    print(tags_equal("<img src=dogs.jpg width=99>", "<img src=dogs.jpg width=20>"))
    print(tags_equal("<p>", "<P>"))
    print(tags_equal("<b>", "<p>"))

    print(tags_equal("<LABEL FOR=id_email for=id_username>", "<LABEL FOR=id_email>"))
    print(tags_equal("<LABEL FOR=id_email for=id_username>", "<LABEL FOR=id_username>"))

    print(tags_equal("<input value='hello there'>", '<input value="hello there">'))
    print(tags_equal("<input value=hello>", "<input value='hello'>"))
    print(tags_equal("<input value='hi friend'>", "<input value='hi there'>"))


if __name__ == '__main__':
    main()

