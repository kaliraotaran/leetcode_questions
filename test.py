def successfulPairs( spells, potions) :
        res =[]
        arr = []
        for i in range(len(spells)):
            arr1= []
            for j in range(len(potions)):
                
                arr1.append(spells[i]*potions[j])
            arr.append(arr1)
        c =0
        for i in arr:
            c =0
            for j in i:
                if j >= 7:
                    c+=1
            res.append(c)
        return res
print(successfulPairs([5,1,3],[1,2,3,4,5] ))