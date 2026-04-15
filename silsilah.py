data_parent = [
    ("alya", "bima"),
    ("alya", "satria"),
    ("bima", "david"),
    ("bima", "emma"),
    ("satria", "yunita"),
    ("satria", "grace"),
]

def get_siblings(target):
    parents = [p for p, c in data_parent if c == target]
    siblings = set ()
    for p in parents:
        children = [c for parent, c in data_parent if parent == p and c != target]
        siblings.update(children)
    return list(siblings)


def get_grandparents(target_cucu):
    result = []
    parents = [p for p, c in data_parent if c == target_cucu]
    for p in parents:
        grandparents = [gp for gp, child in data_parent if child == p]
        result.extend(grandparents)
    return result

print(f"saudara Bima: {get_siblings('bima')}")
print(f"kakek/nenek Emma: {get_grandparents('emma')}")