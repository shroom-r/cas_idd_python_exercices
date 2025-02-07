def common2(elem1, elem2):
    commonElements = []
    for e1 in elem1:
        for e2 in elem2:
            if (e1 == e2 and e1 not in commonElements):
                commonElements.append(e1)
    
    return commonElements