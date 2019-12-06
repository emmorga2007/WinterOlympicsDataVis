import matplotlib.pylab as plt 

names (Sport) = [biathlon, bobsleigh, curling, ice hockey, skating, skiing]
values (Medals) = [2, 22, 50, 350, 159, 40]
plt.figure(figsize=(5, 5))
plt.subplot(131)
plt.bar(names, values)
plt.title("Medals Won by Canada in each Winter Olympic Sport")
plt.show()

names (Sport) = [biathlon, bobsleigh, curling, ice hockey, skating, skiing]
values (Medals) = [2, 22, 50, 350, 159, 40]
plt.figure(figsize=(5, 5))
plt.subplot(131)
plt.scatter(names, values)
plt.title("Medals Won by Canada in each Winter Olympic Sport")
plt.show()
