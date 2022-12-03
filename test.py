import matplotlib.pyplot as plt

# function to label the bars so data is easer to read

def labelBar(x,y):
    for i in range(len(x)):
        plt.text(i, y[i]//2, y[i], ha = 'center')

# ------------------ DATA -----------------------------------------
participant = ['one', 'two', 'three', 'four', 'five', 'mean', 'StandDev']

timeData = {'one':210, 'two':180, 'three':182, 'four':185, 'five':150, 'mean':181.4, 'StandDev':21.326}
clickData  = {'one':10, 'two':6, 'three':7, 'four':15, 'five':5, 'mean':8.6 , 'StandDev':4}

time = list(timeData.values())
click = list(clickData.values())

# -----------------------------------------------------------------

# figure one Time Data
plt.figure("Time(s)")

plt.bar(participant, time, color = "pink")
plt.xlabel("Participant")
plt.ylabel("Time to complete tasks (sec)")
plt.title("Time Data")
labelBar(participant, time)

#figure two Click Data
plt.figure("Misclicks")
plt.bar(participant, click, color = "purple")
plt.xlabel("Participant")
plt.ylabel("Number of Misclicks")
plt.title("Misclick Data")
labelBar(participant, click)





plt.show()
