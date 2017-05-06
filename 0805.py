def mysteryP( first , second ):
    print first[1:]+second[1:]


def space( str ):
    '''Inserts a space after each letter 
	  in a string'''
    if len(str)<=1:
        return str
    
    elif str[0]==" ":
        return space(str[1:])

    else:
        return str[0]+" "+space(str[1:])
    
def Hamming( s1, s2 ):
    '''Takes two strings of the same length and
    returns the number of positions at which they differ'''
    if len(s1)!=len(s2):
        return -1
    elif s1[0]!=s2[0]:
        return 1+Hamming(s1[1:],s2[1:])
    else:
        return Hamming(s1[1:],s2[1:])
            





