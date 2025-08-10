# Medical-Insurance-Cost-Predictor

A medical insurance cost prediction model using linear regression estimates individual insurance charges based on factors like age, BMI, smoking status, and region. It helps predict costs accurately to assist insurers and customers in financial planning and risk assessment.

## Technologies Used

- **Python** — Core programming language  
- **scikit-learn** — For building and training the linear regression model  
- **pandas** — For data manipulation and analysis  
- **numpy** — For numerical operations  
- **matplotlib** and **seaborn** — For data visualization and exploratory analysis  

## Overview

Medical insurance premiums vary depending on factors such as age, gender, body mass index (BMI), smoking status, and number of children. This model leverages historical insurance data to learn relationships between these features and insurance costs, enabling predictions of future charges with reasonable accuracy.

## Features Used

- **Age**: Age of the individual  
- **Sex**: Gender of the individual (Male/Female)  
- **BMI**: Body Mass Index, indicating body fat based on height and weight  
- **Children**: Number of children/dependents covered by insurance  
- **Smoker**: Smoking status (Yes/No)  
- **Region**: Residential area (used for regional cost variations)  

## How It Works

- The dataset is preprocessed and cleaned using pandas and numpy.  
- Categorical variables are encoded to numerical values.  
- Data visualization with matplotlib and seaborn helps understand feature distributions and correlations.  
- The data is split into training and testing sets.  
- A linear regression model is trained on the training data using scikit-learn.  
- The model predicts insurance charges on test data.  
- Model performance is evaluated using metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), and R² score.  

## Getting Started

1. Clone this repository.  
2. Install the required dependencies:

    ```bash
    pip install numpy pandas scikit-learn matplotlib seaborn
    ```

3. Run the training and prediction scripts.  
4. Use the trained model to predict insurance costs for new input data.

## Use Cases

- Estimating insurance premiums for individuals based on their profiles.  
- Helping insurance companies set competitive and fair pricing.  
- Assisting individuals in budgeting for medical insurance costs.

## Future Improvements

- Incorporate more features like medical history or lifestyle factors.  

---

Feel free to explore the code and contribute enhancements!
