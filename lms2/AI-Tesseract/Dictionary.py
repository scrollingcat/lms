def Push(SItem):
    Stack=[]
    for i,j in SItem.items()    :
        if j>75:
            Stack.append(i)
    print(Stack)
    print("the no. of elements in the stack is",len(Stack))

Push({"Pen":106,"Pencil":59,"Notebook":80,"Eraser":25})