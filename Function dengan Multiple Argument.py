obj_list = [2, 4, 5, 6]
obj_penambah = [1, 2, 3]

def kali_list(a, b):
    a.extend(b)
    return (a)
      
print(kali_list(obj_list, obj_penambah))
