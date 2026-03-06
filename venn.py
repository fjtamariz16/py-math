from matplotlib_venn import venn2, venn2_circles, venn2_unweighted
from matplotlib import pyplot as plt

H = {'rabbit', 'elephant', 'panda', 'elk', 'goat'}
P = {'cat', 'dog', 'rabbit', 'snake', 'goat'}

venn2([H, P], ('Herbivore', 'Pet'))
plt.show()
