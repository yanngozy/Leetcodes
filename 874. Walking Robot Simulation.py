def robotSim(commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        def update_direction(x,d):
            pos = {
                        'N':('W','E'),
                        'S':('E','W'),
                        'E':('N','S'),
                        'W':('S','N')
                  }
            return pos[x][d+2]

        x,y={},{} 
        for a,b in obstacles:
            x[a]=x.get(a,set())
            y[b]=y.get(b,set())
            x[a].add(b)
            y[b].add(a)
            
        pos_x,pos_y = 0,0
        res=0
        dir='N' # initial direction
        
        for k in commands:
            if k in {-1,-2}:
                dir = update_direction(dir,k)
            else:
                if dir=='W':
                    if pos_y in y:
                        for i in range(1,k+1):
                            if pos_x-i in y[pos_y]:
                                i-=1
                                break
                        pos_x-=i
                    else:
                        pos_x-=k

                elif dir=='E':
                    if pos_y in y:
                        for i in range(1,k+1):
                            if pos_x+i in y[pos_y]:
                                i-=1
                                break
                        pos_x+=i
                    else:
                        pos_x+=k
                
                elif dir=='N':
                    if pos_x in x:
                        for i in range(1,k+1):
                            if pos_y+i in x[pos_x]:
                                i-=1
                                break
                        pos_y+=i
                    else:
                        pos_y+=k
                
                elif dir=='S':
                    if pos_x in x:
                        for i in range(1,k+1):
                            if pos_y-i in x[pos_x]:
                                i-=1
                                break
                        pos_y-=i
                    else:
                        pos_y-=k

                res=max(res,pos_x**2+pos_y**2)
        
        return res
