import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(12,3))

q, B, E, m = 1.6e-19, 1.0, 0.3, 1.67e-27

t = np.linspace(0, 0.00000014, 100000)

y=(E/B)*(1-np.cos(q*B*t/m))
x=(E/B)*(t-(m*np.sin(q*B*t/m)/(q*B)))

plt.plot(x,y)
plt.show()
