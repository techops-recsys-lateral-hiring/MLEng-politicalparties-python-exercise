import streamlit as st

def get_prediction(input_text):
    # TODO - task 3
    # -----------------------------------
    # Goal: our goal is to complete the implementation of this function, 
    #       which takes input text and returns a prediction result from a pre-trained model.
    pass

# Streamlit page configuration
st.set_page_config(page_title="Tweet Classifier", layout="wide")

# Streamlit UI components
st.title("Classify your tweet")

# User inputs the tweet
tweet_input = st.text_input("Enter your tweet", "")

# Button to trigger prediction
if st.button("Classify Tweet"):
    # Get prediction
    prediction = get_prediction(tweet_input)
    
    # Display the prediction
    st.write("Prediction:", prediction)

