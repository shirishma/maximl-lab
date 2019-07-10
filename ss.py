NO_OF_CHARS = 256
def max(str, n): 
    count = [0] * NO_OF_CHARS 
    for i in range(n): 
        count[ord(str[i])] += 1
      
    cou = 0
    for i in range(NO_OF_CHARS): 
        if (count[i] != 0): 
            cou += 1    
      
    return cou 
  
def small(str): 
  
    n = len(str)      
    max1 = max(str, n) 
    minl = n     
    for pr in range(n): 
        for br in range(n): 
            su = str[pr:br] 
            subslenght = len(su) 
            subjet = max(su,subslenght) 
            if (subslenght < minl and 
                max1 == subjet): 
                minl = subslenght 
  
    return minl 
if __name__ == "__main__": 
    str = input()
    l = small(str); 
    print( l) 
