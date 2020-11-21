class Kangaroo:
    """ 
    Kangaroo class representing a kangaroo!

    attributes = pouch_contents: 
    """

    def __init__(self, pouch_contents=None):
        if pouch_contents == None:
            pouch_contents = []
        self.pouch_contents = pouch_contents

    def put_in_pouch(self, obj):
        self.pouch_contents.append(obj)

    def __str__(self):
        return "Kangaroo with {} in pouch".format(self.pouch_contents)


if __name__ == "__main__":
    kang = Kangaroo()
    roo = Kangaroo()
    kang.put_in_pouch(1)
    kang.put_in_pouch(roo)
    print(kang)
    print(roo)
