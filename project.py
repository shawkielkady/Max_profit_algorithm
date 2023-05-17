class job:
    def __init__(self, start, finish, profit):
        self.start = start
        self.finish = finish
        self.profit = profit
        
    def __repr__(self):
        return str((self.start, self.finish, self.profit))
def MaxProfitJobs(jobs):
    if not jobs:
        return 0
    jobs.sort(key = lambda x: x.start)
    n=len(jobs)
    tasks=[[] for _ in range(n)]
    maxProfits= [0] * n
    for i in range(n):
        for j in range(i):
            if jobs[j].finish <= jobs[i].start and maxProfits[i] < maxProfits[j]:
                tasks[i]=tasks[j].copy()
                maxProfits[i] = maxProfits[j]
        tasks[i].append(i)
        maxProfits[i] += jobs[i].profit
    return (maxProfits, tasks)
    index = 0
    for i in range(1,n):
        if(maxProfits[i] > maxProfits[index]):
            index=i
    print("The maximum profit is " , max(maxProfits))
    print("The jobs involved in max profit are " , end='')
    for i in tasks[index]:
        print(jobs[i])
    print()
    return (maxProfits, tasks)
if __name__ == '__main__':
    jobs=[job(1,6,6),job(2,5,5),job(5,7,5),job(6,8,3)]
    result = MaxProfitJobs(jobs)
    maxProfits, tasks = result
    index = maxProfits.index(max(maxProfits))
    print("The maximum profit is " , max(maxProfits))
    print("The jobs involved in max profit are " , end='')
    for i in tasks[index]:
        print(jobs[i], end=' ')