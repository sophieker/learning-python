def tower_of_hanui(n , start, end, middle): 
    if n==1: 
        print ("Move disk 1 from ",start,"to ",end)
        return
    tower_of_hanui(n-1, start, middle, end) 
    print ("Move disk",n,"from",start,"to",end) 
    tower_of_hanui(n-1, middle, end, start) 

n = 4
tower_of_hanui(n,'A','B','C')
