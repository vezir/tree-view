
def subtree(node, relationships):
    return {
        v:subtree(v, relationships[1:])
        for v in [x[0] for x in relationships if x[1] == node]
    }


if __name__ == '__main__':
    # (child, parent) pairs where -1 means no parent
    flat_tree = [
        (1, -1),
        (4, 1),
        (10, 4),
        (11, 4),
        (16, 11),
        (17, 11),
        (24, 17),
        (25, 17),
        (5, 1),
        (8, 5),
        (9, 5),
        (7, 9),
        (12, 9),
        (22, 12),
        (23, 12),
        (2, 23),
        (26, 23),
        (27, 23),
        (20, 9),
        (21, 9),
        (1, -1),
        (4, 1),
        (10, 4),
        (122, 4)
    ]

    sonuc = subtree(-1, flat_tree)
    import json
    tree_str = json.dumps(sonuc, sort_keys=True, indent=4)
    print(tree_str)
    tree_str0 = tree_str
    tree_str = tree_str.replace("\n    ", "\n")
    tree_str = tree_str.replace('"', "")
    tree_str = tree_str.replace(',', "")
    tree_str = tree_str.replace("{", "")
    tree_str = tree_str.replace("}", "")
    tree_str = tree_str.replace("    ", " | ")
    tree_str = tree_str.replace("  ", " ")
    print(tree_str)


    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            return False


    def go(dic, last_key, current_level):
        for key, value in dic.items():
            for i in range(current_level - 1):
                print("| ", end="")

            print(last_key, "= ", end="")
            print(key, ": ", end="")

            if current_level > 0:
                print("")

            if isinstance(value, dict):
                current_level = current_level + 1
                go(value, key, current_level)
            else:
                print(value)


    def go2(dic, last_key, current_level):
        if not bool(dic):
           print("""{}<li>{}</li>""".format(" "*(current_level+1), last_key))
        for key, value in dic.items():
            if isinstance(value, dict):
                if bool(value):
                   print("""{}<li><span class="caret">{}</span>
{}<ul class="nested">""".format(" "*current_level, key, " "*(current_level+1)))
                   current_level = current_level + 1
                go2(value, key, current_level)
                if bool(value):
                   print("""{}</ul>""".format(" "*current_level))
                   print("""{}</li>""".format(" "*(current_level-1)))
            else:
                print(value)

    print("""<ul id="myUL">""")
    go2(sonuc, None, 1)
