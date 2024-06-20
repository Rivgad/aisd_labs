import random


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_balanced_tree(N: int):
    if N < 0:
        return None

    if N == 0:
        return None

    Nl = N // 2
    Nr = N - Nl - 1
    root = TreeNode(random.randint(0, 99))

    root.left = build_balanced_tree(Nl)
    root.right = build_balanced_tree(Nr)

    return root


def preorder_traversal(root: TreeNode, level: int = 0):
    if root is not None:
        print(" " * level * 5, root.value)
        preorder_traversal(root.left, level + 1)
        preorder_traversal(root.right, level + 1)


def symmetric_traversal(root: TreeNode, level: int = 0):
    if root is not None:
        symmetric_traversal(root.left, level + 1)
        print(" " * level * 5, root.value)
        symmetric_traversal(root.right, level + 1)


def inverse_symmetric_traversal(root: TreeNode, level: int = 0):
    if root is not None:
        inverse_symmetric_traversal(root.right, level + 1)
        print(" " * level * 5, root.value)
        inverse_symmetric_traversal(root.left, level + 1)


def main():
    n = int(input("Введите количество вершин: "))
    root = build_balanced_tree(n)

    # Вывод дерева в прямом порядке
    print("Прямой порядок обхода:")
    preorder_traversal(root)

    # Вывод дерева в симметричном порядке
    print("\nСимметричный порядок обхода:")
    symmetric_traversal(root)

    # Вывод дерева в обратном симметричном порядке
    print("\nОбратно-симметричный порядок обхода:")
    inverse_symmetric_traversal(root)


if __name__ == "__main__":
    main()
