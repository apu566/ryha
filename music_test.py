a_file = open("a.txt", "r")
a_list = a_file.readlines()
a2_list = []
for a in a_list:
    a2_list.append(a.replace("\n",""))
a_set = set(a2_list)
a_file.close()

b_file = open("new.txt" , "r")
b_list = b_file.readlines()
b2_list =[]
for b in b_list:
    b2_list.append(b.replace("\n",""))
b_set = set(b2_list)
b_file.close()


final_file = open("final.txt", "a")
final_list = b_set - a_set
for i in list(final_list):
    final_file.write(i)
    final_file.write('\n')
final_file.close()

