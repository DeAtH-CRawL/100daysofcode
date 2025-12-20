import random
import maths

def mutate(alist):
    if alist is None:
        raise ValueError("alist cannot be None")

    blist=[]
    for item in alist:
        if item is None:
            raise ValueError("item in alist cannot be None")

        new_item = item * 2
        try:
            new_item += random.randint(1,3)
            new_item = maths.add(new_item,item)
        except Exception as e: 
            raise ValueError(f"Error occurred while mutating item {item}: {e}")

        blist.append(new_item)
    print(blist)

