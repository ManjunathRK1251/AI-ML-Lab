import matplotlib.pyplot as plt
import numpy as np

X=[0]
Y=[0]

a=np.array([1,0])
b=np.array([[5,0],[0,5]])

'''
y - a
A - b
x - c
xecs - d
'''

# Calculate the inverse of vector b
b=np.linalg.inv(b)
print(f"INV of b : {b}")
print()

#Calculate the dot product of a and b
c = b @ a
print (f"a^(-1).y : {a}")
print()

# Merge vectors a and c
print(f"c : {c}")
print(f"a : {a}")
print()

d = np.array([c,a])
print(f"d: {d}")

#set the origin
origin = [0], [0]

# plt.axis('equal')

# ticklabel_format - Change the ScalarFormatter used by default for linear axes or it customizes the graph
# ScalarFormatter - Format tick values as a number
#tick values - Ticks are the values used to show specific points on the coordinate axis
# style='sci' - turns on scientific notation
# axis = 'both' - Which axis to apply the parameters to.
# scilimits = (m,n) - scientific notation will be used for numbers outside the range 10^m to 10^n
# Use (0,0) to include all numbers.
plt.ticklabel_format(style='sci', axis='both', scilimits=(0,0))

# quiver([X, Y], U, V, [C], **kw)
# X, Y define the arrow locations, U, V define the arrow directions, and C optionally sets the color.
# units = 'xy' , units is used to specify how the arrows are measured
# scale - Number of data units per arrow length unit; a smaller scale parameter makes the arrow longer. Default is None.
plt.quiver(X,Y,c[0],c[1], color='orange',units='xy',scale=0.2)
plt.quiver(X, Y, a[0],a[1], units='xy', scale=0.3)

# setting x and y axes limits
plt.xlim(-2, 5)
plt.ylim(-2, 2.5)
plt.grid()
plt.show()