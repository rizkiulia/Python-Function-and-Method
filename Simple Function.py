#Contoh Fungsi Sederhana

#fungsi yang menerima satu input argumen berbentuk list dan mempunyai elemen bertipe numeric semua, dimana fungsi tersebut berguna untuk menghitung rata2 dari kumpulan elemen list tersebut. namai fungsi tersebut 'mean_list'

obj_list = [11.25, 18.0, 20.0, 10.75, 9.50]
def mean_list(inp_list):
    # isikan code
    return(sum(inp_list)/len(inp_list))
print(mean_list(obj_list))

