# ML Fundamentals Checkpoint

This checkpoint is designed to test your understanding of the content from the Machine Learning Fundamentals Cumulative Lab.

Specifically, this will cover:

* Performing a train-test split to evaluate model performance on unseen data
* Applying appropriate preprocessing steps to training and test data
* Identifying overfitting and underfitting

## Your Task: Build and Evaluate a Ridge Regression Model to Predict Home Prices

### Data Understanding

You will be using the Ames Housing dataset, modeling the `SalePrice` based on all other numeric features of the dataset. You can view the `data_description.txt` file for explanations of these variables if desired, but the specific feature descriptions can be safely ignored.


```python
# Run this cell without changes
import pandas as pd

# Read in CSV file
df = pd.read_csv("ames.csv", index_col=0)
# Keep only numeric data
df = df.select_dtypes(include="number")
# Keep only columns with no missing values
df = df.dropna(axis=1)
df
```

### Modeling

You will apply a **predictive** modeling process using scikit-learn. That means that you are trying to build a model with the best performance on predicting the target (`SalePrice`) using the features of unseen data.

For this reason you will first perform a **train-test split**, so that you are fitting the model using the training dataset and evaluating the model using the testing dataset.

You will also report model **metrics** in terms of both r-squared and RMSE, for both the train and test data, in order to interpret your model performance.

### Requirements

#### 1. Perform a Train-Test Split

#### 2. Preprocess Data

#### 3. Fit a `Ridge` Model

#### 4. Evaluate the Model Performance

#### 5. Interpret the Model Performance

## 1. Perform a Train-Test Split

This step has two parts. First, separate `df` into `X` and `y`.

* `X` should be a pandas `DataFrame` containing all columns of `df` except for the target
* `y` should be a pandas `Series` containing just the target

The target is `SalePrice`.


```python
# Replace None with appropriate code
X = None
y = None
# your code here
raise NotImplementedError
```


```python
# Checking the type and shape of X
assert type(X) == pd.DataFrame
assert X.shape == (1460, 33)

# Checking the type and shape of y
assert type(y) == pd.Series
assert y.shape == (1460,)

# PUT ALL WORK FOR THE ABOVE QUESTION ABOVE THIS CELL
# THIS UNALTERABLE CELL CONTAINS HIDDEN TESTS
```

Now that you have `X` and `y`, perform a train-test split ([documentation here](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html)). Let's say that 40% of the data should be in the test set (60% in the train set), and the random state should be 42.


```python
# Replace None with appropriate code

# Import the train_test_split function
from sklearn.model_selection import train_test_split

# Perform train-test split. Replace None for test_size and random_state!
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=None, random_state=None)
# your code here
raise NotImplementedError
```


```python
# Checking the shapes
# (If this fails, make sure you specified the appropriate test_size)
assert X_train.shape == (876, 33)
assert y_train.shape == (876,)

# Checking the contents
# (If this fails, make sure you specified the appropriate random_state)
assert X_train.iloc[100]["YearBuilt"] == 1947
assert y_train.iloc[100] == 110000

# PUT ALL WORK FOR THE ABOVE QUESTION ABOVE THIS CELL
# THIS UNALTERABLE CELL CONTAINS HIDDEN TESTS
```

## 2. Preprocess Data

### Ridge Regression Recap

We are going to use a `Ridge` regression, which adds a penalty term to the square of the magnitude of the coefficients.

In other words, whereas an ordinary least squares regression uses this cost function:

$$ \sum_{i=1}^n(y_i - \sum_{j=1}^k(m_jx_{ij} ) -b )^2$$

...where $n$ is the number of rows in the dataset, $y$ is the target value, $k$ is the number of features in the dataset, $m$ is the slope parameter (coefficient) we are trying to find, $x$ is the value of the feature, and $b$ is the intercept...

...a ridge regression uses this cost function:

$$\sum_{i=1}^n(y_i - \sum_{j=1}^k(m_jx_{ij})-b)^2 + \lambda \sum_{j=1}^p m_j^2$$

The difference is the $\lambda \sum_{j=1}^p m_j^2$ at the end, where $\lambda$ is a _hyperparameter_ that we specify, which is multiplied by the coefficients. **The goal of fitting a model is finding $m$ values to *minimize* the cost function**, so a larger $\lambda$ means more of a penalty on high coefficients. This is a form of *regularization* that should help with overfitting.

### Scaling

Ridge regression, which uses L2 norm regularization, means that feature values need to be standardized so that some values aren't penalized "unfairly". So let's go ahead and apply a `StandardScaler` ([documentation here](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html)) to the entire feature set, fitting and transforming `X_train` and transforming `X_test`.

Create new variables `X_train_scaled` and `X_test_scaled` which are the scaled versions of `X_train` and `X_test`.


```python
# Replace None with appropriate code

# Import StandardScaler
None

# Instantiate a scaler object
scaler = None

# Fit the scaler on X_train and transform X_train
None
X_train_scaled = None

# Transform X_test
X_test_scaled = None

# your code here
raise NotImplementedError
```


```python
import numpy as np

# scaler should be a StandardScaler
assert type(scaler) == StandardScaler
# scaler should be fitted
assert type(scaler.mean_) == np.ndarray

# X_train_scaled should have the same shape
# as X_train but with different contents
assert X_train_scaled.shape == X_train.shape
assert X_train_scaled[0][0] != X_train.iloc[0].iloc[0]

# Same goes for X_test_scaled
assert X_test_scaled.shape == X_test.shape
assert X_test_scaled[0][0] != X_test.iloc[0].iloc[0]

# PUT ALL WORK FOR THE ABOVE QUESTION ABOVE THIS CELL
# THIS UNALTERABLE CELL CONTAINS HIDDEN TESTS
```

## 3. Fit a `Ridge` Model

Now that we have our preprocessed data, fit a `Ridge` regression model ([documentation here](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html)).

When instantiating the model, specify an `alpha` (regularization penalty) of 100, a `solver` of `"sag"` (stochastic average gradient descent), and a `random_state` of 1.


```python
# Replace None with appropriate code

# Import Ridge model from scikit-learn
None

# Instantiate the model
model = None

# Fit the model on the scaled training data
None

# your code here
raise NotImplementedError
```


```python
# model should be a Ridge regressor
assert type(model) == Ridge

# model should be fitted
assert type(model.coef_) == np.ndarray

# PUT ALL WORK FOR THE ABOVE QUESTION ABOVE THIS CELL
# THIS UNALTERABLE CELL CONTAINS HIDDEN TESTS
```

## 4. Evaluate the Model Performance

First, use the fitted model to generate `SalePrice` predictions for both the train and the test data. These variables should be called `y_pred_train` for the training data and `y_pred_test` for the testing data.

Make sure you use the scaled versions of the data!

We will use these predictions to evaluate the model performance.


```python
# Replace None with appropriate code
y_pred_train = None
y_pred_test = None
# your code here
raise NotImplementedError
```


```python
# Both should be NumPy arrays
assert type(y_pred_train) == np.ndarray
assert type(y_pred_test) == np.ndarray

# Should have the same shapes as y_train and y_test, respectively
assert y_pred_train.shape == y_train.shape
assert y_pred_test.shape == y_test.shape

# PUT ALL WORK FOR THE ABOVE QUESTION ABOVE THIS CELL
# THIS UNALTERABLE CELL CONTAINS HIDDEN TESTS
```

Now, use those predicted values to evaluate the model in terms of both:

* RMSE, using `mean_squared_error` ([documentation here](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html)) with `squared=False`
* R-squared, using `r2_score` ([documentation here](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html))

Apply these to both the train and test datasets. We have already imported the necessary functions; you just need to call the functions and pass in the appropriate data.


```python
# Replace None with appropriate code

from sklearn.metrics import mean_squared_error, r2_score

train_rmse = None
test_rmse = None

train_r2 = None
test_r2 = None

# your code here
raise NotImplementedError

print(f"""
RMSE
Train: {train_rmse} \t Test: {test_rmse}

R-squared
Train: {train_r2} \t Test: {test_r2}
""")
```


```python
# RMSE scores should be floating point numbers
assert type(train_rmse) == np.float64 or type(train_rmse) == float
assert type(test_rmse) == np.float64 or type(test_rmse) == float

# PUT ALL WORK FOR THE ABOVE QUESTION ABOVE THIS CELL
# THIS UNALTERABLE CELL CONTAINS HIDDEN TESTS
```


```python
# R-squared scores should be floating point numbers
assert type(train_r2) == np.float64 or type(train_r2) == float
assert type(test_r2) == np.float64 or type(test_r2) == float

# PUT ALL WORK FOR THE ABOVE QUESTION ABOVE THIS CELL
# THIS UNALTERABLE CELL CONTAINS HIDDEN TESTS
```

## 5. Interpret the Model Performance

Here's we'll focus on RMSE metrics, since those can be represented as "the average error in the price prediction".

Recall that the purpose of using regularization (e.g. a `Ridge` model) is to reduce overfitting.

Let's say that we previously used a basic ordinary least squares regression model, and we got RMSE scores of `$33,633.14` on the training data and `$39,255.80` on the test data. A full comparison of scores is in the table below:


```python
# Run this cell without changes
scores = pd.DataFrame([
    {"Model": "Linear Regression", "Train RMSE": 33633.14, "Test RMSE": 39255.80},
    {"Model": "Ridge Regression", "Train RMSE": 33910.84, "Test RMSE": 39213.66},
])
scores.set_index("Model", inplace=True)
scores.style.format("${:,.2f}")
```

Was our strategy of using a `Ridge` model to reduce overfitting successful? Which model is better?

Assign the variable `best_model_name` to either `"Linear Regression"` or `"Ridge Regression"`.

Recall that this is a predictive modeling context, so when we are defining the "best" model, we are interested in the model performance on unseen data.


```python
# Replace None with appropriate code
best_model_name = None
# your code here
raise NotImplementedError
```


```python
# Should be "Linear Regression" or "Ridge Regression"
assert best_model_name in ["Linear Regression", "Ridge Regression"]

# PUT ALL WORK FOR THE ABOVE QUESTION ABOVE THIS CELL
# THIS UNALTERABLE CELL CONTAINS HIDDEN TESTS
```
