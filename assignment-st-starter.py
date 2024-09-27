# import packages
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns

sns.set()

# show the title
st.title('Titanic App by Zhixuan Ye')

# read csv and show the dataframe
df = pd.read_csv("train.csv")

st.subheader('Titanic Dataset')
st.dataframe(df)

# create a figure with three subplots, size should be (15, 5)
# show the box plot for ticket price with different classes
# you need to set the x labels and y labels
# a sample diagram is shown below
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

sns.boxplot(x='Pclass', y='Fare', data=df[df['Pclass'] == 1], ax=axs[0])
sns.boxplot(x='Pclass', y='Fare', data=df[df['Pclass'] == 2], ax=axs[1])
sns.boxplot(x='Pclass', y='Fare', data=df[df['Pclass'] == 3], ax=axs[2])

axs[0].set_xlabel('Pclass', fontsize=12)
axs[0].set_ylabel('Fare', fontsize=12)

axs[1].set_xlabel('Pclass', fontsize=12)
axs[1].set_ylabel('Fare', fontsize=12)

axs[2].set_xlabel('Pclass', fontsize=12)
axs[2].set_ylabel('Fare', fontsize=12)

plt.tight_layout()
st.pyplot(fig)
