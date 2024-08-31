import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

st.title('Financial Budget Analysis Dashboard')

st.markdown("""
# **Objectives of Budget 2024: Text Analysis**

1. **Trend Analysis**
   - **Objective:** Analyze the evolution of consumer opinions and business reactions over time following the budget announcement.
   - **Goal:** Identify patterns or shifts in sentiments by tracking changes on a daily, weekly, or monthly basis.

2. **Impact Analysis**
   - **Objective:** Assess how changes in taxation, subsidies, and prices have influenced consumer spending habits and business decisions.
   - **Goal:** Determine the economic impact by analyzing consumer spending reports and business activity, such as expansion or reduction in operations.

3. **Comparative Analysis**
   - **Objective:** Evaluate the differing impacts of Budget 2024 on various consumer groups (e.g., low-income vs. high-income) and industries (e.g., manufacturing vs. services).
   - **Goal:** Compare the effects of the budget to determine which groups and sectors benefit the most and which might face challenges.
""")

merged_data = pd.read_csv('merged_data.csv')

st.header("Dataset")
st.dataframe(merged_data.head(10), use_container_width=True)


# Convert 'date' column to datetime
merged_data['date'] = pd.to_datetime(merged_data['date'])

# Group by 'date' and 'sentiment' and count occurrences
sentiment_trends = merged_data.groupby(['date', 'sentiment']).size().reset_index(name='count')

# Streamlit app


# Sentiment Trends Over Time
st.subheader('Sentiment Trends Over Time')
plt.figure(figsize=(12, 8))
sns.lineplot(data=sentiment_trends, x='date', y='count', hue='sentiment', marker='o', palette='plasma')
plt.title('Sentiment Trends Over Time')
plt.xlabel('Date')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.legend(title='Sentiment')
st.pyplot(plt)

# Word Cloud of Consumer Opinions
st.subheader('Word Cloud of Consumer Opinions')
text = ' '.join(merged_data['opinion'].dropna())
wordcloud = WordCloud(
    width=800,
    height=400,
    background_color='white',
    colormap='plasma',
    contour_color='black',
    contour_width=2,
    max_font_size=100,
    min_font_size=10,
    stopwords=None,
    random_state=42
).generate(text)
plt.figure(figsize=(12, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of Consumer Opinions', fontsize=20)
st.pyplot(plt)

# Word Cloud of Producer Opinions
st.subheader('Word Cloud of Producer Opinions')
text = ' '.join(merged_data['producer_opinion'].dropna())
wordcloud = WordCloud(
    width=800,
    height=400,
    background_color='white',
    colormap='plasma',
    contour_color='black',
    contour_width=1,
    max_font_size=100,
    min_font_size=10,
    stopwords=None,
    random_state=42
).generate(text)
plt.figure(figsize=(12, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of Producer Opinions', fontsize=20)
st.pyplot(plt)

# Business Financial Impact Over Time
st.subheader('Business Financial Impact Over Time')
plt.figure(figsize=(12, 6))
sns.lineplot(data=merged_data, x='date', y='income', marker='o', palette='plasma')
plt.title('Business Financial Impact Over Time')
plt.xlabel('Date')
plt.ylabel('Income')
plt.xticks(rotation=45)
st.pyplot(plt)

# Distribution of Income
st.subheader('Distribution of Income')
plt.figure(figsize=(12, 6))
sns.histplot(data=merged_data, x='income', bins=30, kde=True, palette='plasma')
plt.title('Distribution of Income')
plt.xlabel('Income')
plt.ylabel('Frequency')
st.pyplot(plt)

# Distribution of Sentiments
st.subheader('Distribution of Sentiments')
sentiment_counts = merged_data['sentiment'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', colors=sns.color_palette('plasma'))
plt.title('Distribution of Sentiments')
st.pyplot(plt)

import seaborn as sns

# Create a DataFrame of word frequencies
from collections import Counter
word_freq = Counter(' '.join(merged_data['producer_opinion']).split())
word_freq_df = pd.DataFrame(word_freq.items(), columns=['Word', 'Frequency']).sort_values(by='Frequency', ascending=False).head(20)


st.subheader('Top 20 Words in Producer Opinions')
plt.figure(figsize=(12, 6))
sns.barplot(data=word_freq_df, x='Word', y='Frequency', palette='plasma')
plt.xticks(rotation=45)
st.pyplot(plt)

word_freq = Counter(' '.join(merged_data['opinion']).split())
word_freq_df = pd.DataFrame(word_freq.items(), columns=['Word', 'Frequency']).sort_values(by='Frequency', ascending=False).head(20)
st.subheader('Top 20 Words in Consumer Opinions')
plt.figure(figsize=(12, 6))
sns.barplot(data=word_freq_df, x='Word', y='Frequency', palette='plasma')
plt.xticks(rotation=45)
st.pyplot(plt)

