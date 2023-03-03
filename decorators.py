
def greet(fx):
    def mfx(*args,**kwargs):
     print("The list has been sorted to:")
     fx(*args,**kwargs)
    return mfx


@greet
def list_sort(list):

    new_list = []
    while my_list:
        min = my_list[0]  
        for x in my_list: 
            if x < min:
                min = x
        new_list.append(min)
        my_list.remove(min)    
    print(new_list)

my_list=[0,10,2,1,8,-1]

list_sort(my_list)