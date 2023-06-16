def rotated(num):


    res =num[0]
    l,r = 0,len(num)-1



    while l<=r:

        if num[l] < num[r]:
            res = min(res,num[l])
            break


        m =(l+r) //2
        res = min(res,num[m])
        if num[m] >= num[l]:
            l=m+1
        
        else:
            r =m-1
        array =num

    return res




rotated([4,5,6,1,2,3])
            
