import sys
class TreeNode:
    def __init__(self, value: str):
        self.left: None | TreeNode = None
        self.right: None | TreeNode = None
        self.value = value


def sorted_insert(lst, value, key):
    target_idx = 0
    for i in range(len(lst)):
        target_idx = i
        if key(lst[i]) > key(value):
            break
    lst.insert(target_idx, value)


def encode(inp: str) -> tuple[str, dict[str, str]]:
    if inp == "":
        print("c пустой строкой делать нечего")
        sys.exit()
    output_string = ""
    dictionary = {}
    frequencies = {}
    for chr in inp:
        if chr in frequencies:
            frequencies[chr] += 1
        else:
            frequencies[chr] = 1
    srt = sorted(list(frequencies.items()), key=lambda x: x[1])
    nodes = [(TreeNode(char), value) for (char, value) in srt]

    while len(nodes) > 1:
        s1, s2 = nodes.pop(0), nodes.pop(0)
        node = TreeNode(s1[0].value + s2[0].value)
        node.left = s1[0]
        node.right = s2[0]
        sorted_insert(
            nodes,
            (node,s1[1] + s2[1]),
            lambda x: x[1],
        )
    root = nodes[0][0]
    def walk(node, acc):
        if node.left is None and node.right is None:
            dictionary[node.value] = acc
        else:
            if node.left is not None:
                walk(node.left, acc + "0")
            if node.right is not None:
                walk(node.right, acc + "1")

    walk(root, "")

    for ch in inp:
        output_string += dictionary[ch]
    return (output_string, dictionary)


def decode(encoded: str, table: dict[str, str]) -> str:
    table = list(dict.items(table))
    st = ""
    output_str = ""
    for i in encoded:
        st += i
        for j in range(len(table)):
            if table[j][1] == st:
                output_str += table[j][0]
                st = ""
    return output_str
en = encode("привет мой код я хочу чтоб ты работал")


print(en)
print(decode(en[0], en[1]))
