import matplotlib.pyplot as plt

names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

plt.figure(figsize=(9, 3))

plt.subplot(1,3,3)
plt.bar(names, values)
plt.subplot(2,3,4)
plt.scatter(names, values)
plt.subplot(1,3,2)
plt.plot(names, values)
plt.suptitle('Categorical Plotting')
plt.show()