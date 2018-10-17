def insertion_bloc(table,param,T):
    l = " "
    q = " "
    K= []
    for i in range (len(param)-1):
        q= q+(param[i])+(" ,")
    q= q+(param[i+1])
    print ("insert into "+ table+" ("+q+") values")
    if (len(T) <100):
     for k in range (len(T)-1):
         print("("+(T[k])+")"+ ",")
     print("("+T[k+1]+")"+";")
    else:
         for k in range (0,100):
           print("("+(T[k])+")"+ ",")
         print("("+T[k+1]+")"+";")
         for j in range (100, len(T)-1):
            K.append(T[j])
         algo1(table,param,K)



