def isPalindrome(word,i=0):
    if(len(word)-i==0):
        #print 'finished'
        return True
    else:
        if(word[i]==word[len(word)-i-1]):
            #print str(i) + 'true'
            return isPalindrome(word,i+1)
        else:
            #print str(i) + 'false'
            return False

def isPalindrome2(word):
    if(len(word)<=1):
        return True
    else:
        if(word[0]==word[-1]):
            return isPalindrome2(word[1:-1])
        else:
            return False