import random
import numpy as np
from tkinter import *
import matplotlib.pyplot as plt
import matplotlib.animation as dw
import threading
import sys


def cambiaopinione(mappa):
    x = 0
    y = 0
    for h in range(0, n):
        for k in range(0, n):
            e = random.randint(1, 8)
            if e == 1:
                x = (h - 1) % n
                y = (k + 1) % n
            elif e == 2:
                x = h
                y = (k + 1) % n
            elif e == 3:
                x = (h + 1) % n
                y = (k + 1) % n
            elif e == 4:
                x = (h + 1) % n
                y = k
            elif e == 5:
                x = (h + 1) % n
                y = (k - 1) % n
            elif e == 6:
                x = h
                y = (k - 1) % n
            elif e == 7:
                x = (h - 1) % n
                y = (k - 1) % n
            else:
                x = (h - 1) % n
                y = k
            if x < 0:
                x = n + x
            if y < 0:
                y = n + y
            mappa[h][k] = mappa[x][y]
    return mappa


n = 100
dim = 500
p = np.zeros((n, n))
lato = dim / n
# situazione iniziale
for i in range(0, n):
    for j in range(0, n):
        e = random.randint(1, 2)
        ex = False
        if e == 1:
            ex = True
        p[i, j] = ex
p = np.array(p, dtype=np.bool)
ripetizioni = 10000
finestra = Tk()
finestra.title("Evoluzione del sistema")
foglio = Canvas(finestra, width=dim, height=dim, background="white")
foglio.grid(row=0, column=0)
# ==== crea gli nxn rettangoli ==== #
rettangolo = []
x1 = 0
y1 = 0
rossi = 0
for h in range(0, n):
    colonna = []
    for k in range(0, n):
        if p[h, k] == True:
            colore = "red"
            rossi += 1
        else:
            colore = "yellow"
        colonna.append(foglio.create_rectangle(x1, y1, x1 + lato, y1 + lato, fill=colore, width=0))
        y1 = y1 + lato
    rettangolo.append(colonna)
    x1 = x1 + lato
    y1 = 0
foglio.update()
h = 0
k = 0
p = cambiaopinione(p)
# ====MATPLOTLIB VARIABLES==== #
z = 0
arr = np.arange(0)
x = np.arange(0)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
# ====SAVE TO FILE==== #
f_name = 'evolution.dat'
try:
    with open(f_name, 'a') as f:
        f.write("\t APPENDING NEW SESSION\n")
except FileNotFoundError:
    msg = "can't find file {0}.".format(f_name)
    print(msg)
    with open(f_name, 'w') as f:
        f.write("\t STARTING A NEW SESSION\n")


def save_to_file(x, y, i, end=False):
    if end:
        with open(f_name, 'a') as f:
            f.write("\t ENDED\n")
    else:
        with open(f_name, 'a') as f:
            f.write("[" + str(x) + ", " + str(y) + "]\t IT: " + i + "\n")


def reset(i):
    global arr, z, x, p
    rossi = 0
    for h in range(0, n):
        for k in range(0, n):
            if p[h, k] == True:
                colore = "red"
                rossi += 1
            else:
                colore = "yellow"
            foglio.itemconfig(rettangolo[h][k], fill=colore)
    foglio.update()
    p = cambiaopinione(p)
    # ====PRINT TO CHART==== #
    arr = np.append(arr, int(rossi))
    x = np.append(x, z)
    # print(arr)
    ax.clear()
    if arr[-1] >= n*n/2:
        ax.plot(x, arr, c='r', linewidth=1, label='Red')
    else:
        ax.plot(x, arr, c='y', linewidth=1, label='Yellow')
    ax.axhline(n*n/2, color='c', ls='--', label='Eq. line')
    ax.set_xlim(left=max(0, len(arr) - 50), right=len(arr) + 50)
    ax.grid(True)
    # ax.axes.get_xaxis().set_visible(False)
    plt.ylabel('N° red')
    plt.tight_layout(pad=2.5, w_pad=0.01, h_pad=0.01)
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
               ncol=2, mode="expand", borderaxespad=0.)
    # ====PRINT TO FILE==== #
    ordine = str(i)
    save_to_file(z, arr[-1], ordine)
    z += 1
    if rossi != 0:
        percento = round((rossi / (n ** 2) * 100), 3)
        stpercento = str(percento)
        ax.set_xlabel("Iteration: " + ordine + "    Red %: "+ stpercento)
    titolo = "# iterazione: " + ordine + " % rossi: " + stpercento
    finestra.title(titolo)


try:
    animation = dw.FuncAnimation(fig, reset, interval=0, blit=False)
    plt.show()
    finestra.mainloop()
except KeyboardInterrupt:
    # TODO #
    sys.exit(0)
