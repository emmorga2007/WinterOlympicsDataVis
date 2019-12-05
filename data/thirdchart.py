import matplotlib.pylab as plt

(Gold Medals Graph)
names (Gold)= [Ice Hockey, Skating]
values (Gold Medal Count)=[220, 39]

plt.subplot(131)
plt.bar(names, values)
plt.ylabel("Medal Count")
plt.xlabel("Sport")
plt.suptitle("Gold Medals Won by Canada for Ice Hockey and Skating 1846-2014")
plt.show()