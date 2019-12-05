import matplotlib.pylab as plt

(Ice Hockey Graphs)
names (Ice Hockey)= [Bronze, Silver, Gold]
values (Medal Count)=[35, 96, 220]
plt.figure(figsize=(5, 5))
plt.subplot(131)
plt.bar(names, values)
plt.ylabel("Medal Count")
plt.xlabel("Medals")
plt.suptitle("Medals Won by Canada for Ice Hockey 1846-2014")
plt.show()


(Skating Graphs)
names (Skating)= [Bronze, Silver, Gold]
values (Medal Count)=[45, 75, 39]
plt.figure(figsize=(5, 5))
plt.subplot(131)
plt.bar(names, values)
plt.ylabel("Medal Count")
plt.xlabel("Medals")
plt.suptitle("Medals Won by Canada for Skating 1846-2014")
plt.show()
