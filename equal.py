class Sravnenie:
    def chek(str1,str2):
        chk =False
        #print('----')
        for x in range(0,len(str1)):

            if (str1[x]!='_'):
                if(str1[x]==str2[x]):
                    chk=True
                else:
                   # print('----')
                    return False
        return chk        
   