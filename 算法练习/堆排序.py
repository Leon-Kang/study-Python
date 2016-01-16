def adjust_head(lists, i, size):
    lchild = 2 * i + 1
    rchild = 2 * i + 2
    max = i
    if i < size / 2:
        if lchild < size and lists[lchild] > lists[max]:
            max = lchild
            if rchild < size and lists[rchild] > lists[max]:
                max = rchild
                if max != i:
                    lists[max], lists[i] = lists[i], lists[max]
                    adjust_head(lists, max, size)
    for i in range(0, (size / 2))[::-1]:
        adjust_head(lists, i, size)
    size = len(lists)
    build_heap(lists, size)
    for i in range(0, size)[::-1]:
        lists[0], lists[i] = lists[i], lists[0]
        adjust_head(lists, 0, i)