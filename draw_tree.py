def draw_tree(node, prefix="", is_left=True):
    if node is not None:
        # Najpierw rysujemy prawe poddrzewo (żeby było "na górze")
        if node.right is not None:
            new_prefix = prefix + ("│   " if is_left else "    ")
            draw_tree(node.right, new_prefix, False)

        # Rysujemy bieżący węzeł
        connector = "└── " if is_left else "┌── "
        print(prefix + connector + str(node.value))

        # Potem lewe poddrzewo (będzie "na dole")
        if node.left is not None:
            new_prefix = prefix + ("    " if is_left else "│   ")
            draw_tree(node.left, new_prefix, True)
