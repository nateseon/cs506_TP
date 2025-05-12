

Project Overview

We are working on a Loan approval prediction model. The goal of the project is to predict whether a loan application will be approved or not(binary classification problem). The features in the dataset include various factors such as:

* Income of the applicant
* Loan amount requested
* Credit score (CIBIL score)
* And other features like education, dependents, etc.

### What Are We Trying to Achieve?:

We are trying to build a model that can predict whether a loan application will be approved or not, based on the applicant’s details. The model should be able to:

1. Look at new loan applications and decide if the application is likely to be approved or rejected (this is the prediction).
2. Provide insights into which features (income, loan amount, etc.) have the biggest impact on the loan approval decision.

### Steps We Took in the Project:

#### 1.Data Preprocessing:

* We started with raw data about loan applicants.
* We cleaned the data by handling missing values and normalizing (scaling) the data so that all features are on the same scale. This helps the model perform better.

#### 2. Building the Model:

* We chose XGBoost (a powerful machine learning algorithm) to train our model. XGBoost is good for classification problems like ours.
* We fed the cleaned data into the model to learn the relationship between the features (like income, loan amount) and the target (loan approval status).

#### 3. Training the Model:

* The model "learns" from the training data (80% of the dataset) by finding patterns and relationships in the data. For example, it might learn that higher income increases the chances of loan approval, or low CIBIL score decreases approval chances.
* Once trained, the model can then make predictions about new data (the 20% test data).

#### 4. Evaluating the Model:

* Accuracy: We check how often the model's predictions are correct. An accuracy of **98%** means the model is predicting correctly 98% of the time.
* Precision and Recall: These metrics help us understand how well the model is doing, especially when the data is imbalanced (e.g., if most applications are approved, the model could just predict "approved" all the time to get a high accuracy).

  * Precision tells us how many of the approvals predicted by the model were actually correct.
  * Recall tells us how many of the actual approvals the model was able to predict correctly.
* F1-Score: This combines both precision and recall into one metric, giving us a better sense of the model's overall performance.

#### 5. Confusion Matrix:

* The confusion matrix shows how many times the model predicted the correct or incorrect class (approved/rejected).
* True Positives: Correctly predicted approved loans.
* True Negatives: Correctly predicted rejected loans.
* False Positives: Wrongly predicted a loan as approved when it should have been rejected.
* False Negatives: Wrongly predicted a loan as rejected when it should have been approved.



---


The overall goal is to:

* Make accurate predictions about whether a loan should be approved or rejected.
* Provide insights into what factors are most important in the decision-making process for loan approval.
