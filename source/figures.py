"""Draw every figure in the notes from the functions and numbers used in the text."""
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import FancyBboxPatch, Polygon

for f in ['/System/Library/Fonts/Supplemental/STIXTwoText.ttf', '/System/Library/Fonts/Supplemental/STIXTwoText-Italic.ttf', '/System/Library/Fonts/Supplemental/STIXGeneralBol.otf']:
    fm.fontManager.addfont(f)
plt.rcParams.update({
    'font.family': 'STIX Two Text', 'mathtext.fontset': 'stix', 'font.size': 8.5,
    'axes.linewidth': 0.8, 'axes.edgecolor': '#222222', 'savefig.dpi': 300,
})

NAVY, RED, TEAL, GOLD, GREY = '#2D5299', '#B8433A', '#00907F', '#B07818', '#8A8F98'
INK, MUTED = '#222222', '#6B7078'
GOLDFILL, REDFILL, GREYFILL, TEALFILL, NAVYFILL = '#EBD9B8', '#EED3D0', '#C9CCD1', '#C7E6E2', '#D3DCEE'
OUT = sys.path[0] + '/figs/'
W2, H2 = 5.85, 2.55   # two panels
W1, H1 = 4.35, 2.85   # one panel


def axes(ax, xlabel, ylabel, title=None, xmax=None, ymax=None, origin=(0, 0)):
    for s in ('top', 'right'):
        ax.spines[s].set_visible(False)
    ax.spines['left'].set_position(('data', origin[0]))
    ax.spines['bottom'].set_position(('data', origin[1]))
    ax.set_xticks([]); ax.set_yticks([])
    if xmax is not None:
        ax.set_xlim(origin[0], xmax)
    if ymax is not None:
        ax.set_ylim(origin[1], ymax)
    ax.plot(1, origin[1], '>', color=INK, ms=4, transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(origin[0], 1, '^', color=INK, ms=4, transform=ax.get_xaxis_transform(), clip_on=False)
    ax.set_xlabel(xlabel, loc='right', labelpad=2)
    ax.set_ylabel(ylabel, loc='top', rotation=0, labelpad=0)
    ax.yaxis.set_label_coords(0.0, 1.03)
    ax.yaxis.label.set_horizontalalignment('left')
    if title:
        ax.set_title(title, loc='right', fontsize=8.5, pad=15)


def xticks(ax, vals, labels=None):
    ax.set_xticks(vals); ax.set_xticklabels(labels if labels else [str(v) for v in vals])
    ax.tick_params(axis='x', length=0, pad=3)


def yticks(ax, vals, labels=None):
    ax.set_yticks(vals); ax.set_yticklabels(labels if labels else [str(v) for v in vals])
    ax.tick_params(axis='y', length=0, pad=3)


def guide(ax, x, y, x0=0, y0=0, color=GREY):
    ax.plot([x, x], [y0, y], ls=(0, (3, 2)), lw=0.7, color=color, zorder=1)
    ax.plot([x0, x], [y, y], ls=(0, (3, 2)), lw=0.7, color=color, zorder=1)


def dot(ax, x, y, color=INK, size=4):
    ax.plot([x], [y], 'o', color=color, ms=size, zorder=5)


def lbl(ax, x, y, s, color=INK, ha='left', va='center', size=8.5, **kw):
    ax.text(x, y, s, color=color, ha=ha, va=va, fontsize=size, **kw)


def note(ax, x, y, s, ha='left', va='center', size=8):
    ax.text(x, y, s, color=MUTED, ha=ha, va=va, fontsize=size, linespacing=1.15)


def arrow(ax, x0, y0, x1, y1, color=GOLD, lw=1.2, both=False):
    ax.annotate('', xy=(x1, y1), xytext=(x0, y0),
                arrowprops=dict(arrowstyle='<|-|>' if both else '-|>', color=color, lw=lw,
                                shrinkA=0, shrinkB=0, mutation_scale=8))


def save(fig, name):
    fig.savefig(OUT + name + '.png', bbox_inches='tight', pad_inches=0.04, facecolor='white')
    plt.close(fig)


def two(**kw):
    return plt.subplots(1, 2, figsize=(W2, H2), gridspec_kw={'wspace': 0.32}, **kw)


def one():
    return plt.subplots(figsize=(W1, H1))


# ---------------------------------------------------------------- Part I
def f1():
    fig, (a, b) = two()
    x = np.linspace(0.05, 20, 400)
    axes(a, r'Quantity of $x$', r'Total utility $U$', '(a) total utility, with $y$ held fixed', 21, 20)
    a.plot(x, 4 * np.sqrt(x), color=NAVY, lw=1.6)
    lbl(a, 12.5, 10.8, r'$U=\sqrt{xy}$', NAVY)
    note(a, 8.5, 5.0, 'each extra unit adds less\nthan the one before')
    axes(b, r'Quantity of $x$', r'Marginal utility $MU_{x}$', '(b) marginal utility', 21, 6)
    x2 = np.linspace(0.12, 20, 400)
    b.plot(x2, 2 / np.sqrt(x2), color=RED, lw=1.6)
    lbl(b, 11.5, 1.2, r'$MU_{x}=\frac{1}{2}\sqrt{y/x}$', RED)
    note(b, 5, 4.2, 'diminishing marginal utility')
    save(fig, 'f1')


def f2():
    fig, (a, b) = two()
    axes(a, r'Quantity of $x$', r'Quantity of $y$', '(a) the budget line and the chosen point', 44, 33)
    x = np.linspace(0, 40, 50)
    a.plot(x, 30 - 0.75 * x, color=NAVY, lw=1.6)
    x2 = np.linspace(0, 20, 50)
    a.plot(x2, 30 - 1.5 * x2, color=NAVY, lw=1.4, ls=(0, (5, 3)))
    guide(a, 20, 15); guide(a, 10, 15)
    dot(a, 20, 15); dot(a, 10, 15)
    lbl(a, 20.8, 16.3, 'A'); lbl(a, 10.8, 16.3, 'B')
    lbl(a, 32, 10, r'$p_{x}=3$', NAVY); lbl(a, 20.8, 2.5, r'$p_{x}=6$', NAVY)
    note(a, 19, 28, 'a rise in $p_x$ pivots the line\nabout the $y$ intercept')
    xticks(a, [10, 20]); yticks(a, [15, 30])
    axes(b, r'Quantity of $x$', r'$V(x)=U^{2}$', '(b) the same problem, one variable', 44, 400)
    v = (120 * x - 3 * x ** 2) / 4
    b.plot(x, v, color=TEAL, lw=1.6)
    guide(b, 20, 300); dot(b, 20, 300)
    note(b, 25, 365, 'the peak is where\n$dV/dx=0$')
    xticks(b, [20], [r'$x^{*}=20$'])
    save(fig, 'f2')


def f3():
    fig, ax = one()
    axes(ax, r'Quantity of $x$', r'Price $p_{x}$', '(c) the demand curve for $x$', 44, 10)
    x = np.linspace(6.2, 42, 300)
    ax.plot(x, 60 / x, color=NAVY, lw=1.6)
    guide(ax, 10, 6); guide(ax, 20, 3); dot(ax, 10, 6); dot(ax, 20, 3)
    lbl(ax, 10.8, 6.5, 'B'); lbl(ax, 20.8, 3.5, 'A')
    lbl(ax, 31, 2.55, r'$p_{x}=\frac{B}{2x}$', NAVY)
    note(ax, 22, 7.6, 'spending stays at $B/2$ at every\nprice, so this curve is unit elastic\nall the way along')
    xticks(ax, [10, 20]); yticks(ax, [3, 6])
    save(fig, 'f3')


def lossav():
    fig, ax = one()
    x = np.linspace(-100, 100, 401)
    v = np.where(x >= 0, np.abs(x) ** 0.88, -2.25 * np.abs(x) ** 0.88)
    ax.set_xlim(-110, 110); ax.set_ylim(-135, 70)
    for s in ('top', 'right'):
        ax.spines[s].set_visible(False)
    ax.spines['left'].set_position(('data', 0)); ax.spines['bottom'].set_position(('data', 0))
    ax.set_xticks([]); ax.set_yticks([])
    ax.plot(x, v, color=NAVY, lw=1.6)
    lbl(ax, 104, 8, 'gains', INK, ha='right', va='bottom')
    lbl(ax, -104, -10, 'losses', INK, ha='left', va='top')
    lbl(ax, 3, 68, 'value', INK, va='top')
    note(ax, 4, -8, 'reference\npoint', va='top')
    guide(ax, 100, 57.5, x0=0); guide(ax, -100, -129.4, x0=0)
    lbl(ax, 100, -6, '+£100', MUTED, ha='center', va='top', size=8)
    lbl(ax, -100, 6, '−£100', MUTED, ha='center', va='bottom', size=8)
    note(ax, 12, -75, 'a loss of £100 weighs about\ntwice as much as a gain of £100')
    save(fig, 'lossav')


def f4():
    fig, (a, b) = two()
    L = np.linspace(0, 16.4, 300)
    Q = 6 * L ** 2 - 0.25 * L ** 3
    axes(a, r'Labour $L$ (capital fixed)', r'Output $Q$', '(a) total product', 18, 600)
    a.plot(L, Q, color=NAVY, lw=1.6)
    dot(a, 8, 256, NAVY); dot(a, 16, 512, NAVY)
    a.plot([8, 8], [0, 256], ls=(0, (3, 2)), lw=0.7, color=GREY)
    note(a, 8.4, 95, 'inflection point:\n$MP_L$ at a maximum')
    note(a, 15.6, 560, r'$MP_{L}=0$', ha='right')
    lbl(a, 11.5, 250, r'$Q=F(K_{0},L)$', NAVY)
    axes(b, r'Labour $L$', r'$MP_{L}$, $AP_{L}$', '(b) marginal and average product', 19.5, 60)
    L2 = np.linspace(0, 16, 300)
    b.axvspan(8, 19.5, color='#F4EEE3', lw=0, zorder=0)
    b.plot(L2, 12 * L2 - 0.75 * L2 ** 2, color=RED, lw=1.6)
    b.plot(L2, 6 * L2 - 0.25 * L2 ** 2, color=TEAL, lw=1.6)
    guide(b, 12, 36); dot(b, 12, 36, TEAL)
    lbl(b, 5.6, 50, r'$MP_{L}$', RED); lbl(b, 16.2, 32, r'$AP_{L}$', TEAL)
    note(b, 12.4, 44, '$MP_L$ cuts $AP_L$\nat its maximum', size=7.5)
    lbl(b, 8.3, 57, 'diminishing marginal returns', GOLD, size=7.5)
    save(fig, 'f4')


TFC5 = 60
def mc5(q): return 0.12 * q ** 2 - 2.4 * q + 15
def avc5(q): return 0.04 * q ** 2 - 1.2 * q + 15
def atc5(q): return avc5(q) + TFC5 / q


def f5():
    fig, (a, b) = two()
    q = np.linspace(2.5, 27, 300)
    axes(a, r'Output $Q$', '£ per unit', '(a) unit costs', 30, 36)
    qm = np.linspace(2.5, 25.4, 300)
    a.plot(qm, mc5(qm), color=RED, lw=1.6)
    qt = q[atc5(q) <= 34]
    a.plot(qt, atc5(qt), color=NAVY, lw=1.6)
    a.plot(q, avc5(q), color=TEAL, lw=1.6); a.plot(q, TFC5 / q, color=GREY, lw=1.4)
    qa = q[np.argmin(atc5(q))]
    guide(a, qa, atc5(qa)); dot(a, qa, atc5(qa), NAVY); dot(a, 15, 6, TEAL)
    lbl(a, 25.6, 33.5, '$MC$', RED); lbl(a, 27.3, atc5(27) + 0.6, '$ATC$', NAVY)
    lbl(a, 27.3, avc5(27) - 0.9, '$AVC$', TEAL); lbl(a, 27.3, TFC5 / 27, '$AFC$', GREY)
    note(a, 5, 35, '$MC$ passes through the\nminimum of $AVC$ and $ATC$', va='top', size=7.5)
    axes(b, r'Output $Q$', '£', '(b) total costs', 30, 420)
    tvc = avc5(q) * q
    b.plot(q, tvc + TFC5, color=NAVY, lw=1.6); b.plot(q, tvc, color=TEAL, lw=1.6)
    b.plot([0, 29], [TFC5, TFC5], color=GREY, lw=1.4)
    t16 = avc5(16) * 16
    arrow(b, 16, t16 + 2, 16, t16 + TFC5 - 2, GOLD, both=True)
    b.annotate('vertical gap $=TFC$', xy=(16, t16 + 30), xytext=(4, 245), color=GOLD, fontsize=8,
               arrowprops=dict(arrowstyle='-', color=GOLD, lw=0.6))
    lbl(b, 27.3, avc5(27) * 27 + TFC5, '$TC$', NAVY); lbl(b, 27.3, avc5(27) * 27, '$TVC$', TEAL)
    lbl(b, 22, TFC5 + 12, '$TFC$', GREY, va='bottom')
    note(b, 3, 380, 'slope of $TC$ = $MC$')
    save(fig, 'f5')


def f6():
    fig, ax = one()
    lr = lambda q: 3 + ((q - 50) / 28) ** 2
    q = np.linspace(4, 98, 400)
    axes(ax, r'Output $Q$', 'Long-run cost per unit', None, 102, 10)
    for qk in (14, 30, 50, 70, 86):
        qq = np.linspace(qk - 15, qk + 15, 100)
        ax.plot(qq, lr(qq) + 0.006 * (qq - qk) ** 2, color=GREY, lw=0.9, ls=(0, (4, 2.5)))
    ax.plot(q, lr(q), color=NAVY, lw=1.8)
    guide(ax, 50, 3); dot(ax, 50, 3, NAVY)
    xticks(ax, [50], ['MES'])
    lbl(ax, 6, 9.6, 'economies\nof scale', GOLD, size=8, va='top')
    lbl(ax, 99, 9.6, 'diseconomies\nof scale', GOLD, size=8, va='top', ha='right')
    lbl(ax, 62, 2.3, '$LRAC$', NAVY)
    note(ax, 53, 1.0, 'dashed: short-run $ATC$ curves,\none for each plant size', size=7.5)
    save(fig, 'f6')


def f7():
    fig, (a, b) = plt.subplots(2, 1, figsize=(W1, 4.5))
    q = np.linspace(0, 120, 100)
    axes(a, r'Output $Q$', '£ per unit', '(a) average and marginal revenue', 128, 13.5)
    a.plot(q, 12 - 0.1 * q, color=NAVY, lw=1.6)
    a.plot(q[q <= 60], 12 - 0.2 * q[q <= 60], color=RED, lw=1.6)
    lbl(a, 80, 6.2, r'$AR=P(Q)$', NAVY); lbl(a, 38, 6.0, '$MR$', RED)
    note(a, 62, 10.6, '$MR$: same intercept,\ntwice the slope')
    xticks(a, [60], ['$a/2b$']); yticks(a, [12], ['$a$'])
    axes(b, r'Output $Q$', '£', '(b) total revenue', 128, 400)
    b.plot(q, 12 * q - 0.1 * q ** 2, color=TEAL, lw=1.6)
    guide(b, 60, 360); dot(b, 60, 360, TEAL)
    note(b, 63, 120, '$TR$ is maximised\nwhere $MR=0$')
    fig.subplots_adjust(hspace=0.6)
    save(fig, 'f7')


def tr8(q): return 14 * q - 0.06 * q ** 2
def tc8(q): return 150 + 6 * q - 0.06 * q ** 2 + 0.00035 * q ** 3
def mc8(q): return 6 - 0.12 * q + 0.00105 * q ** 2
def atc8(q): return tc8(q) / q
QM = np.sqrt(8 / 0.00105)


def f8():
    fig, (a, b) = two()
    q = np.linspace(0, 150, 300)
    axes(a, r'Output $Q$', '£', '(a) totals', 172, 1000)
    a.plot(q, tr8(q), color=TEAL, lw=1.6); a.plot(q, tc8(q), color=RED, lw=1.6)
    arrow(a, QM, tc8(QM) + 8, QM, tr8(QM) - 8, GOLD, both=True)
    a.plot([QM, QM], [0, tc8(QM)], ls=(0, (3, 2)), lw=0.7, color=GREY)
    lbl(a, 152, tr8(150), '$TR$', TEAL); lbl(a, 152, tc8(150), '$TC$', RED)
    lbl(a, QM + 3, 650, 'profit\n£316', GOLD, size=8)
    m = mc8(QM); qt = np.linspace(QM - 20, QM + 20, 20)
    a.plot(qt, tr8(QM) + m * (qt - QM), color=INK, lw=0.9, ls=(0, (2, 2)))
    a.plot(qt, tc8(QM) + m * (qt - QM), color=INK, lw=0.9, ls=(0, (2, 2)))
    note(a, 3, 985, 'parallel tangents:\nslope of $TR$ = slope of $TC$', va='top', size=7)
    qi = 0.12 / 0.0021; dot(a, qi, tc8(qi), RED, size=3.5)
    a.annotate('inflection:\n$MC$ at its minimum', xy=(qi, tc8(qi)), xytext=(100, 170), color=MUTED, fontsize=7,
               arrowprops=dict(arrowstyle='-', color=MUTED, lw=0.6))
    xticks(a, [QM], ['87.3'])
    axes(b, r'Output $Q$', '£ per unit', '(b) margins', 168, 15)
    q2 = np.linspace(0, 116.7, 100)
    b.plot(q2, 14 - 0.12 * q2, color=NAVY, lw=1.6)
    q3 = np.linspace(8, 150, 200)
    b.plot(q3, mc8(q3), color=RED, lw=1.6)
    guide(b, QM, mc8(QM)); dot(b, QM, mc8(QM))
    lbl(b, 118, 0.6, '$MR$', NAVY); lbl(b, 152, mc8(150), '$MC$', RED)
    note(b, 14, 13.4, '$MR>MC$:\nexpand output', size=7.5)
    note(b, 100, 13.4, '$MR<MC$:\ncontract output', size=7.5)
    arrow(b, 30, 12.2, 55, 8.4, GREY, lw=0.8); arrow(b, 118, 12.2, 112, 6.8, GREY, lw=0.8)
    xticks(b, [QM], [r'$Q^{*}=87.3$']); yticks(b, [mc8(QM)], ['3.53'])
    save(fig, 'f8')


# ---------------------------------------------------------------- Part II
def f9():
    fig, (a, b) = two()
    q = np.linspace(0, 110, 50)
    axes(a, r'Quantity $Q$', r'Price $P$', '(a) a change in price', 128, 70)
    a.plot(q, 60 - 0.5 * q, color=NAVY, lw=1.6)
    guide(a, 40, 40); guide(a, 70, 25); dot(a, 40, 40); dot(a, 70, 25)
    lbl(a, 41.5, 43, 'a'); lbl(a, 71.5, 28, 'b')
    a.annotate('', xy=(68, 27), xytext=(42, 41), arrowprops=dict(arrowstyle='-|>', color=GOLD, lw=1.1,
               connectionstyle='arc3,rad=-0.3', mutation_scale=8))
    lbl(a, 72, 56, 'movement along $D$\n(price change only)', GOLD, size=7.5)
    lbl(a, 78, 34, r'$D: P=60-\frac{1}{2}Q$', NAVY, size=7.5)
    xticks(a, [40, 70]); yticks(a, [25, 40])
    axes(b, r'Quantity $Q$', r'Price $P$', '(b) a rise in income, normal good', 128, 82)
    b.plot(q, 60 - 0.5 * q, color=NAVY, lw=1.6)
    b.plot(q, 75 - 0.5 * q, color=NAVY, lw=1.6, ls=(0, (5, 3)))
    for qq in (30, 70):
        arrow(b, qq, 60 - 0.5 * qq + 1, qq, 75 - 0.5 * qq - 1, GOLD)
    lbl(b, 112, 5, '$D_0$', NAVY); lbl(b, 112, 20, '$D_1$', NAVY)
    lbl(b, 4, 16, 'buyers will now pay\n$\\gamma\\Delta Y/\\beta$ more\nat every quantity', GOLD, size=7.5)
    save(fig, 'f9')


def f10():
    fig, (a, b) = two()
    q = np.linspace(0, 100, 50)
    axes(a, r'Quantity $Q$', r'Price $P$', '(a) supply as a marginal-cost schedule', 110, 70)
    a.plot(q, 10 + 0.5 * q, color=RED, lw=1.6)
    guide(a, 30, 25); guide(a, 70, 45); dot(a, 30, 25); dot(a, 70, 45)
    lbl(a, 74, 32, r'$S: P=10+\frac{1}{2}Q$', RED, size=7.5)
    note(a, 4, 64, 'height of $S$ = marginal cost\nof producing that unit', size=7.5)
    yticks(a, [10], [r'$-\mu/\lambda$'])
    axes(b, r'Quantity $Q$', r'Price $P$', '(b) a fall in unit costs', 112, 78)
    b.plot(q, 20 + 0.5 * q, color=RED, lw=1.6)
    b.plot(q, 8 + 0.5 * q, color=RED, lw=1.6, ls=(0, (5, 3)))
    for qq in (35, 80):
        arrow(b, qq, 20 + 0.5 * qq - 1, qq, 8 + 0.5 * qq + 1, GOLD)
    lbl(b, 101, 70, '$S_0$', RED); lbl(b, 101, 58, '$S_1$', RED)
    lbl(b, 4, 74, 'unit costs fall by £$h$ = £12:\nany $Q$ is now supplied\nat a price £12 lower', GOLD, size=7.5, va='top')
    save(fig, 'f10')


def f11():
    fig, (a, b) = two()
    q = np.linspace(0, 110, 50)
    axes(a, r'Quantity $Q$', r'Price $P$', '(a) equilibrium', 120, 70)
    a.plot(q, 60 - 0.5 * q, color=NAVY, lw=1.6); a.plot(q, 10 + 0.5 * q, color=RED, lw=1.6)
    guide(a, 50, 35); dot(a, 50, 35)
    lbl(a, 52, 31, 'E'); lbl(a, 111, 5, '$D$', NAVY); lbl(a, 111, 65, '$S$', RED)
    xticks(a, [50], [r'$Q^{*}=50$']); yticks(a, [35], [r'$P^{*}=35$'])
    axes(b, r'Quantity $Q$', r'Price $P$', '(b) demand rises: the adjustment', 128, 82)
    q2 = np.linspace(0, 115, 50)
    b.plot(q2, 60 - 0.5 * q2, color=NAVY, lw=1.4, ls=(0, (5, 3)))
    b.plot(q2, 75 - 0.5 * q2, color=NAVY, lw=1.6); b.plot(q2, 10 + 0.5 * q2, color=RED, lw=1.6)
    b.plot([50, 80], [35, 35], color=GOLD, lw=3, solid_capstyle='butt')
    dot(b, 50, 35, GREY); guide(b, 65, 42.5); dot(b, 65, 42.5)
    b.plot([0, 50], [35, 35], ls=(0, (3, 2)), lw=0.7, color=GREY)
    lbl(b, 66.5, 46.5, '$E_1$')
    b.annotate('excess demand\nat $P_0$', xy=(74, 35.6), xytext=(86, 48), color=GOLD, fontsize=7.5,
               arrowprops=dict(arrowstyle='-', color=GOLD, lw=0.6))
    arrow(b, 4, 35.5, 4, 42, GOLD); lbl(b, 6, 39, 'bid up', GOLD, size=7.5)
    lbl(b, 117, 17.5, '$D_1$', NAVY); lbl(b, 117, 2.5, '$D_0$', NAVY); lbl(b, 117, 67.5, '$S$', RED)
    yticks(b, [35, 42.5], ['$P_0$', '$P_1$'])
    save(fig, 'f11')


def f12():
    fig, (a, b) = two()
    q = np.linspace(0, 40, 50)
    for ax, (p0, p1), title, ped in ((a, (14, 16), '(a) elastic point: the loss is bigger', '2.3'),
                                     (b, (4, 6), '(b) inelastic point: the gain is bigger', '0.25')):
        q0, q1 = 40 - 2 * p0, 40 - 2 * p1
        axes(ax, r'Quantity $Q$', r'Price $P$', title, 43, 21)
        ax.add_patch(Polygon([(0, p0), (q1, p0), (q1, p1), (0, p1)], color=GOLDFILL, lw=0))
        ax.add_patch(Polygon([(q1, 0), (q0, 0), (q0, p0), (q1, p0)], color=REDFILL, lw=0))
        ax.plot(q, 20 - 0.5 * q, color=NAVY, lw=1.6)
        guide(ax, q1, p1); guide(ax, q0, p0); dot(ax, q1, p1); dot(ax, q0, p0, GREY)
        gain, loss = (p1 - p0) * q1, p0 * (q0 - q1)
        lbl(ax, q1 / 2, (p0 + p1) / 2, 'gain %d' % gain, GOLD, ha='center', size=8)
        xticks(ax, [q1, q0]); yticks(ax, [p0, p1], ['$P_0=%d$' % p0, '$P_1=%d$' % p1])
        lbl(ax, 41, 1.5, '$D$', NAVY)
        note(ax, 22, 17, r'$|PED|=%s$ here' % ped)
    lbl(a, 15, 6, 'loss 56', RED, size=8)
    lbl(b, 33, 5.2, 'loss 16', RED, size=8)
    save(fig, 'f12')


def f13():
    fig, (a, b) = plt.subplots(2, 1, figsize=(W1, 4.5))
    q = np.linspace(0, 100, 50)
    axes(a, r'Quantity $Q$', r'Price $P$', '(a) elasticity along a straight-line demand curve', 106, 11)
    a.plot(q, 10 - 0.1 * q, color=NAVY, lw=1.6)
    guide(a, 50, 5); dot(a, 50, 5)
    lbl(a, 51, 6, '$|PED|=1$'); lbl(a, 16, 9.3, '$|PED|>1$', NAVY); lbl(a, 74, 3.5, '$|PED|<1$', NAVY)
    axes(b, r'Quantity $Q$', r'Total revenue $TR$', '(b) total revenue along the same curve', 106, 330)
    b.plot(q, 10 * q - 0.1 * q ** 2, color=TEAL, lw=1.6)
    guide(b, 50, 250); dot(b, 50, 250, TEAL)
    note(b, 54, 300, '$TR$ peaks where $|PED|=1$,\nwhich is where $MR=0$', size=7.5)
    fig.subplots_adjust(hspace=0.6)
    save(fig, 'f13')


def f14():
    fig, (a, b) = two()
    for ax, beta, A, title in ((a, 0.835, 65.05, '(a) inelastic demand'), (b, 5.5, 205, '(b) elastic demand')):
        axes(ax, r'Quantity $Q$', r'Price $P$', title, 84, 62)
        P = np.linspace(0, 62, 200)
        Qd = A - beta * P
        m = (Qd >= 0) & (Qd <= 75)
        ax.plot(Qd[m], P[m], color=NAVY, lw=1.6)
        qs = np.linspace(0, 75, 50)
        ax.plot(qs, 10 + qs / 2, color=RED, lw=1.6)
        ax.plot(qs, 22 + qs / 2, color=RED, lw=1.6, ls=(0, (5, 3)))
        p1 = (A + 44) / (beta + 2); q1 = A - beta * p1
        guide(ax, 40, 30); guide(ax, q1, p1); dot(ax, 40, 30, GREY); dot(ax, q1, p1)
        lbl(ax, 76, 47.5, '$S_0$', RED); lbl(ax, 76, 59.5, '$S_1$', RED)
        lbl(ax, 3, 9.5, r'$\Delta P=%.1f$' % (p1 - 30) + '\n' + r'$\Delta Q=%.1f$' % (q1 - 40), GOLD, va='top', size=7.5)
    lbl(a, 66, 3, '$D$', NAVY); lbl(b, 76, 23.6, '$D$', NAVY)
    save(fig, 'f14')


def f15():
    fig, ax = one()
    q = np.linspace(0, 110, 50)
    axes(ax, r'Quantity $Q$', r'Price $P$', None, 130, 66)
    ax.add_patch(Polygon([(0, 60), (50, 35), (0, 35)], color=NAVYFILL, lw=0))
    ax.add_patch(Polygon([(0, 10), (50, 35), (0, 35)], color=REDFILL, lw=0))
    ax.plot(q, 60 - 0.5 * q, color=NAVY, lw=1.6); ax.plot(q, 10 + 0.5 * q, color=RED, lw=1.6)
    guide(ax, 50, 35); dot(ax, 50, 35)
    lbl(ax, 6, 42, 'consumer\nsurplus', NAVY, size=8); lbl(ax, 6, 28, 'producer\nsurplus', RED, size=8)
    lbl(ax, 111, 5, '$D=MPB$', NAVY); lbl(ax, 111, 65, '$S=MPC$', RED)
    xticks(ax, [50], ['$Q^{*}$']); yticks(ax, [35], ['$P^{*}$'])
    save(fig, 'f15')


def f16():
    fig, (a, b) = two()
    q = np.linspace(3, 27, 300)
    qa = q[np.argmin(atc5(q))]; pmin = atc5(qa)
    for ax, P, title in ((a, 13.0, '(a) short run: supernormal profit'), (b, pmin, '(b) long run: entry removes it')):
        axes(ax, r'Output $Q$', '£ per unit', title, 31, 26)
        qs = np.linspace(3, 27, 300)
        qstar = qs[(qs > 10)][np.argmin(np.abs(mc5(qs[qs > 10]) - P))]
        if P > pmin + 0.5:
            ax.add_patch(Polygon([(0, atc5(qstar)), (qstar, atc5(qstar)), (qstar, P), (0, P)], color=GOLDFILL, lw=0))
            lbl(ax, 0.6, (P + atc5(qstar)) / 2, 'supernormal\nprofit', GOLD, size=7.5)
        qmc = np.linspace(3, 24.6, 200); ax.plot(qmc, mc5(qmc), color=RED, lw=1.6)
        qat = np.linspace(6, 27, 200); ax.plot(qat, atc5(qat), color=NAVY, lw=1.6)
        qav = np.linspace(5, 27, 200); ax.plot(qav, avc5(qav), color=TEAL, lw=1.6)
        ax.plot([0, 24], [P, P], color=GOLD, lw=1.4)
        guide(ax, qstar, P); dot(ax, qstar, P)
        lbl(ax, 24.8, 25, '$MC$', RED); lbl(ax, 27.3, atc5(27) + 0.5, '$ATC$', NAVY); lbl(ax, 27.3, avc5(27) - 0.5, '$AVC$', TEAL)
        xticks(ax, [qstar], ['$Q^{*}$']); yticks(ax, [P], ['$P=MR$'])
    note(b, 8, 23, r'$P=\min ATC$:' + '\nnormal profit only', size=7.5)
    save(fig, 'f16')


def f17():
    fig, ax = plt.subplots(figsize=(W1 + 0.4, 3.1))
    q = np.linspace(0, 175, 300)
    axes(ax, r'Output $Q$', '£ per unit', None, 192, 15.5)
    qc = (0.06 + np.sqrt(0.0036 + 4 * 0.00105 * 8)) / (2 * 0.00105); pc = 14 - 0.06 * qc; pm = 14 - 0.06 * QM
    ax.add_patch(Polygon([(0, atc8(QM)), (QM, atc8(QM)), (QM, pm), (0, pm)], color=GOLDFILL, lw=0))
    qq = np.linspace(QM, qc, 60)
    ax.add_patch(Polygon(list(zip(qq, 14 - 0.06 * qq)) + list(zip(qq[::-1], mc8(qq[::-1]))), color=GREYFILL, lw=0))
    ax.plot(q, 14 - 0.06 * q, color=NAVY, lw=1.6)
    qmr = np.linspace(0, 116.7, 50); ax.plot(qmr, 14 - 0.12 * qmr, color=GREY, lw=1.4)
    q2 = np.linspace(10, 165, 200); ax.plot(q2, mc8(q2), color=RED, lw=1.6)
    q3 = np.linspace(14, 175, 200); ax.plot(q3, atc8(q3), color=TEAL, lw=1.4)
    guide(ax, QM, pm); dot(ax, QM, pm); ax.plot([QM, QM], [0, mc8(QM)], color=GREY, lw=0.7, ls=(0, (3, 2)))
    dot(ax, QM, mc8(QM), size=3); guide(ax, qc, pc); dot(ax, qc, pc, GREY)
    lbl(ax, 2, 5.65, 'supernormal profit', GOLD, size=7.5)
    lbl(ax, 177, 14 - 0.06 * 175, '$D=AR$', NAVY); lbl(ax, 118, 0.5, '$MR$', GREY); lbl(ax, 167, mc8(165), '$MC$', RED)
    lbl(ax, 177, atc8(175), '$ATC$', TEAL)
    ax.annotate('welfare loss', xy=(108, 6.6), xytext=(122, 10.5), color=MUTED, fontsize=8,
                arrowprops=dict(arrowstyle='-', color=MUTED, lw=0.7))
    xticks(ax, [QM, qc], ['$Q_m=87.3$', '$Q_c=120.4$']); yticks(ax, [pc, pm], ['$P_c=6.78$', '$P_m=8.76$'])
    save(fig, 'f17')


def pdisc():
    fig, (a, b) = two()
    for ax, A, sl, title, ped, pr, xm in ((a, 12, 1, '(a) students', '2', 8, 13), (b, 20, 2, '(b) adults', '1.5', 12, 11)):
        qmax = A / sl
        axes(ax, r'Quantity $Q$', '£ per unit', title, xm, 21)
        q = np.linspace(0, qmax, 50)
        ax.plot(q, A - sl * q, color=NAVY, lw=1.6)
        q2 = np.linspace(0, qmax / 2, 50); ax.plot(q2, A - 2 * sl * q2, color=GREY, lw=1.4)
        ax.plot([0, xm], [4, 4], color=RED, lw=1.4)
        guide(ax, 4, pr); dot(ax, 4, pr); dot(ax, 4, 4, size=3)
        lbl(ax, 4.3, pr + 1.0, r'$|PED|=%s$' % ped, MUTED, size=7.5)
        lbl(ax, 1.6, A - sl * 1.6 + 1.6, '$D$', NAVY)
        lbl(ax, qmax * 0.5 + 0.2, 1.0, '$MR$', GREY); lbl(ax, xm, 4.6, '$MC$', RED, ha='right', va='bottom')
        xticks(ax, [4]); yticks(ax, [4, pr], ['4', str(pr)])
    save(fig, 'pdisc')


def f18():
    fig, ax = one()
    axes(ax, r'Output $Q$', '£ per unit', None, 136, 15)
    qu = np.linspace(0, 50, 20); ql = np.linspace(50, 125, 20)
    ax.plot(qu, 12 - 0.04 * qu, color=NAVY, lw=1.6); ax.plot(ql, 16 - 0.12 * ql, color=NAVY, lw=1.6)
    ax.plot(qu, 12 - 0.08 * qu, color=GREY, lw=1.4)
    ql2 = np.linspace(50, 66.7, 20); ax.plot(ql2, 16 - 0.24 * ql2, color=GREY, lw=1.4)
    ax.plot([50, 50], [4, 8], color=GREY, lw=0.8, ls=(0, (2, 2)))
    q = np.linspace(0, 120, 20)
    ax.plot(q, 4.8 + 0.01 * q, color=RED, lw=1.5); ax.plot(q, 6.5 + 0.01 * q, color=RED, lw=1.5, ls=(0, (5, 3)))
    guide(ax, 50, 10); dot(ax, 50, 10)
    lbl(ax, 121, 6.0, '$MC_0$', RED); lbl(ax, 121, 7.7, '$MC_1$', RED)
    lbl(ax, 26, 9.0, '$MR$', GREY); lbl(ax, 126, 1.0, '$D$', NAVY)
    note(ax, 2, 14.8, 'more elastic: a price rise\nis not matched', va='top', size=7.5)
    note(ax, 66, 10.8, 'less elastic: a price cut\nis matched', size=7.5)
    note(ax, 70, 2.4, '$MC$ may shift\nwithin the gap', size=7.5)
    xticks(ax, [50], ['$Q^{*}$']); yticks(ax, [10], ['$P^{*}$'])
    save(fig, 'f18')


def labmin():
    fig, ax = one()
    L = np.linspace(0, 190, 50)
    axes(ax, r'Employment $L$', 'Wage £ per hour', None, 210, 21)
    ax.plot(L, 20 - 0.1 * L, color=NAVY, lw=1.6); ax.plot(L, 4 + 0.05 * L, color=RED, lw=1.6)
    guide(ax, 106.7, 9.33); dot(ax, 106.7, 9.33)
    ax.plot([0, 205], [12, 12], color=GOLD, lw=1.3)
    ax.plot([80, 160], [12, 12], color=GOLD, lw=3, solid_capstyle='butt')
    dot(ax, 80, 12, size=3); dot(ax, 160, 12, size=3)
    ax.plot([80, 80], [0, 12], ls=(0, (3, 2)), lw=0.7, color=GREY); ax.plot([160, 160], [0, 12], ls=(0, (3, 2)), lw=0.7, color=GREY)
    lbl(ax, 120, 12.6, 'unemployment', GOLD, ha='center', va='bottom', size=7.5)
    lbl(ax, 2, 12.6, 'minimum wage', GOLD, va='bottom', size=7.5)
    lbl(ax, 140, 8.0, '$MRP_L$ = demand', NAVY, size=7.5); lbl(ax, 191, 14.0, 'supply', RED, size=7.5)
    xticks(ax, [80, 106.7, 160], ['80', '106.7', '160']); yticks(ax, [9.33, 12], ['9.33', '12'])
    save(fig, 'labmin')


def monops():
    fig, ax = one()
    L = np.linspace(0, 170, 50)
    axes(ax, r'Employment $L$', 'Wage £ per hour', None, 185, 21)
    ax.plot(L, 20 - 0.1 * L, color=NAVY, lw=1.6); ax.plot(L, 4 + 0.05 * L, color=RED, lw=1.6)
    L2 = np.linspace(0, 155, 50); ax.plot(L2, 4 + 0.1 * L2, color=RED, lw=1.4, ls=(0, (5, 3)))
    guide(ax, 80, 12); dot(ax, 80, 12, size=3); dot(ax, 80, 8)
    ax.plot([0, 80], [8, 8], ls=(0, (3, 2)), lw=0.7, color=GREY)
    ax.plot([0, 106.7], [9.33, 9.33], color=GOLD, lw=1.3); dot(ax, 106.7, 9.33, GOLD)
    ax.plot([106.7, 106.7], [0, 9.33], ls=(0, (3, 2)), lw=0.7, color=GREY)
    lbl(ax, 150, 3.4, '$MRP_L$', NAVY); lbl(ax, 128, 13.6, 'supply (wage paid)', RED, size=7.5)
    lbl(ax, 157, 19.5, '$MCL$', RED)
    lbl(ax, 2, 10.0, 'minimum wage', GOLD, size=7.5)
    xticks(ax, [80, 106.7], ['80', '106.7']); yticks(ax, [8, 9.33, 12], ['8', '9.33', '12'])
    save(fig, 'monops')


def f19():
    fig, (a, b) = two()
    q = np.linspace(0, 110, 50)
    axes(a, r'Quantity $Q$', 'Price, costs', '(a) negative production externality', 128, 80)
    a.add_patch(Polygon([(30, 45), (50, 55), (50, 35)], color=GREYFILL, lw=0))
    a.plot(q, 60 - 0.5 * q, color=NAVY, lw=1.6); a.plot(q, 10 + 0.5 * q, color=RED, lw=1.6)
    q2 = np.linspace(0, 96, 50); a.plot(q2, 30 + 0.5 * q2, color=TEAL, lw=1.6)
    guide(a, 30, 45); guide(a, 50, 35); dot(a, 30, 45, TEAL); dot(a, 50, 35, GREY)
    lbl(a, 64, 2.5, '$D=MPB=MSB$', NAVY, size=7.5); lbl(a, 111, 65, '$MPC$', RED)
    lbl(a, 2, 78, '$MSC=MPC+MEC$', TEAL, size=7.5, va='top')
    a.annotate('welfare loss', xy=(45, 46), xytext=(70, 28), color=MUTED, fontsize=7.5,
               arrowprops=dict(arrowstyle='-', color=MUTED, lw=0.6))
    xticks(a, [30, 50], ['$Q^{*}$', '$Q_{mkt}$'])
    axes(b, r'Quantity $Q$', 'Price, benefits', '(b) positive consumption externality', 128, 84)
    b.add_patch(Polygon([(50, 55), (70, 45), (50, 35)], color=GREYFILL, lw=0))
    b.plot(q, 60 - 0.5 * q, color=NAVY, lw=1.6); b.plot(q, 80 - 0.5 * q, color=TEAL, lw=1.6)
    b.plot(q, 10 + 0.5 * q, color=RED, lw=1.6)
    guide(b, 50, 35); guide(b, 70, 45); dot(b, 50, 35, GREY); dot(b, 70, 45, TEAL)
    lbl(b, 111, 5, '$MPB$', NAVY); lbl(b, 111, 25, '$MSB$', TEAL); lbl(b, 111, 65, '$S$', RED)
    note(b, 70, 77, '$S=MPC=MSC$', size=7.5)
    b.annotate('welfare loss', xy=(55, 45), xytext=(4, 4), color=MUTED, fontsize=7.5,
               arrowprops=dict(arrowstyle='-', color=MUTED, lw=0.6))
    xticks(b, [50, 70], ['$Q_{mkt}$', '$Q^{*}$'])
    save(fig, 'f19')


def f20():
    fig, (a, b) = two()
    q = np.linspace(0, 110, 50)
    axes(a, r'Quantity $Q$', r'Price $P$', '(a) specific tax $t$ per unit', 124, 74)
    a.add_patch(Polygon([(0, 30), (40, 30), (40, 40), (0, 40)], color=GOLDFILL, lw=0))
    a.add_patch(Polygon([(40, 40), (50, 35), (40, 30)], color=GREYFILL, lw=0))
    a.plot(q, 60 - 0.5 * q, color=NAVY, lw=1.6)
    qs = np.linspace(0, 105, 50); a.plot(qs, 10 + 0.5 * qs, color=RED, lw=1.6)
    qt = np.linspace(0, 95, 50); a.plot(qt, 20 + 0.5 * qt, color=RED, lw=1.6, ls=(0, (5, 3)))
    guide(a, 40, 40); dot(a, 40, 40); dot(a, 40, 30); guide(a, 50, 35); dot(a, 50, 35, GREY)
    a.plot([0, 40], [30, 30], ls=(0, (3, 2)), lw=0.7, color=GREY)
    lbl(a, 2, 37.6, 'tax revenue', GOLD, size=7.5)
    a.annotate('welfare loss', xy=(45, 35), xytext=(58, 22), color=MUTED, fontsize=7.5,
               arrowprops=dict(arrowstyle='-', color=MUTED, lw=0.7))
    lbl(a, 111, 5, '$D$', NAVY); lbl(a, 106, 62.5, '$S$', RED); lbl(a, 96, 68.5, '$S+t$', RED)
    xticks(a, [40, 50], ['$Q_t$', '$Q^{*}$']); yticks(a, [30, 35, 40], ['$P_S$', '$P^{*}$', '$P_D$'])
    axes(b, r'Quantity $Q$', r'Price $P$', '(b) subsidy $s$ per unit', 124, 74)
    b.add_patch(Polygon([(0, 30), (60, 30), (60, 40), (0, 40)], color=TEALFILL, lw=0))
    b.add_patch(Polygon([(50, 35), (60, 40), (60, 30)], color=GREYFILL, lw=0))
    b.plot(q, 60 - 0.5 * q, color=NAVY, lw=1.6)
    b.plot(qs, 10 + 0.5 * qs, color=RED, lw=1.6); b.plot(q, 0.5 * q, color=RED, lw=1.6, ls=(0, (5, 3)))
    guide(b, 60, 40); dot(b, 60, 40); dot(b, 60, 30); guide(b, 50, 35); dot(b, 50, 35, GREY)
    lbl(b, 1.5, 36.2, 'cost to\ngovernment', TEAL, size=6.5)
    b.annotate('welfare loss', xy=(57, 35), xytext=(72, 22), color=MUTED, fontsize=7.5,
               arrowprops=dict(arrowstyle='-', color=MUTED, lw=0.7))
    lbl(b, 111, 5, '$D$', NAVY); lbl(b, 106, 62.5, '$S$', RED); lbl(b, 111, 55, '$S-s$', RED)
    xticks(b, [50, 60], ['$Q^{*}$', '$Q_s$']); yticks(b, [30, 35, 40], ['$P_D$', '$P^{*}$', '$P_S$'])
    save(fig, 'f20')


def f21():
    fig, (a, b) = two()
    q = np.linspace(0, 110, 50); qs = np.linspace(0, 105, 50)
    axes(a, r'Quantity $Q$', r'Price $P$', '(a) maximum price below $P^{*}$', 124, 66)
    a.add_patch(Polygon([(0, 25), (30, 25), (30, 35), (0, 35)], color=GOLDFILL, lw=0))
    a.add_patch(Polygon([(30, 45), (50, 35), (30, 25)], color=GREYFILL, lw=0))
    a.plot(q, 60 - 0.5 * q, color=NAVY, lw=1.6); a.plot(qs, 10 + 0.5 * qs, color=RED, lw=1.6)
    a.plot([0, 120], [25, 25], color=GOLD, lw=1.2)
    a.plot([30, 70], [25, 25], color=GOLD, lw=3, solid_capstyle='butt')
    guide(a, 50, 35); dot(a, 50, 35, GREY); a.plot([30, 30], [0, 45], ls=(0, (3, 2)), lw=0.7, color=GREY)
    a.plot([70, 70], [0, 25], ls=(0, (3, 2)), lw=0.7, color=GREY)
    lbl(a, 50, 21.5, 'shortage', GOLD, ha='center', va='top', size=7.5)
    lbl(a, 1.5, 30, 'transfer\nto buyers', GOLD, size=7)
    a.annotate('welfare loss', xy=(36, 36), xytext=(54, 52), color=MUTED, fontsize=7.5,
               arrowprops=dict(arrowstyle='-', color=MUTED, lw=0.7))
    lbl(a, 111, 5, '$D$', NAVY); lbl(a, 106, 62.5, '$S$', RED)
    xticks(a, [30, 70], ['$Q_S$\ntraded', '$Q_D$']); yticks(a, [25, 35], ['$P_{max}$', '$P^{*}$'])
    axes(b, r'Quantity $Q$', r'Price $P$', '(b) minimum price above $P^{*}$', 124, 66)
    b.plot(q, 60 - 0.5 * q, color=NAVY, lw=1.6); b.plot(qs, 10 + 0.5 * qs, color=RED, lw=1.6)
    b.plot([0, 120], [45, 45], color=GOLD, lw=1.2)
    b.plot([30, 70], [45, 45], color=GOLD, lw=3, solid_capstyle='butt')
    guide(b, 50, 35); dot(b, 50, 35, GREY)
    b.plot([30, 30], [0, 45], ls=(0, (3, 2)), lw=0.7, color=GREY); b.plot([70, 70], [0, 45], ls=(0, (3, 2)), lw=0.7, color=GREY)
    lbl(b, 50, 48, 'surplus', GOLD, ha='center', va='bottom', size=7.5)
    lbl(b, 111, 5, '$D$', NAVY); lbl(b, 106, 62.5, '$S$', RED)
    xticks(b, [30, 70], ['$Q_D$\ntraded', '$Q_S$']); yticks(b, [35, 45], ['$P^{*}$', '$P_{min}$'])
    save(fig, 'f21')


# ---------------------------------------------------------------- Part III
def f22():
    fig, ax = one()
    x = np.linspace(0, 10, 300)
    axes(ax, 'Consumer goods per year', 'Capital goods\nper year', None, 13, 10.5)
    ax.plot(x, 8 * np.sqrt(1 - (x / 10) ** 2), color=NAVY, lw=1.6)
    ya, yb = 8 * np.sqrt(1 - 0.16), 8 * np.sqrt(1 - 0.49)
    dot(ax, 4, ya); dot(ax, 7, yb)
    arrow(ax, 4, ya, 7, ya); arrow(ax, 7, ya, 7, yb)
    lbl(ax, 3.6, ya + 0.45, 'A', ha='right'); lbl(ax, 7.2, yb - 0.3, 'B', va='top')
    lbl(ax, 5.5, ya + 0.3, r'$\Delta x$', GOLD, ha='center', va='bottom')
    lbl(ax, 7.3, (ya + yb) / 2, r'$\Delta y$ = opportunity cost' + '\nof $\\Delta x$ more consumer goods', GOLD, size=7.5)
    dot(ax, 3, 2.5, GREY); lbl(ax, 3.3, 2.5, 'C: attainable but inefficient', MUTED, size=7.5)
    dot(ax, 10, 8.3, GREY); lbl(ax, 9.7, 8.9, 'D: unattainable with\ncurrent resources', MUTED, size=7.5, ha='right')
    lbl(ax, 1.2, 8.35, 'PPF', NAVY)
    save(fig, 'f22')


def flow(ax, pts, color, lw=1.4):
    xs, ys = zip(*pts)
    ax.plot(xs[:-1] + (xs[-1],), ys[:-1] + (ys[-1],), color=color, lw=lw, solid_joinstyle='miter')
    ax.annotate('', xy=pts[-1], xytext=pts[-2], arrowprops=dict(arrowstyle='-|>', color=color, lw=lw,
                shrinkA=0, shrinkB=0, mutation_scale=9))


def box(ax, x, y, w, h, title, sub, fill='#EEF1F7'):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle='round,pad=0.02,rounding_size=0.08',
                                fc=fill, ec=INK, lw=1.0, zorder=3))
    ax.text(x, y + 0.2, title, ha='center', va='center', fontsize=9.5, fontweight='bold', family='STIXGeneral', zorder=4)
    ax.text(x, y - 0.18, sub, ha='center', va='center', fontsize=7.5, color=MUTED, zorder=4, linespacing=1.1)


def f23():
    fig, ax = plt.subplots(figsize=(6.0, 4.3))
    ax.set_xlim(0, 10); ax.set_ylim(-0.1, 7); ax.axis('off')
    box(ax, 5, 6.1, 2.6, 0.8, 'Foreign sector', 'rest of the world')
    box(ax, 1.35, 3.5, 2.0, 1.15, 'Households', 'supply factors,\nbuy output')
    box(ax, 5, 3.5, 2.2, 1.05, 'Financial sector', 'banks and\nfinancial markets')
    box(ax, 8.65, 3.5, 2.0, 1.15, 'Firms', 'pay incomes,\nreceive revenue')
    box(ax, 5, 0.9, 2.6, 0.8, 'Government', 'taxes and spends')
    fs = 7.5
    flow(ax, [(1.8, 4.08), (1.8, 4.75), (8.2, 4.75), (8.2, 4.08)], NAVY)
    ax.text(5, 4.83, 'spending on goods and services', ha='center', va='bottom', color=NAVY, fontsize=fs)
    flow(ax, [(8.2, 2.92), (8.2, 2.25), (1.8, 2.25), (1.8, 2.92)], NAVY)
    ax.text(5, 2.17, 'wages, rent, interest, profit', ha='center', va='top', color=NAVY, fontsize=fs)
    flow(ax, [(3.9, 3.22), (2.35, 3.22)], NAVY); ax.text(3.12, 3.14, 'interest', ha='center', va='top', color=NAVY, fontsize=7)
    flow(ax, [(7.65, 3.22), (6.1, 3.22)], NAVY); ax.text(6.88, 3.14, 'interest', ha='center', va='top', color=NAVY, fontsize=7)
    flow(ax, [(2.35, 3.78), (3.9, 3.78)], RED); ax.text(3.12, 3.86, 'saving', ha='center', va='bottom', color=RED, fontsize=fs)
    flow(ax, [(6.1, 3.78), (7.65, 3.78)], TEAL); ax.text(6.88, 3.86, 'investment', ha='center', va='bottom', color=TEAL, fontsize=fs)
    flow(ax, [(0.7, 4.08), (0.7, 6.3), (3.7, 6.3)], RED); ax.text(2.2, 6.38, 'import spending', ha='center', va='bottom', color=RED, fontsize=fs)
    flow(ax, [(6.3, 6.3), (9.3, 6.3), (9.3, 4.08)], TEAL); ax.text(7.8, 6.38, 'export revenue', ha='center', va='bottom', color=TEAL, fontsize=fs)
    flow(ax, [(3.7, 5.9), (1.1, 5.9), (1.1, 4.08)], TEAL); ax.text(2.35, 5.82, 'income from\nassets abroad', ha='center', va='top', color=TEAL, fontsize=7)
    flow(ax, [(8.9, 4.08), (8.9, 5.9), (6.3, 5.9)], RED); ax.text(7.65, 5.82, 'profits paid to\nforeign owners', ha='center', va='top', color=RED, fontsize=7)
    flow(ax, [(1.1, 2.92), (1.1, 1.05), (3.7, 1.05)], RED); ax.text(2.4, 1.13, 'taxes net of benefits', ha='center', va='bottom', color=RED, fontsize=fs)
    flow(ax, [(8.9, 2.92), (8.9, 1.05), (6.3, 1.05)], RED); ax.text(7.6, 1.13, 'taxes net of subsidies', ha='center', va='bottom', color=RED, fontsize=fs)
    flow(ax, [(6.3, 0.7), (9.3, 0.7), (9.3, 2.92)], TEAL); ax.text(7.75, 0.62, 'government spending', ha='center', va='top', color=TEAL, fontsize=fs)
    for i, (c, t) in enumerate(((RED, 'withdrawals'), (TEAL, 'injections'), (NAVY, 'income flows'))):
        x0 = 1.0 + i * 2.0
        ax.plot([x0, x0 + 0.4], [0.0, 0.0], color=c, lw=2.5)
        ax.text(x0 + 0.5, 0.0, t, color=c, va='center', fontsize=8)
    save(fig, 'f23')


def kcross():
    fig, ax = one()
    Y = np.linspace(0, 560, 50)
    axes(ax, 'National income $Y$', 'Planned\nexpenditure $E$', None, 640, 560)
    ax.plot(Y, Y, color=GREY, lw=1.2)
    ax.plot(Y, 200 + 0.45 * Y, color=NAVY, lw=1.6, ls=(0, (5, 3)))
    ax.plot(Y, 250 + 0.45 * Y, color=NAVY, lw=1.6)
    y0, y1 = 200 / 0.55, 250 / 0.55
    guide(ax, y0, y0); guide(ax, y1, y1); dot(ax, y0, y0, GREY); dot(ax, y1, y1)
    arrow(ax, 120, 200 + 0.45 * 120 + 2, 120, 250 + 0.45 * 120 - 2, GOLD)
    lbl(ax, 126, 280, r'$\Delta A$', GOLD)
    arrow(ax, y0, 25, y1, 25, GOLD); lbl(ax, (y0 + y1) / 2, 33, r'$\Delta Y=k\Delta A$', GOLD, ha='center', va='bottom', size=7.5)
    lbl(ax, 300, 250, r'$E=Y$ (45°)', GREY, size=7.5)
    lbl(ax, 565, 250 + 0.45 * 560, '$E_1=A_1+zY$', NAVY, size=7.5)
    lbl(ax, 565, 200 + 0.45 * 560 - 8, '$E_0$', NAVY, size=7.5)
    xticks(ax, [y0, y1], ['$Y_0^{*}$', '$Y_1^{*}$'])
    save(fig, 'kcross')


def f24():
    fig, ax = one()
    axes(ax, 'Real output $Y$', 'Price level $P$', None, 10.5, 10)
    y = np.linspace(0.5, 9.8, 50)
    ax.plot(y, 9 - 0.8 * y, color=NAVY, lw=1.6)
    guide(ax, 2.5, 7); guide(ax, 7.5, 3); dot(ax, 2.5, 7, NAVY); dot(ax, 7.5, 3, NAVY)
    lbl(ax, 5.9, 0.8, '$AD$: $Y=kA(P)$', NAVY, size=8)
    note(ax, 4.6, 9.2, 'a lower price level raises real wealth,\nlowers interest rates and makes\nexports more competitive; the\nmultiplier amplifies each effect', va='top', size=7.5)
    save(fig, 'f24')


def f25():
    fig, axs = plt.subplots(1, 3, figsize=(W2, 2.4), gridspec_kw={'wspace': 0.4})
    y = np.linspace(0.3, 9.5, 100)
    a, b, c = axs
    axes(a, 'Real output $Y$', 'Price level $P$', '(a) short run', 10.5, 10)
    a.plot(y, sras(y), color=RED, lw=1.6)
    lbl(a, 9.0, sras(9.5) + 0.3, '$SRAS$', RED, ha='right', va='bottom')
    note(a, 0.5, 9.5, 'money wage fixed;\n$P=w/MP_L$ rises\nas output rises', va='top', size=7)
    axes(b, 'Real output $Y$', 'Price level $P$', '(b) long run', 10.5, 10)
    b.plot([7.5, 7.5], [0, 9.6], color=TEAL, lw=1.8)
    lbl(b, 7.7, 9.3, '$LRAS$', TEAL, size=7.5)
    note(b, 0.4, 5.2, 'set by real\nfactors, not by\nthe price level', size=7)
    xticks(b, [7.5], ['$Y_{FE}$'])
    axes(c, 'Real output $Y$', 'Price level $P$', '(c) Keynesian', 10.5, 10)
    c.plot([0.4, 3.5], [2, 2], color=GREY, lw=1.6)
    yy = np.linspace(3.5, 6.5, 30); c.plot(yy, 2 + 0.33 * (yy - 3.5) ** 2, color=GREY, lw=1.6)
    c.plot([6.5, 6.5], [4.97, 9.6], color=GREY, lw=1.6)
    note(c, 0.4, 7.6, 'flat, then\nrising, then\nvertical', size=7)
    xticks(c, [6.5], ['$Y_{FE}$'])
    save(fig, 'f25')


def sras(y, shift=0): return 0.8 + shift + 0.5 * np.exp(0.27 * y)


def f26():
    fig, ax = one()
    axes(ax, 'Real output $Y$', 'Price level $P$', None, 11.2, 10)
    y = np.linspace(0.5, 9.3, 100)
    ax.plot(y, sras(y), color=RED, lw=1.6)
    ax.plot([6, 6], [0, 9.6], color=TEAL, lw=1.8)
    yl = np.linspace(0.5, 7.0, 50); ax.plot(yl, 5.0 - 0.6 * yl, color=NAVY, lw=1.6, ls=(0, (5, 3)))
    ax.plot(y, 9.25 - 0.6 * y, color=NAVY, lw=1.6)
    def cross(c):
        yy = np.linspace(0.5, 9.3, 4000); i = np.argmin(np.abs(sras(yy) - (c - 0.6 * yy))); return yy[i], sras(yy[i])
    (y1, p1), (y2, p2) = cross(5.0), cross(9.25)
    guide(ax, y1, p1); guide(ax, y2, p2); dot(ax, y1, p1); dot(ax, y2, p2)
    arrow(ax, y1, 0.45, 6, 0.45, GREY, lw=0.9, both=True); arrow(ax, 6, 0.45, y2, 0.45, GREY, lw=0.9, both=True)
    note(ax, y1 - 0.15, 0.45, 'negative gap', ha='right', size=7.5)
    note(ax, y2 + 0.15, 0.45, 'positive gap', ha='left', size=7.5)
    lbl(ax, 6.2, 9.5, '$LRAS$', TEAL, va='top'); lbl(ax, 9.4, sras(9.3), '$SRAS$', RED)
    lbl(ax, 9.4, 9.25 - 0.6 * 9.3, r'$AD_{high}$', NAVY); lbl(ax, 0.6, 5.0 - 0.6 * 0.6 + 0.3, r'$AD_{low}$', NAVY, va='bottom')
    xticks(ax, [y1, 6, y2], ['$Y_1$', '$Y_{FE}$', '$Y_2$'])
    save(fig, 'f26')


def cycle():
    fig, ax = plt.subplots(figsize=(W1 + 0.6, 2.7))
    t = np.linspace(0, 20, 400)
    trend = 10 + 0.5 * t
    actual = trend + 1.4 * np.sin(2 * np.pi * t / 8.5) * (1 + 0.1 * np.sin(t / 3))
    axes(ax, 'Time', 'Real GDP', None, 21, 24, origin=(0, 8))
    ax.plot(t, trend, color=TEAL, lw=1.4, ls=(0, (5, 3)))
    ax.plot(t, actual, color=NAVY, lw=1.6)
    note(ax, 2.1, 13.2, 'boom', ha='center', va='bottom')
    note(ax, 6.4, 11.1, 'recession', ha='center', va='top')
    note(ax, 10.6, 17.2, 'boom', ha='center', va='bottom')
    i = np.argmin(np.abs(t - 14.9))
    arrow(ax, t[i], actual[i] + 0.05, t[i], trend[i] - 0.05, GOLD, lw=0.9, both=True)
    lbl(ax, t[i] - 0.3, actual[i] - 0.4, 'negative\noutput gap', GOLD, ha='right', va='top', size=7.5)
    lbl(ax, 0.4, 9.6, 'trend output', TEAL, va='top', size=7.5)
    lbl(ax, 18.6, 21.9, 'actual output', NAVY, ha='right', size=7.5)
    save(fig, 'cycle')


def f27():
    fig, (a, b) = two()
    y = np.linspace(0.5, 9.3, 100)
    def cross(f, g):
        yy = np.linspace(0.5, 9.3, 4000); i = np.argmin(np.abs(f(yy) - g(yy))); return yy[i], f(yy[i])
    axes(a, 'Real output $Y$', 'Price level $P$', '(a) demand-pull inflation', 11.8, 10)
    a.plot(y, sras(y), color=RED, lw=1.6)
    ad0 = lambda v: 6.5 - 0.6 * v; ad1 = lambda v: 8.3 - 0.6 * v
    a.plot(y, ad0(y), color=NAVY, lw=1.6, ls=(0, (5, 3))); a.plot(y, ad1(y), color=NAVY, lw=1.6)
    for f in (ad0, ad1):
        yy, pp = cross(sras, f); guide(a, yy, pp); dot(a, yy, pp)
    arrow(a, 2, ad0(2) + 0.1, 2, ad1(2) - 0.1, GOLD)
    note(a, 0.6, 9.8, 'prices and output\nboth rise', va='top', size=7)
    lbl(a, 9.4, ad1(9.3), '$AD_1$', NAVY); lbl(a, 9.4, ad0(9.3), '$AD_0$', NAVY)
    lbl(a, 9.4, sras(9.3), '$SRAS$', RED)
    axes(b, 'Real output $Y$', 'Price level $P$', '(b) cost-push inflation', 11.8, 10)
    s0 = lambda v: sras(v, -0.8); s1 = lambda v: sras(v, 0.9); ad = lambda v: 8 - 0.6 * v
    yb = np.linspace(0.5, 8.6, 100)
    b.plot(yb, s0(yb), color=RED, lw=1.6, ls=(0, (5, 3))); b.plot(yb, s1(yb), color=RED, lw=1.6)
    b.plot(y, ad(y), color=NAVY, lw=1.6)
    for f in (s0, s1):
        yy, pp = cross(f, ad); guide(b, yy, pp); dot(b, yy, pp)
    arrow(b, 7.8, s0(7.8) + 0.1, 7.8, s1(7.8) - 0.1, GOLD)
    note(b, 0.6, 9.8, 'prices rise,\noutput falls', va='top', size=7)
    lbl(b, 8.7, s1(8.6), '$SRAS_1$', RED); lbl(b, 8.7, s0(8.6), '$SRAS_0$', RED)
    lbl(b, 9.4, ad(9.3), '$AD$', NAVY)
    save(fig, 'f27')


def f28():
    fig, ax = one()
    axes(ax, 'Unemployment rate $u$ (%)', r'Inflation $\pi$ (%)', None, 12.2, 5.5)
    u = np.linspace(2.9, 9, 200)
    pc = lambda uu, pe: pe + 2.5 * (5 / uu - 1)
    ax.plot(u, pc(u, 2), color=NAVY, lw=1.6)
    ax.plot(u, pc(u, pc(3.5, 2)), color=NAVY, lw=1.6, ls=(0, (5, 3)))
    ax.plot([5, 5], [0, 5.3], color=TEAL, lw=1.8)
    pb = pc(3.5, 2)
    dot(ax, 5, 2); dot(ax, 3.5, pb); dot(ax, 5, pb)
    arrow(ax, 4.9, 2.07, 3.6, pb - 0.08, GOLD, lw=1.0); arrow(ax, 3.62, pb, 4.88, pb, GOLD, lw=1.0)
    lbl(ax, 5.15, 1.85, 'A', va='top'); lbl(ax, 3.35, pb, 'B', ha='right'); lbl(ax, 5.15, pb + 0.15, 'C', va='bottom')
    lbl(ax, 9.1, pc(9, 2), r'$SRPC_0$ ($\pi^e=2$)', NAVY, size=7.5)
    lbl(ax, 9.1, pc(9, pb), r'$SRPC_1$ ($\pi^e=%.1f$)' % pb, NAVY, size=7.5)
    lbl(ax, 5.2, 5.3, '$LRPC$', TEAL, va='top')
    note(ax, 6.0, 4.4, 'expected inflation rises,\nso $SRPC$ shifts up', size=7.5)
    xticks(ax, [5], ['$u_n$ (NAIRU)'])
    save(fig, 'f28')


def f29():
    fig, (a, b) = two()
    r = np.arange(1, 10); dep = 1000 * 0.9 ** (r - 1)
    axes(a, 'Round', 'New deposit (£)', '(a) deposits created in each round', 10, 1150)
    a.bar(r, dep, width=0.62, color='#5A73A8')
    for k in range(4):
        lbl(a, r[k], dep[k] + 25, '{:,.0f}'.format(dep[k]), INK, ha='center', va='bottom', size=7.5)
    note(a, 5.0, 950, r'each round is $(1-\rho)$ times' + '\nthe one before')
    axes(b, 'Round', 'Deposits so far (£)', '(b) the running total', 10, 11000)
    b.plot(r, np.cumsum(dep), color=TEAL, lw=1.6, marker='o', ms=3.5)
    b.plot([0, 10], [10000, 10000], color=GREY, lw=1, ls=(0, (5, 3)))
    yticks(b, [10000], ['10,000'])
    note(b, 2.2, 8000, r'the total converges on $D_0/\rho$')
    save(fig, 'f29')


def f30():
    fig, (a, b) = two()
    M = np.linspace(0, 10, 50)
    md = lambda m: 9 - 0.8 * m
    axes(a, 'Quantity of money $M$', 'Interest rate $i$', '(a) the Bank sets the rate', 10.5, 10)
    a.plot(M, md(M), color=NAVY, lw=1.6)
    for i, ls in ((4, '-'), (6, (0, (5, 3)))):
        a.plot([0, 10.3], [i, i], color=RED, lw=1.5, ls=ls)
    guide(a, 6.25, 4); guide(a, 3.75, 6); dot(a, 6.25, 4); dot(a, 3.75, 6, GREY)
    arrow(a, 6.1, 3.55, 3.9, 3.55, GOLD, lw=1.0)
    lbl(a, 6.6, 4.2, r'$M_S$: $i_B=4\%$', RED, va='bottom', size=7.5)
    lbl(a, 6.6, 6.2, r'$i_B=6\%$', RED, va='bottom', size=7.5)
    lbl(a, 9.0, 2.5, '$M_D$', NAVY)
    note(a, 4.2, 2.6, 'quantity of\nmoney falls', size=7)
    yticks(a, [4, 6], ['4', '6'])
    axes(b, 'Quantity of money $M$', 'Interest rate $i$', '(b) exam convention: fixed supply', 10.5, 10)
    b.plot(M, md(M), color=NAVY, lw=1.6)
    b.plot([5, 5], [0, 9.5], color=RED, lw=1.6)
    guide(b, 5, md(5)); dot(b, 5, md(5))
    lbl(b, 5.2, 9.3, '$M_S$', RED, va='top'); lbl(b, 9.0, 2.5, '$M_D$', NAVY)
    note(b, 5.6, 7.3, 'the rate settles where\nthe fixed stock is\nwillingly held', size=7)
    yticks(b, [md(5)], ['$i^{*}$'])
    save(fig, 'f30')


def f31():
    fig, ax = plt.subplots(figsize=(W1 + 0.4, 3.0))
    axes(ax, 'Real output $Y$', 'Price level $P$', None, 152, 168, origin=(60, 60))
    d = np.linspace(-26, 36, 200); y = 100 + d
    s0 = lambda dd: 100 + 1.2 * dd + 0.02 * dd ** 2
    ax.plot(y, s0(d), color=RED, lw=1.6, ls=(0, (5, 3)))
    d1 = np.linspace(-26, 22, 200); ax.plot(100 + d1, s0(d1) + 30, color=RED, lw=1.6)
    dd = np.linspace(-36, 36, 50)
    ax.plot(100 + dd, 100 - dd, color=NAVY, lw=1.6, ls=(0, (5, 3))); ax.plot(100 + dd, 130 - dd, color=NAVY, lw=1.6)
    ax.plot([100, 100], [60, 165], color=TEAL, lw=1.8)
    dB = (-2.2 + np.sqrt(2.2 ** 2 + 4 * 0.02 * 30)) / 0.04
    for (yy, pp) in ((100, 100), (100 + dB, 130 - dB), (100, 130)):
        guide(ax, yy, pp, x0=60, y0=60); dot(ax, yy, pp)
    lbl(ax, 98.5, 100, 'A', ha='right'); lbl(ax, 100 + dB + 2, 130 - dB - 3, 'B', va='top'); lbl(ax, 98.5, 133, 'C', ha='right')
    arrow(ax, 75, 125 + 1, 75, 155 - 1, GOLD); arrow(ax, 86, s0(-14) + 1, 86, s0(-14) + 29, GOLD)
    lbl(ax, 137, 64, '$AD_0$', NAVY); lbl(ax, 137, 94, '$AD_1$', NAVY)
    lbl(ax, 137, s0(36), '$SRAS_0$', RED); lbl(ax, 123, s0(22) + 30, '$SRAS_1$', RED)
    lbl(ax, 101.5, 163, '$LRAS$', TEAL, va='top')
    xticks(ax, [100, 100 + dB], ['$Y_{FE}$', '$Y_B$'])
    save(fig, 'f31')


def lfunds():
    fig, ax = one()
    axes(ax, 'Loanable funds (£bn)', 'Real interest\nrate $r$ (%)', None, 215, 6, origin=(80, 0))
    Q = np.linspace(90, 195, 50)
    ax.plot(Q, (Q - 100) / 20, color=TEAL, lw=1.6)
    Qi = np.linspace(100, 155, 50); ax.plot(Qi, (160 - Qi) / 10, color=NAVY, lw=1.6)
    Qg = np.linspace(130, 185, 50); ax.plot(Qg, (190 - Qg) / 10, color=NAVY, lw=1.6, ls=(0, (5, 3)))
    guide(ax, 140, 2, x0=80); guide(ax, 160, 3, x0=80); dot(ax, 140, 2, GREY); dot(ax, 160, 3)
    dot(ax, 130, 3, size=3); ax.plot([130, 130], [0, 3], ls=(0, (3, 2)), lw=0.7, color=GREY)
    arrow(ax, 130, 3.35, 160, 3.35, GOLD, lw=0.9, both=True); lbl(ax, 145, 3.45, 'borrowing £30bn', GOLD, ha='center', va='bottom', size=7)
    arrow(ax, 130, 1.4, 140, 1.4, RED, lw=0.9, both=True); lbl(ax, 135, 0.95, 'crowded out £10bn', RED, ha='center', va='top', size=7)
    lbl(ax, 196, 4.75, 'saving $S$', TEAL, size=7.5)
    lbl(ax, 156, 0.4, '$I$', NAVY, size=7.5); lbl(ax, 186, 0.5, '$I+(G-T)$', NAVY, size=7.5)
    xticks(ax, [130, 140, 160]); yticks(ax, [2, 3])
    save(fig, 'lfunds')


def laffer():
    fig, ax = one()
    axes(ax, r'Tax rate $\tau$', 'Revenue $T/Y_{0}$', None, 1.05, 0.3)
    t = np.linspace(0, 1, 300)
    for eps, c, ls in ((1, NAVY, '-'), (2, RED, (0, (5, 3)))):
        ax.plot(t, t * (1 - t) ** eps, color=c, lw=1.6, ls=ls)
        ts = 1 / (1 + eps); guide(ax, ts, ts * (1 - ts) ** eps); dot(ax, ts, ts * (1 - ts) ** eps, c)
    lbl(ax, 0.52, 0.262, r'$\varepsilon=1$', NAVY); lbl(ax, 0.36, 0.158, r'$\varepsilon=2$', RED)
    xticks(ax, [1 / 3, 0.5, 1], ['33%', '50%', '100%'])
    note(ax, 0.66, 0.285, r'peak at $\tau^{*}=1/(1+\varepsilon)$', size=7.5)
    save(fig, 'laffer')


def lorenz():
    fig, ax = plt.subplots(figsize=(3.6, 3.3))
    axes(ax, 'Cumulative share of population $p$', 'Cumulative share\nof income', None, 1.05, 1.05)
    p = np.linspace(0, 1, 200)
    ax.fill_between(p, p ** 2, p, color=GOLDFILL, lw=0)
    ax.fill_between(p, 0, p ** 2, color=TEALFILL, lw=0)
    h1, = ax.plot(p, p, color=GREY, lw=1.2); h2, = ax.plot(p, p ** 2, color=NAVY, lw=1.6)
    h3, = ax.plot(p, p ** 3, color=RED, lw=1.4, ls=(0, (5, 3)))
    lbl(ax, 0.45, 0.33, 'A', GOLD, ha='center'); lbl(ax, 0.8, 0.2, 'B', TEAL, ha='center')
    ax.legend([h1, h2, h3], ['line of equality', r'$\ell(p)=p^{2}$', r'$\ell(p)=p^{3}$'], loc='upper left',
              frameon=False, fontsize=7.5)
    xticks(ax, [0.5, 1], ['0.5', '1']); yticks(ax, [0.5, 1], ['0.5', '1'])
    save(fig, 'lorenz')


def lras():
    fig, ax = one()
    axes(ax, 'Real output $Y$', 'Price level $P$', None, 10.5, 10)
    y = np.linspace(0.5, 9.8, 50)
    ax.plot(y, 9 - 0.7 * y, color=NAVY, lw=1.6)
    ax.plot([4.8, 4.8], [0, 9.6], color=TEAL, lw=1.6, ls=(0, (5, 3))); ax.plot([7, 7], [0, 9.6], color=TEAL, lw=1.8)
    guide(ax, 4.8, 9 - 0.7 * 4.8); guide(ax, 7, 9 - 0.7 * 7); dot(ax, 4.8, 9 - 0.7 * 4.8); dot(ax, 7, 9 - 0.7 * 7)
    arrow(ax, 4.9, 8.6, 6.9, 8.6, GOLD)
    lbl(ax, 4.6, 9.4, '$LRAS_0$', TEAL, ha='right', va='top'); lbl(ax, 7.2, 9.4, '$LRAS_1$', TEAL, va='top')
    lbl(ax, 9.7, 9 - 0.7 * 9.7 + 0.3, '$AD$', NAVY, ha='right', va='bottom')
    xticks(ax, [4.8, 7], ['$Y_{FE}$', "$Y'_{FE}$"]); yticks(ax, [9 - 0.7 * 7, 9 - 0.7 * 4.8], ['$P_1$', '$P_0$'])
    save(fig, 'lras')


def f32():
    fig, ax = one()
    axes(ax, 'Quantity of sterling', 'Exchange rate ($ per £)', None, 11.2, 10)
    q = np.linspace(0.5, 9.6, 50)
    ax.plot(q, 1.5 + 0.6 * q, color=RED, lw=1.6)
    ax.plot(q, 8 - 0.6 * q, color=NAVY, lw=1.6, ls=(0, (5, 3))); ax.plot(q, 9.2 - 0.6 * q, color=NAVY, lw=1.6)
    guide(ax, 6.5 / 1.2, 1.5 + 0.6 * 6.5 / 1.2); guide(ax, 7.7 / 1.2, 1.5 + 0.6 * 7.7 / 1.2)
    dot(ax, 6.5 / 1.2, 1.5 + 0.6 * 6.5 / 1.2, GREY); dot(ax, 7.7 / 1.2, 1.5 + 0.6 * 7.7 / 1.2)
    lbl(ax, 9.7, 1.5 + 0.6 * 9.6, r'$S_{£}$', RED)
    lbl(ax, 9.7, 9.2 - 0.6 * 9.6, r'$D_{£1}$', NAVY); lbl(ax, 9.7, 8 - 0.6 * 9.6, r'$D_{£0}$', NAVY)
    note(ax, 6.6, 0.35, 'higher demand for £\n(exports, UK assets):\nappreciation', va='bottom', size=7.5)
    yticks(ax, [1.5 + 0.6 * 6.5 / 1.2, 1.5 + 0.6 * 7.7 / 1.2], ['$e_0$', '$e_1$'])
    save(fig, 'f32')


def jcurve():
    fig, ax = plt.subplots(figsize=(W1, 2.5))
    t = np.linspace(-3, 20, 400)
    tb = np.where(t < 0, 0, 3.2 * (1 - np.exp(-t / 5)) - 4.5 * (t / 2.5) * np.exp(-t / 2.5))
    axes(ax, 'Time', 'Trade balance', None, 21, 3.3, origin=(-3, -2.2))
    ax.plot([-3, 21], [0, 0], color=GREY, lw=0.8)
    ax.plot([0, 0], [-2.2, 3.1], color=GREY, lw=0.8, ls=(0, (3, 2)))
    ax.plot(t, tb, color=NAVY, lw=1.6)
    note(ax, 0.3, 2.9, 'depreciation', va='top')
    note(ax, 3.2, -1.95, 'elasticities low:\nbalance worsens', va='bottom', size=7.5)
    note(ax, 12, 2.0, 'volumes adjust:\nbalance improves', va='bottom', size=7.5)
    save(fig, 'jcurve')


def f33():
    fig, (a, b) = two()
    axes(a, 'Shirts', 'Loaves', '(a) production possibilities', 46, 68)
    a.plot([0, 30], [60, 0], color=NAVY, lw=1.6); a.plot([0, 40], [40, 0], color=RED, lw=1.6)
    lbl(a, 12, 39, 'UK', NAVY); lbl(a, 29, 14, 'Portugal', RED)
    note(a, 16, 62, 'UK: 1 shirt costs 2 loaves\nPortugal: 1 shirt costs 1 loaf', va='top', size=7)
    xticks(a, [30, 40]); yticks(a, [40, 60])
    axes(b, 'Shirts', 'Loaves', '(b) gains from specialisation', 46, 68)
    b.plot([0, 30], [60, 0], color=NAVY, lw=1.6); b.plot([0, 40], [60, 0], color=TEAL, lw=1.4, ls=(0, (5, 3)))
    dot(b, 15, 30, GREY); dot(b, 16, 36, TEAL)
    note(b, 14, 27, 'autarky\n(15 shirts, 30 loaves)', ha='right', va='top', size=7)
    lbl(b, 17.5, 38.5, 'with trade\n(16 shirts, 36 loaves)', TEAL, size=7, va='bottom')
    lbl(b, 26, 55, 'trade line:\n1 shirt for 1.5 loaves', TEAL, size=7)
    lbl(b, 3, 6, 'UK PPF', NAVY)
    xticks(b, [30, 40]); yticks(b, [60])
    save(fig, 'f33')


def f34():
    fig, (a, b) = two()
    Q = np.linspace(0, 200, 50)
    for ax, title, mid in ((a, '(a) a tariff of 2 per unit', 'revenue'), (b, '(b) a quota of 40 units', 'quota rents')):
        axes(ax, 'Quantity $Q$', 'Price $P$', title, 210, 21)
        ax.add_patch(Polygon([(40, 8), (60, 8), (60, 10)], color=GREYFILL, lw=0))
        ax.add_patch(Polygon([(100, 8), (120, 8), (100, 10)], color=GREYFILL, lw=0))
        ax.add_patch(Polygon([(60, 8), (100, 8), (100, 10), (60, 10)], color=GOLDFILL, lw=0))
        ax.plot(Q, 20 - 0.1 * Q, color=NAVY, lw=1.6); ax.plot(Q[Q <= 160], 4 + 0.1 * Q[Q <= 160], color=RED, lw=1.6)
        ax.plot([0, 210], [8, 8], color=GREY, lw=1.2); ax.plot([0, 210], [10, 10], color=INK, lw=1.2)
        for x0, y0 in ((40, 8), (60, 10), (100, 10), (120, 8)):
            ax.plot([x0, x0], [0, y0], ls=(0, (3, 2)), lw=0.7, color=GREY)
        lbl(ax, 80, 9, mid, GOLD, ha='center', size=6.5)
        arrow(ax, 60, 6.6, 100, 6.6, GREY, lw=0.8, both=True); lbl(ax, 80, 6.2, 'imports 40', MUTED, ha='center', va='top', size=6)
        ax.annotate('welfare\nloss', xy=(53, 8.6), xytext=(5, 13.5), color=MUTED, fontsize=7, arrowprops=dict(arrowstyle='-', color=MUTED, lw=0.6))
        ax.annotate('welfare\nloss', xy=(106, 8.6), xytext=(140, 13.5), color=MUTED, fontsize=7, arrowprops=dict(arrowstyle='-', color=MUTED, lw=0.6))
        lbl(ax, 196, 1.2, '$D$', NAVY); lbl(ax, 160, 20.5, '$S$', RED, va='top')
        xticks(ax, [40, 60, 100, 120]); yticks(ax, [8, 10], ['$P_w=8$', '10'])
    save(fig, 'f34')


def f35():
    fig, ax = one()
    Q = np.linspace(0, 190, 50)
    axes(ax, 'Quantity $Q$', 'Price $P$', '(c) a producer subsidy of 2 per unit', 200, 21)
    q = np.linspace(0, 60, 30)
    ax.fill_between(q, 2 + 0.1 * q, 4 + 0.1 * q, color=TEALFILL, lw=0)
    ax.add_patch(Polygon([(40, 8), (60, 8), (60, 10)], color=GREYFILL, lw=0))
    ax.plot(Q, 20 - 0.1 * Q, color=NAVY, lw=1.6)
    ax.plot(Q[Q <= 150], 4 + 0.1 * Q[Q <= 150], color=RED, lw=1.6)
    ax.plot(Q[Q <= 160], 2 + 0.1 * Q[Q <= 160], color=RED, lw=1.6, ls=(0, (5, 3)))
    ax.plot([0, 200], [8, 8], color=GREY, lw=1.2)
    for x0 in (40, 60, 120):
        ax.plot([x0, x0], [0, 8], ls=(0, (3, 2)), lw=0.7, color=GREY)
    dot(ax, 120, 8, NAVY)
    lbl(ax, 3, 13, 'cost to\ntaxpayers', TEAL, size=8)
    ax.annotate('', xy=(25, 5.5), xytext=(12, 11.8), arrowprops=dict(arrowstyle='-|>', color=TEAL, lw=0.8, mutation_scale=7))
    ax.annotate('welfare loss', xy=(55, 8.9), xytext=(75, 5.5), color=MUTED, fontsize=8, arrowprops=dict(arrowstyle='-', color=MUTED, lw=0.6))
    lbl(ax, 125, 9.0, 'consumption unchanged', NAVY, size=8, va='bottom')
    lbl(ax, 150, 19.3, '$S$', RED); lbl(ax, 160, 17.6, '$S-s$', RED); lbl(ax, 190, 1.5, '$D$', NAVY)
    xticks(ax, [40, 60, 120]); yticks(ax, [8], ['$P_w=8$'])
    save(fig, 'f35')


def goods():
    fig, ax = plt.subplots(figsize=(4.8, 2.9))
    ax.set_xlim(0, 10); ax.set_ylim(0, 6.6); ax.axis('off')
    cells = [((2.0, 3.0), NAVYFILL, 'Private good', 'a sandwich'),
             ((6.0, 3.0), GOLDFILL, 'Common good', 'ocean fish stocks'),
             ((2.0, 0.0), TEALFILL, 'Club good', 'a streaming service'),
             ((6.0, 0.0), REDFILL, 'Public good', 'national defence')]
    for (x, y), c, name, ex in cells:
        ax.add_patch(plt.Rectangle((x, y), 4.0, 3.0, fc=c, ec='white', lw=3))
        ax.text(x + 2.0, y + 1.75, name, ha='center', va='center', fontsize=10.5, fontweight='bold', family='STIXGeneral')
        ax.text(x + 2.0, y + 1.05, 'e.g. ' + ex, ha='center', va='center', fontsize=8, color=INK)
    ax.text(4.0, 6.3, 'Excludable', ha='center', va='center', fontsize=9.5)
    ax.text(8.0, 6.3, 'Non-excludable', ha='center', va='center', fontsize=9.5)
    ax.text(1.75, 4.5, 'Rival', ha='right', va='center', fontsize=9.5)
    ax.text(1.75, 1.5, 'Non-rival', ha='right', va='center', fontsize=9.5)
    save(fig, 'goods')


ALL = [f1, f2, f3, lossav, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16, f17, pdisc, f18,
       labmin, monops, f19, goods, f20, f21, f22, f23, kcross, f24, f25, f26, cycle, f27, f28, f29, f30, f31,
       lfunds, laffer, lorenz, lras, f32, jcurve, f33, f34, f35]

if __name__ == '__main__':
    want = set(sys.argv[1:])
    for fn in ALL:
        if not want or fn.__name__ in want:
            fn()
    print('drew', len(want) or len(ALL))
