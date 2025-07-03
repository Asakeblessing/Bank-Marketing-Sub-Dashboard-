import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Bank Marketing Dashboard", layout="wide")

# Load data
df = pd.read_csv('Cleaned_BankMarketing.csv')

st.title("📊 Bank Marketing Campaign Dashboard")

# Show raw data
if st.checkbox("Show Raw Data"):
    st.write(df.head())

# Subscription distribution
st.subheader("1. Subscription Outcome")
st.bar_chart(df['y'].value_counts())

# Age Distribution
st.subheader("2. Age Distribution")
fig1, ax1 = plt.subplots()
sns.histplot(df['age'], kde=True, ax=ax1)
st.pyplot(fig1)

# Job Distribution
st.subheader("3. Job Category Distribution")
fig2, ax2 = plt.subplots(figsize=(10,5))
sns.countplot(data=df, y='job', order=df['job'].value_counts().index, ax=ax2)
st.pyplot(fig2)

# Marital vs Subscription
st.subheader("4. Marital Status vs Subscription")
fig3, ax3 = plt.subplots()
sns.countplot(data=df, x='marital', hue='y', ax=ax3)
st.pyplot(fig3)

# Education vs Subscription
st.subheader("5. Education vs Subscription")
fig4, ax4 = plt.subplots(figsize=(10,5))
sns.countplot(data=df, x='education', hue='y', ax=ax4)
plt.xticks(rotation=45)
st.pyplot(fig4)
