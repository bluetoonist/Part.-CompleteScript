import matplotlib.pyplot as plt
import numpy as np

info = {'4907': 6871, '4624': 1068, '4672': 887, '4904': 146, '4905': 146, '4634': 84, '4648': 82, '4739': 64, '4608': 47, '4902': 47, '5033': 47, '5024': 47, '1100': 46, '4647': 44, '5056': 43, '4735': 34, '4781': 14, '4616': 11, '4738': 8, '4731': 6, '4732': 2, '4720': 1, '4722': 1, '4733': 1, '4724': 1, '4723': 1}

EventId = []
Counter = []

for key,val in info.items():

    if val < 100:
        EventId.append(key)
        Counter.append(val)

# Basic Graph
# plt.title("EventID Counter")
# plt.plot(EventId,Counter)
# plt.legend()
# plt.grid(True)
# plt.show()

# Example Graph 2
# plt.scatter(EventId,Counter,marker='s',c='r')
# plt.legend()
# plt.grid(True)
# plt.show()

plt.figure(figsize=(15,5))
plt.bar(EventId,Counter,width=0.5,color="red")

plt.show()
