def spiralOrder(matrix) -> list:
    

    matrix = {x:y for x,y in enumerate(matrix)}
    look = "top"
    res = []

    while matrix:
        if look == "top":
            look = "right"
            for i in matrix:
                res += matrix[i]
                matrix.pop(i)
                break
        
        elif look == "right":
            look = "down"
            for i in matrix:
                res += [matrix[i].pop()]
                
        elif look == "down":
            look = "left"
            temp = matrix.popitem()[1]
            temp.reverse()
            res += temp
                
                
        else:
            look = "top"
            temp = []
            for i in matrix: 
                temp.append(matrix[i].pop(0))
                
            temp.reverse()
            res += temp
            
        matrix = {x:y for x,y in matrix.items() if y}
    return res
                
matrix = [[7],[9],[6]]
spiralOrder(matrix)