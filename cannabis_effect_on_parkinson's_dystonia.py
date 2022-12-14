# -*- coding: utf-8 -*-
"""Cannabis Effect on Parkinson's Dystonia

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15bV5bXTG_V61X5mu7rpNregL2_2TJAPe
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

"""# *Data from the Fox Insight Study(FI) - Visualized by Leah Tibbets*


---

Data used in the preparation of this data vizualization were obtained from the Fox Insight Database (https://foxinsight-info.michaeljfox.org/insight/explore/insight.jsp) on 09/04/2022. For up-to-date information on the study, 
visit https://foxinsight-info.michaeljfox.org/insight/explore/insight.jsp


*The Fox Insight Study (FI) is funded by The Michael J. Fox Foundation for Parkinson’s Research. We would like to thank the Parkinson’s community for participating in this study to make this research possible.*
"""

CannDystonia = pd.read_csv('/content/CannDystonia.csv')

"""## **Histogram 1**
Explores the data from the Fox Den study of the effects **cannabis** has on **Parkinson's Dystonia**. The data samples **1000** people with Parkinson's who answered the cannabis questionnaire.

# **The legend is:**

Light Gray = **Started With Cannabis** (1)

Red = **Markedly Worse** (2)

Blue = **Mildly Worse** (3)

Green = **No Effect** (4)

Orange = **Mildly Better** (6)

Pink = **Markedly Better** (8)

Gray = **Have not had Dystonia** (12)





"""

CannEffectDystonia = CannDystonia['CannEffectDystonia']
CannDystoniaAge = CannDystonia["age"]

# plot:
fig, ax = plt.subplots()

ax.set_ylabel("Participants")
ax.set_xlabel("Effect on Parkinson's Dystonia")
CannEffectDystonia, CannEffectAge , patches = ax.hist(CannEffectDystonia, bins=12, linewidth=1.2, edgecolor="white")



colors = cm.get_cmap('Set1')
for i, rect in enumerate(patches):
    rect.set_fc(colors(i))

plt.show()



"""**1617 total people answered that had tried cannabis with their Parkinson's Dystonia in the full study. The full study contains 2746 people who answered the cannabis questionnaire**

# **Out of that:**

712 **better**

55 **worse**

850 **had no effect**

# **That means:**

3% were **worse**

14% were **a lot better**

29% were **mildly better**

52% had **no effect**





"""