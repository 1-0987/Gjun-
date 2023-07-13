import random


class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left_tree = None
        self.right_tree = None

    def insert(self, data):
        if self.data != data:  # 不重複 (若重複則不動作)
            if data < self.data:  # 欲插入者<root => 加入左子樹
                if self.left_tree:  # 若已有左子樹
                    self.left_tree.insert(data)
                else:
                    self.left_tree = BinarySearchTree(
                        data)  # 若原先無左子樹，則加入者即為左子樹

            else:
                if self.right_tree:  # 若已有右子樹
                    self.right_tree.insert(data)
                else:
                    self.right_tree = BinarySearchTree(data)

    def delete(self, data):
        if data < self.data:
            if self.left_tree:
                self.left_tree = self.left_tree.delete(data)  # 成為新的左子樹
            else:  # 沒有這個數
                print(f"Delete {data} fail: data not found")
            result_tree = self

        elif data > self.data:
            if self.right_tree:
                self.right_tree = self.right_tree.delete(data)  # 成為新的右子樹
            else:  # 沒有這個數
                print(f"Delete {data} fail: data not found")
            result_tree = self

        else:  # data == self.data #需要找人替補原本的空缺
            if self.left_tree == None and self.right_tree == None:  # 情境1:無子樹
                result_tree = None
            elif self.left_tree == None and self.right_tree != None:  # 只有右子樹沒有左
                result_tree = self.right_tree  # 刪掉自己後殘餘子樹變成新的我
            elif self.right_tree == None and self.left_tree != None:  # 只有左子樹沒有右
                result_tree = self.left_tree  # 刪掉自己後殘餘子樹變成新的我
            else:  # 左右子樹都在，找右子樹最小值遞補 (或是可以找左子樹最大值遞補)
                substitute = self.right_tree  # 先賦予右子樹為根結點
                while substitute.left_tree != None:  # 一直找到右子樹中有左葉的(會找到右子樹的最小的)
                    substitute = substitute.left_tree  # 一直找到最小的(最左的子樹)
                self.data = substitute.data  # 新的root
                self.right_tree = self.right_tree.delete(
                    substitute.data)  # 新的右子樹
                result_tree = self
        return result_tree

    def search(self, data):
        if data < self.data:
            is_find = \
                self.left_tree.search(data) if self.left_tree else False
        elif data > self.data:
            is_find = \
                self.right_tree.search(data) if self.right_tree else False
        else:
            is_find = True

        return is_find

    def Travers_preorder(self, root):
        traversal_order = list()
        if root:  # 若存在
            traversal_order.append(root.data)
            traversal_order += self.Travers_preorder(root.left_tree)
            traversal_order += self.Travers_preorder(root.right_tree)

        return traversal_order

    def Travers_inorder(self, root):
        traversal_order = list()
        if root:  # 若存在
            traversal_order += self.Travers_inorder(root.left_tree)
            traversal_order.append(root.data)
            traversal_order += self.Travers_inorder(root.right_tree)

        return traversal_order

    def Travers_postorder(self, root):
        traversal_order = list()
        if root:  # 若存在
            traversal_order += self.Travers_postorder(root.left_tree)
            traversal_order += self.Travers_postorder(root.right_tree)
            traversal_order.append(root.data)

        return traversal_order


if __name__ == '__main__':
    insert_order = random.sample(range(1, 20), 7)  # 1-19選7
    print("Insert Order:", insert_order)

    bst = BinarySearchTree(insert_order[0])
    for data in insert_order[1:]:
        print("Insert:", data)
        bst.insert(data)
    print("PreOrder Traversal:", bst.Travers_preorder(bst))
    print("InOrder Traversal:", bst.Travers_inorder(bst))
    print("PostOrder Traversal:", bst.Travers_postorder(bst))

    # Test Search
    print("Test search start")
    target_must_be_found = random.sample(insert_order, 5)  # 從中找出5個
    for target in target_must_be_found:
        # 法1
        is_find = bst.search(target)
        if is_find == False:
            print("Something goes wrong")
        # 法2
        assert bst.search(target) == True, print(
            "Something goes wrong. by Assert")  # 斷言用法
    target_must_not_be_found = [-1 *
                                sample for sample in random.sample(insert_order, 5)]

    for fake_target in target_must_not_be_found:
        assert bst.search(fake_target) == False, print("Something goes, wrong")

    print("Test search done")

    # bst = BinarySearchTree(5)
    # bst.insert(4)
    # bst.insert(3)
    # bst.insert(2)
    # bst.insert(1)
    # bst.insert(11)
    # bst.insert(10)
    # bst.insert(7)
    # bst.insert(8)
    # bst.delete(5)

    # print("From root:", bst.data)  # root
    # trace_left_tree = bst.left_tree  # 以下為驗算tree程式
    # while trace_left_tree != None:
    #     print("find left tree:", trace_left_tree.data)
    #     trace_left_tree = trace_left_tree.left_tree
    # print("From right child node")
    # trace_right_tree = bst.right_tree  # 以下為驗算tree程式
    # while trace_right_tree != None:
    #     print("find right tree:", trace_right_tree.data)
    #     trace_right_tree = trace_right_tree.left_tree  # 因為本圖形(見照片)

    # print("Search 12: ", bst.search(12))
    # print("Search 11: ", bst.search(11))
