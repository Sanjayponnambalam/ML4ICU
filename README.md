# ML4ICU
Predicting Patient Deterioration in Intensive Care Units (ICUs), focuses on developing a machine learning model to predict patient decline based on physiological data


## **Overview**
ML4ICU is a machine learning project designed to enhance patient care in Intensive Care Units (ICUs) by accurately predicting patient deterioration.  
By analyzing vital signs such as heart rate, respiratory rate, body temperature, oxygen saturation, blood pressure, and demographic information, ML4ICU provides early warnings of potential health crises, aiding timely intervention.

---

## **Key Features**
- **Predictive Modeling**: Accurately classifies patients into `High Risk` and `Low Risk` categories.
- **Vital Sign Analysis**: Utilizes physiological metrics such as:
  - `Heart Rate`
  - `Respiratory Rate`
  - `Body Temperature`
  - `Oxygen Saturation`
  - Derived metrics like `HRV`, `BMI`, and `MAP`
- **User Interface**: Integrated with a web application using Flask and Bootstrap for seamless interaction.
- **Computational Efficiency**: Subset of the dataset (2k rows) used for constraints while maintaining robust performance.

---

## **Dataset**
- **Size**: Original dataset contains 200k+ rows; subset of 2k rows used for computational constraints.
- **Features**:  
  - `Heart Rate`  
  - `Respiratory Rate`  
  - `Body Temperature`  
  - `Oxygen Saturation`  
  - `Derived_HRV`  
  - `Derived_BMI`  
  - `Derived_MAP`
- **Target Variable**:  
  - `Risk Category`: Binary classification (`High Risk` / `Low Risk`)

---





## **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/username/ML4ICU.git
   cd ML4ICU
   ```

2. Usage
   ```python
   python app.py

   ```
3. Access the web interface at http://localhost:5000.
   
4. Input patient data via the UI and receive real-time predictions.

---
   
## **Architecture**

![Architecture Diagram](/ML4ICUArchitecture.jpg "System Architecture")


## Workflow Overview

This project aims to leverage the power of ensemble learning techniques to build a robust and accurate prediction model. The workflow involves the following key steps:

### 1. Exploratory Data Analysis (EDA)
* **Univariate Analysis:** Understanding the distribution, central tendency, and dispersion of individual features.
* **Multivariate Analysis:** Exploring relationships between different features.
* **Target Variable Analysis:** Analyzing the distribution and characteristics of the target variable.

### 2. Data Preprocessing
* **Handling Missing Values:** Imputing missing values using appropriate interpolation techniques.
* **Outlier Management:** Identifying and addressing outliers using robust statistical methods.

### 3. Distribution Analysis
* **Shapiro-Wilk Test:** Assessing the normality of data distributions.
* **Levene's Test:** Checking for homogeneity of variances (homoscedasticity).
* **Q-Q Plots:** Visualizing the distribution of data against a theoretical normal distribution.

### 4. Dataset Splitting
* **Train-Test Split:** Dividing the dataset into training and testing sets in an 80-20 ratio.

### 5. Cross-Validation
* **K-Fold Cross-Validation:** Implementing K-Fold Cross-Validation to evaluate model performance on different subsets of the data.

### 6. Model Building: Ensemble Learning with Bagging and Support Vector Classifier
* **Bagging:** Creating multiple bootstrapped subsets of the training data.
* **Support Vector Classifier (SVC):** Training an SVC model on each bootstrapped subset.
* **Ensemble:** Combining the predictions of individual SVC models to make final predictions.

By combining the strengths of bagging and SVC, this approach aims to reduce variance, improve prediction accuracy, and enhance the overall robustness of the model.

---

## **Model Performance**

The model demonstrated excellent performance on both the training and testing sets, as evidenced by the following metrics:

**Training Set:**
* **Accuracy:** 98%
* **Precision:** 98%
* **Recall:** 98%
* **F1-Score:** 98%

**Testing Set:**
* **Accuracy:** 98%
* **Precision:** 98%
* **Recall:** 97%
* **F1-Score:** 97%

**Confusion matrices:**

* **Training Set**

  ```lua
  [[81891  1800]
   [ 1879 74051]]
  ```
* **Testing Set**
  ```lua
  [[20487   444]
   [516 18459]]
  ```
These results suggest that the model is highly accurate and reliable in predicting the target variable, both on the data it was trained on and on unseen data. The consistency between the training and testing set performance indicates that the model is not overfitting and generalizes well to new data.

---

## **Comparative Analysis of models**

| Algorithm | Accuracy | Recall | Precision | F1-Score | AUC-ROC |
|---|---|---|---|---|---|
| Bagging with SVC | 98% | 97% | 98% | 98% | 0.980 |
| MSIPA | 93.7% | 91.4% | 92.6% | 92% | 0.967 |
| LSTM | 89.2% | 87.3% | 88.5% | 87.9% | 0.941 |
| GRU | 88.5% | 86.5% | 87.7% | 87.1% | 0.935 |
| RNN | 85.4% | 83.6% | 84.8% | 84.2% | 0.913 |

---

## **Future Enhancements**

* Incorporate additional features like patient history for better predictions.
* Optimize performance for larger datasets.
* Real-time embedding with ICU equipments.

---

## **License**

This project is licensed under the MIT License. See the ![LICENSE](https://github.com/Sanjayponnambalam/ML4ICU/blob/main/LICENSE) file for details

---

## **Website**

* Low Risk

![Low Risk Prediction](https://github.com/Sanjayponnambalam/ML4ICU/blob/main/website/imgs/lowrisk.png)

* High Risk
  
![High Risk Prediction](https://github.com/Sanjayponnambalam/ML4ICU/blob/main/website/imgs/highrisk)

---

