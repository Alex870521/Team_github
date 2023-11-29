import matplotlib.pyplot as plt
from functools import wraps

# For more details please seehttps://matplotlib.org/stable/users/explain/customizing.html

# font_scalings = {
#     'xx-small': 0.579,
#     'x-small': 0.694,
#     'small': 0.833,
#     'medium': 1.0,
#     'large': 1.200,
#     'x-large': 1.440,
#     'xx-large': 1.728,
#     'larger': 1.2,
#     'smaller': 0.833
# }


def set_figure(func=None, *, figsize=None, fs=None, fw=None, titlesize=None):
    def decorator(_func):
        @wraps(_func)
        def wrapper(*args, **kwargs):
            plt.rcParams['mathtext.fontset'] = 'custom'
            plt.rcParams['mathtext.rm'] = 'Times New Roman'
            plt.rcParams['mathtext.it'] = 'Times New Roman: italic'
            plt.rcParams['mathtext.bf'] = 'Times New Roman: bold'
            plt.rcParams['mathtext.default'] = 'regular'

            # The font properties used by `text.Text`.
            # The text, annotate, label, title, ticks, are used to create text
            plt.rcParams['font.family'] = 'Times New Roman'
            plt.rcParams['font.weight'] = fw or 'normal'
            plt.rcParams['font.size'] = fs or 16

            plt.rcParams['axes.titlelocation'] = 'center'
            plt.rcParams['axes.titleweight'] = 'bold'
            plt.rcParams['axes.titlesize'] = 'large'
            plt.rcParams['axes.labelweight'] = 'bold'

            plt.rcParams['xtick.labelsize'] = 'medium'
            plt.rcParams['ytick.labelsize'] = 'medium'

            # matplotlib.font_manager.FontProperties ---> matplotlib.rcParams
            plt.rcParams['legend.loc'] = 'best'
            plt.rcParams['legend.frameon'] = False
            plt.rcParams['legend.fontsize'] = 'small'
            # plt.rcParams['legend.fontweight'] = 'bold'  #key error
            plt.rcParams['legend.handlelength'] = 1.5

            plt.rcParams['figure.figsize'] = figsize or (8, 8)
            plt.rcParams['figure.autolayout'] = True
            # plt.rcParams['figure.constrained_layout.use'] = True
            plt.rcParams['figure.dpi'] = 150

            plt.rcParams['savefig.transparent'] = True

            result = _func(*args, **kwargs)

            return result
        return wrapper

    if func is None:
        return decorator

    else:
        return decorator(func)
