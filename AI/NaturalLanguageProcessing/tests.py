from sklearn.datasets import fetch_20newsgroups
groups = fetch_20newsgroups()
import seaborn as sns
sns.distplot(groups.target)

import matplotlib.pyplot as plt
plt.show()


