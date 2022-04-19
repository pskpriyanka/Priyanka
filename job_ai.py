job=[['J1',5,200],['J2',3,180],['J3',3,190],['J4',2,300],['J5',4,120],['J6',2,100]]

def job_scheduling(job,t):
    n=len(job)
    
    for i in range(n):
        for j in range(n-1-i):
            if job[j][2]<job[j+1][2]:
                job[j],job[j+1]=job[j+1],job[j]
               
               
    #to keep track of free time slots            
    result=[False]*t
    
    scheduled_job=['-1']*t
    
    profit=0
    
    for i in range(n):
        for j in range(min(t-1,job[i][1]-1),-1,-1):
            if result[j] is False:
                result[j]=True
                scheduled_job[j]=job[i][0]
                profit=profit+job[i][2]
                break
    print(scheduled_job)
    print(profit)
    
print(job_scheduling(job,3))

