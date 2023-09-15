import streamlit as st

# Define quiz questions and answers
questions = [
    {
        'question': "🚂 What is the purpose of the 'train-test split' technique in machine learning, and why is it important?",
        'options': [
            "To train the model. 📚",
            "To evaluate the model's performance. 📊",
            "To validate the model's parameters. 🔍"
        ],
        'correct_option': 1  # Index of the correct option (0-based)
    },
    {
        'question': "🤔 In the context of machine learning, what does 'overfitting' mean?",
        'options': [
            "The model performs well on the training data but poorly on new, unseen data. 🙁",
            "The model performs equally well on both training and test data. 😄",
            "The model is too simple to capture the underlying patterns in the data. 🤨"
        ],
        'correct_option': 0
    },
    {
        'question': "📏 What is the purpose of feature scaling in machine learning?",
        'options': [
            "To make all features have the same value. 📐",
            "To reduce the dimensionality of the dataset. 📉",
            "To normalize the data and bring it to a similar scale. 📈"
        ],
        'correct_option': 2
    },
    {
        'question': "🤖 Which machine learning algorithm is commonly used for classification problems?",
        'options': [
            "Linear Regression 📈",
            "K-Means Clustering 📊",
            "Logistic Regression 🧮"
        ],
        'correct_option': 2
    },
    {
        'question': "📊 What is the mean of a normally distributed dataset?",
        'options': [
            "Zero 0️⃣",
            "One 1️⃣",
            "It depends on the dataset. 📉"
        ],
        'correct_option': 0
    },
    {
        'question': "🔄 What is the purpose of cross-validation in machine learning?",
        'options': [
            "To train a model on all available data. 📚",
            "To evaluate the model's performance on a separate dataset. 📊",
            "To assess how well a model will generalize to unseen data. 🔍"
        ],
        'correct_option': 2
    },
    {
        'question': "📈 Which evaluation metric is commonly used for regression problems?",
        'options': [
            "Accuracy 🎯",
            "F1 Score 📊",
            "Mean Squared Error (MSE) 📈"
        ],
        'correct_option': 2
    },
    {
        'question': "🔍 What is the main goal of dimensionality reduction techniques like PCA?",
        'options': [
            "To increase the number of features in the dataset. 📈",
            "To improve model accuracy. 📊",
            "To reduce the number of features while preserving important information. 🧮"
        ],
        'correct_option': 2
    },
    {
        'question': "📉 What is the purpose of a confusion matrix in classification?",
        'options': [
            "To measure the model's accuracy. 📊",
            "To visualize data in a 2D space. 📈",
            "To evaluate the performance of a classification model. 🔍"
        ],
        'correct_option': 2
    },
    {
        'question': "🐼 Which Python library is commonly used for data manipulation and analysis?",
        'options': [
            "Matplotlib 📊",
            "Scikit-Learn 📚",
            "Pandas 🐼"
        ],
        'correct_option': 2
    },
    {
        'question': "🔢 What is the process of converting categorical variables into numerical form called?",
        'options': [
            "Normalization 📏",
            "Encoding 🔢",
            "Feature scaling 📈"
        ],
        'correct_option': 1
    },
    {
        'question': "🌳 Which algorithm is used for finding patterns in data via unsupervised learning?",
        'options': [
            "K-Nearest Neighbors 🧮",
            "Principal Component Analysis (PCA) 🔍",
            "Decision Trees 🌳"
        ],
        'correct_option': 1
    },
    {
        'question': "🧐 What is the purpose of regularization in machine learning?",
        'options': [
            "To make the model more complex. 📊",
            "To prevent overfitting and control model complexity. 🔍",
            "To increase the bias of the model. 📉"
        ],
        'correct_option': 1
    },
    {
        'question': "📖 What is the term for a dataset with labels that indicate the correct output?",
        'options': [
            "Supervised learning 📊",
            "Unsupervised learning 🔍",
            "Reinforcement learning 🎮"
        ],
        'correct_option': 0
    },
    {
        'question': "📊 Which statistical test is used to determine if there is a significant difference between the means of two groups?",
        'options': [
            "Chi-squared test 📈",
            "T-test 🔍",
            "F-test 🧮"
        ],
        'correct_option': 1
    },
]

# Initialize a variable to keep track of the user's score
score = 0

# Streamlit app layout
st.title("📚 Data Science Quiz  App By Ali Shan🧠")
st.markdown("Test your knowledge of data science concepts!")

# Iterate through questions
for i, question_data in enumerate(questions, 1):
    st.subheader(f"Question {i}: {question_data['question']}")
    user_answer = st.radio("Select an option:", question_data['options'])
    
    # Check if the user's answer is correct
    if user_answer == question_data['options'][question_data['correct_option']]:
        score += 1

# Display the user's score
st.subheader("🏆 Quiz Results 📊")
st.write(f"You scored {score} out of {len(questions)} questions! 🎉")

# Calculate and display the percentage
percentage = (score / len(questions)) * 100
st.write(f"Your score is {percentage:.2f}% 📈")

# Provide feedback based on the user's performance
if percentage == 100:
    st.success("Congratulations! You got a perfect score! 🥇🌟")
elif percentage >= 75:
    st.success("Great job! You have a strong understanding of data science concepts. 👏👍")
elif percentage >= 50:
    st.warning("Not bad! You're on the right track, keep learning. 😃📚")
else:
    st.error("You might want to review some data science concepts. Don't give up! 📖🤔")
