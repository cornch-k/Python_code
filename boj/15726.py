from ast import Num


Num_List = list(map(int, input().split()))
if(Num_List[0] == min(Num_List)):
    print(int(Num_List[0]/Num_List[1]*Num_List[2]))
elif(Num_List[1] == min(Num_List)):
    print(int(Num_List[0]/Num_List[1]*Num_List[2]))
elif(Num_List[2] == min(Num_List)):
    print(int(Num_List[0]*Num_List[1]/Num_List[2]))