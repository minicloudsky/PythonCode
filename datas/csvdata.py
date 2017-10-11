import types
def print_list(li):
    for i in li:
        if (type(i) == list):
            print_list(i)
        else:
            print(i)
lists = [12354,1,2,3,['a','b','c',[67,436,46],['q','w','e']]]
print_list(lists)