from matplotlib import pyplot as plt
import time

f = plt.figure(1, figsize = (8,8))
ax = f.gca()
ax.set_xlim([0, 10000])
ax.set_ylim([0, 10000])
f.show()

x1 = 0.0
y1 = 0.0
x2 = 10000.0
y2 = 5000.0

dx = x2 - x1
dy = y2 - y1

if dx > dy:
    steps = dx
else:
    steps = dy

x_increment = dx / steps
y_increment = dy / steps

begin = time.time()
for i in range(int(steps)):
    ax.plot(x1, y1, 'ko')
    f.canvas.draw()
    x1 = x1 + x_increment
    y1 = y1 + y_increment
    # raw_input('pause : press any key ...')
end = time.time()
print('Time spent: {}'.format(end - begin))
f.close()