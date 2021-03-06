# coding=utf-8 #使用中文必须加这一句
# import matplotlib.pyplot as plt
# # plt.plot([1,2,3,4])
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16],linewidth=8.0)
# plt.ylabel('some numbers')
# plt.show()
#
# import matplotlib.pyplot as plt
# plt.plot([1,2,3,4], [1,4,9,16], 'ro')
# plt.axis([0, 6, 0, 20])
# plt.show()
#
# import numpy as np
# import matplotlib.pyplot as plt
# # evenly sampled time at 200ms intervals
# t = np.arange(0., 5., 0.2)
# # red dashes, blue squares and green triangles
# plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
# plt.show()
#
# import numpy as np
# import matplotlib.pyplot as plt
# def f(t):
#     return np.exp(-t) * np.cos(2*np.pi*t)
# t1 = np.arange(0.0, 5.0, 0.1)
# t2 = np.arange(0.0, 5.0, 0.02)
# plt.figure(1)
# plt.subplot(221)
# plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
# plt.subplot(222)
# plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
# plt.show()
#
# import matplotlib.pyplot as plt
# plt.figure(1)                # the first figure
# plt.subplot(211)             # the first subplot in the first figure
# plt.plot([1, 2, 3])
# plt.subplot(212)             # the second subplot in the first figure
# plt.plot([4, 5, 6])
# plt.figure(2)                # a second figure
# plt.plot([8, 5, 6])          # creates a subplot(111) by default
# # plt.figure(1)                # figure 1 current; subplot(212) still current
# # plt.subplot(211)             # make subplot(211) in figure1 current
# plt.title('Easy as 1, 2, 3') # subplot 211 title
# plt.show()
#
# ## Working with text
# import numpy as np
# import matplotlib.pyplot as plt
# mu, sigma = 100, 15
# x = mu + sigma * np.random.randn(10000)
# # the histogram of the data
# n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)
# plt.xlabel('Smarts')
# plt.ylabel('Probability')
# plt.title('Histogram of IQ')
# plt.text(60, .025, r'$\mu=100,\ \sigma_i=15$')
# plt.axis([40, 160, 0, 0.03])
# plt.grid(True)
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# ax = plt.subplot(111)
# t = np.arange(0.0, 5.0, 0.01)
# s = np.cos(2*np.pi*t)
# line, = plt.plot(t, s, lw=2)
# plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
#             arrowprops=dict(facecolor='black', shrink=0.3) #shrink表示缩小，shrink=0.1表示缩小为原来的0.9倍，shrink的取值范围为shrink<1(不包括等于)
#             )
# plt.ylim(-2,2)
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# # make up some data in the interval ]0, 1[
# y = np.random.normal(loc=0.5, scale=0.4, size=1000)
# y = y[(y > 0) & (y < 1)]
# y.sort()
# x = np.arange(len(y))
# # plot with various axes scales
# plt.figure(1)
# # linear
# plt.subplot(221)
# plt.plot(x, y)
# plt.yscale('linear')
# plt.title('linear')
# plt.grid(True)
# # log
# plt.subplot(222)
# plt.plot(x, y)
# plt.yscale('log')
# plt.title('log')
# plt.grid(True)
# # symmetric log
# plt.subplot(223)
# plt.plot(x, y - y.mean())
# plt.yscale('symlog', linthreshy=0.05)
# plt.title('symlog')
# plt.grid(True)
# # logit
# plt.subplot(224)
# plt.plot(x, y)
# plt.yscale('logit')
# plt.title('logit')
# plt.grid(True)
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
# x, y = np.random.randn(2, 100)
# fig = plt.figure()
# ax1 = fig.add_subplot(211)
# ax1.xcorr(x, y, usevlines=True, maxlags=30, normed=True, lw=2)
# ax1.grid(False)
# ax1.axhline(0, color='black', lw=2)
# ax2 = fig.add_subplot(212, sharex=ax1)
# ax2.acorr(x, usevlines=True, normed=True, maxlags=50, lw=2)
# ax2.grid(True)
# ax2.axhline(0, color='black', lw=2)
# plt.show()
import matplotlib.pyplot as plt

def make_ticklabels_invisible(fig):
    for i, ax in enumerate(fig.axes):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
        for tl in ax.get_xticklabels() + ax.get_yticklabels():
            tl.set_visible(False)


plt.figure(0)
ax1 = plt.subplot2grid((3,3), (0,0), colspan=3)
ax2 = plt.subplot2grid((3,3), (1,0), colspan=2)
ax3 = plt.subplot2grid((3,3), (1, 2), rowspan=2)
ax4 = plt.subplot2grid((3,3), (2, 0))
ax5 = plt.subplot2grid((3,3), (2, 1))

plt.suptitle("subplot2grid")
make_ticklabels_invisible(plt.gcf())
plt.show()
