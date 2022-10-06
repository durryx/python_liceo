import matplotlib.pyplot as plt
import numpy as np

def ftot(p,v,t): 
    f = np.zeros(3)
    if np.abs(p[0]) < dist/2:
        f[0] = E*q*np.cos(w*t)
    else:
        f = q*np.cross(v,B)
    return f


def trajectory(dt):
    p = np.array([[0,0,0]])
    v = np.array([[0,0,0]])
    t = np.array([0])
    i = 0
    while np.linalg.norm(p[i]) < radius:
        t = np.append(t, t[i]+dt)
        f = ftot(p[i], v[i], t[i])
        v = np.vstack((v, (v[i] + f / m * dt)))
        p = np.vstack((p, (p[i] + v[i+1] * dt))) 
        i+=1
    
    return p[:i], v[:i], t[:i]


q, m, dist, radius = 1.6e-19, 1.67e-27, 90e-6, 0.1
V=50000
B = np.array([0.0,1.5,0.0])

E = V/dist
w = q*np.linalg.norm(B)/m
p,v,t = trajectory(5e-12)

fig, ax = plt.subplots(figsize=(8,8))
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
plt.plot(p[:,0], p[:,2])
plt.show()
