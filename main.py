from collections import deque
from tabulate import tabulate

# proces = [id, at, bt]
processes = [['P1', 0, 25], ['P2', 5, 10], ['P3', 8, 12], ['P4', 10, 20], ['P5', 12, 15]]
tempProcesses = deque(processes)
tq = 3
comp = []
tat = []

totalTime = 0
while tempProcesses:
    meanBT = 0
    totBT = 0

    if len(tempProcesses) == 0 and current is None:
        break

    if tempProcesses[0][1] > totalTime:
        totalTime += 1
        continue

    current = tempProcesses.popleft()
    totBT = sum(tempProcesses[x][2] for x in range(len(tempProcesses)))

    if len(tempProcesses) > 0:
        meanBT = round(totBT / len(tempProcesses), 2)
    else:
        meanBT = 0

    if len(tempProcesses) == 0:
        meanBT = round(current[2], 2)

    tq = meanBT
    currentrt = round(current[2], 2)
    newtq = round(meanBT / currentrt, 2)

    newrt = round(currentrt - newtq, 2)
    if newrt < 0:
        newrt = 0

    if newrt > 0:
        new_process = [current[0], current[1], newrt]
        tempProcesses.append(new_process)

    if newrt == 0:
        turn_around_time = round(totalTime + current[2] - current[1], 2)
        temp = [current[0], turn_around_time]
        tat.append(temp)
    totalTime += 1

tat.sort()
wt = []
ct = []

for x in range(len(tat)):
    tempwt = round(tat[x][1] - processes[x][2], 2)
    wt.append(tempwt)
    tempct = round(tempwt + processes[x][1] + processes[x][2], 2)
    ct.append(tempct)

headerlist = ["Process ID", "Arrival Time", "Burst Time", "Completion Time", "Waiting Time", "TurnAround Time"]
mainprocessList = []

for x in range(len(processes)):
    temp = [processes[x][0], processes[x][1], processes[x][2], ct[x], wt[x], tat[x][1]]
    mainprocessList.append(temp)

print(tabulate(mainprocessList, headers=headerlist, tablefmt='grid'))

print("")

n = len(tat)

avtat = round(sum(x[1] for x in tat) / n, 2)
print(f"Average Turn Around Time: {avtat}\n")

avwt = round(sum(wt) / n, 2)
print(f"Average Waiting Time: {avwt}")
