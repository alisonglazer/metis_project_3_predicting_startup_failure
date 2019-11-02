# Metis Project 3

**Project 3 in the Metis Data Science Bootcamp**

Problem statement: *Using data from the web, can we build models using supervised learning techniques to classify whether a startup will be successful?*

I focused on companies founded within the last decade that had raised more than one round of funding. I narrowed the term "success" to mean IPO or getting acquired in this case and "failure" as closing. After tuning a logistic regression model, I deployed the model via a flask web app on [Heroku](https://startup-predictor.herokuapp.com/).
With thousands of companies' information I determined which factors could predict their success. Using the Crunchbase dataset with information on 20,000+ companies and all of their funding rounds, I looked at the following features:

1. Average money raised per funding round
2. Number of funding rounds
3. Average time between funding rounds
4. Time between seed and series A round
5. Country
6. State
7. Industry


I applied various classification algorithms, and I found that tree-based models like XGBoost as well as Logistic Regression performed the best. 

Due to its interpretability and ability to quantitatively translate the inputs to the output, I deployed the Logistic Regression model. Using a probability threshold of 35%, I achieved an f_beta score of 0.85 with a beta value of 3. This places extra emphasis on recall because in the application of venture capital investments (the intended use case for this model), it is far more important to catch any potential "unicorns" even at the expense of investing in a few "duds".

## Files

[`p03_Data_Cleaning.ipynb`](p03_Data_Cleaning.ipynb) shows the process to clean all of the data and prepare relevant features for modeling

[`p03_Modeling.ipynb`](p03_Modeling.ipynb) shows the process of training various classifiers and evaluating feature relationships and model performance

[Web App](web_app) files used to build the browser-based predictor tool hosted on Heroku [here](https://startup-predictor.herokuapp.com/)

Slides can be found [here](https://www.slideshare.net/AlisonGlazer/metis-project-3-predicting-startup-success)
