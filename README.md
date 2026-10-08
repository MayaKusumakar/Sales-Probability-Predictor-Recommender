# Sales-Probability-Predictor-Recommender
Classification problem to see what the probability that a sale/deal will go through for a company based on data of past sales Found an IBM Watson Dataset on IBM’s past sales

### View the Project Presentation: 
[Presentation PDF](https://github.com/MayaKusumakar/Sales-Probability-Predictor-Recommender/blob/main/Sales_Deal_Agent_Deck.pdf)

### Steps: 
1. Found an IBM Watson Dataset on IBM’s past sales
2. Clean/Preprocessed & Feature Engineered
3. Used LightGBM to train the model
    - Metrics were too low so I added more unique features. **Update:** Didn’t change performance
    - Did K fold cross validation to reduce overfitting
    - Tuned threshold separately. **Update:** This improved performance
    - Added another feature (opportunity amount) in from the original raw dataset that had important information. This improved performance but raised questions about data leakage. Investigated the data leakage, turned out to be a false alarm.
