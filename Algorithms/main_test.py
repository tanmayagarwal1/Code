def TopView(root):
    if not root : raise ValueError 
    def Helper(root, d, lvl, depth):
        if not root : return 
        if not lvl in d :
            d[lvl] = [root.data, depth]
        elif depth < d[lvl][1]:
            d[lvl] = [root.data, dept]
        Helper(root.left, d, lvl - 1, depth + 1)
        Helper(root.right, d, lvl + 1, depth + 1)
    d = {}
    Helper(root, d, 1, 1)
    for i in sorted(d.keys()):
        print(d[i][0])
    return 
    
