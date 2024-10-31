# Linear Regression Checkpoint

This checkpoint is designed to test your understanding of linear regression.

Specifically, this will cover:

* Creating simple and multiple linear regression models with StatsModels
* Interpreting linear regression model metrics
* Interpreting linear regression model parameters

## Your Task: Build Linear Regression Models to Predict Home Prices

### Data Understanding

You will be using the Ames Housing dataset, modeling the `SalePrice` using these numeric features:

* `GrLivArea`: Above grade living area (square feet)
* `GarageArea`: Size of garage (square feet)
* `LotArea`: Lot size (square feet)
* `LotFrontage`: Length of street connected to property (feet)


```python
# Run this cell without changes

import pandas as pd
df = pd.read_csv("ames.csv", index_col=0)
df = df[["SalePrice", "GrLivArea", "GarageArea", "LotArea", "LotFrontage"]].copy()
df
```

### Modeling

You will apply an inferential modeling process using StatsModels. This means that you are trying to create the best model in terms of variance in `SalePrice` that is explained (i.e. r-squared), not RMSE or some other more user-friendly metric. For this reason you also will not use a train-test split.

You will build **two models — one simple linear regression model and one multiple linear regresssion model** — then you will interpret the model summaries.

There are two relevant components of interpreting the model summaries: model **metrics** such as r-squared and p-values, which tell you how well your model is fit to the data, and model **parameters** (intercept and coefficients), which tell you how the model is using the feature(s) to predict the target.

### Requirements

## 1. Build a Simple Linear Regression Using StatsModels

Below, we use the `.corr()` method to find which features are most correlated with `SalePrice`:


```python
# Run this cell without changes
df.corr()["SalePrice"]
```

The `GrLivArea` feature has the highest correlation with `SalePrice`, so we will use it to build a simple linear regression model.

Recall that the general structure of a StatsModels linear regression model is something like this:

```python
formula = 'y ~ x'
model = ols(formula, df).fit()
summary = model.summary()
```

Where `y` is the name of the target (dependent) variable, `x` is the name of the feature (independent) variable, and `df` is the dataframe containing both `y` and `x`.

In the cell below, fill in the appropriate values to create and summarize a simple linear regression model where `SalePrice` is the target and `GrLivArea` is the feature.


```python
from statsmodels.formula.api import ols

# Replace None with appropriate code
simple_formula = None
simple_model = None
simple_model_summary = None
# your code here
raise NotImplementedError
simple_model_summary
```


```python
import statsmodels

# simple_model should be a model fit with 1 feature
assert simple_model.df_model == 1

# simple_model_summary should be a StatsModels model summary
assert type(simple_model_summary) == statsmodels.iolib.summary.Summary

# PUT ALL WORK FOR THE ABOVE QUESTION ABOVE THIS CELL
# THIS UNALTERABLE CELL CONTAINS HIDDEN TESTS
```

## 2. Interpret Simple Linear Regression Model Metrics

We want to know:

1. How much of the variance is explained by this model? This is also known as the r-squared. Fill in `r_squared` with this value — a floating point number between 0 and 1.
2. Is the model statistically significant at $\alpha = 0.05$? This is determined by comparing the probability of the f-statistic to the alpha. Fill in `model_is_significant` with this value — either `True` or `False`.

You can either just look at the print-out above and fill in the values, or you can use attributes of `simple_model` ([documentation here](https://www.statsmodels.org/devel/generated/statsmodels.regression.linear_model.RegressionResults.html)). If you are getting stuck, it's usually easier to type the answer in rather than writing code to do it.


```python
# Replace None with appropriate code
r_squared = None
model_is_significant = None
# your code here
raise NotImplementedError
```


```python
import numpy as np

# r_squared should be a floating point value between 0 and 1
assert 0 <= r_squared and r_squared <= 1
assert type(r_squared) == float or type(r_squared) == np.float64

# PUT ALL WORK FOR THE ABOVE QUESTION ABOVE THIS CELL
# THIS UNALTERABLE CELL CONTAINS HIDDEN TESTS
```


```python
# model_is_significant should be True or False
assert model_is_significant == True or model_is_significant == False

# PUT ALL WORK FOR THE ABOVE QUESTION ABOVE THIS CELL
# THIS UNALTERABLE CELL CONTAINS HIDDEN TESTS
```

## 3. Interpret Simple Linear Regression Parameters

Now, we want to know what relationship the model has found between the feature and the target. Because this is a simple linear regression, it follows the format of $y = mx + b$ where $y$ is the `SalePrice`, $m$ is the slope of `GrLivArea`, $x$ is `GrLivArea`, and $b$ is the y-intercept (the value of $y$ when $x$ is 0).

In the cell below, fill in appropriate values for `m` and `b`. Again, you can use the print-out above or use attributes of `simple_model`.


```python
# Replace None with appropriate code

# Slope (coefficient of GrLivArea)
m = None

# Intercept (coefficient of Intercept)
b = None

# your code here
raise NotImplementedError

print(f"""
Our simple linear regression model found a y-intercept
of ${round(b, 2)}, then for every increase of 1 square foot
above-ground living area, the price increases by ${round(m, 2)} 
""")
```


```python
from numbers import Number

# m should be a number
assert isinstance(m, Number)

# PUT ALL WORK FOR THE ABOVE QUESTION ABOVE THIS CELL
# THIS UNALTERABLE CELL CONTAINS HIDDEN TESTS
```


```python
# b should be a number
assert isinstance(b, Number)

# PUT ALL WORK FOR THE ABOVE QUESTION ABOVE THIS CELL
# THIS UNALTERABLE CELL CONTAINS HIDDEN TESTS
```

## 4. Build a Multiple Regression Model Using StatsModels

Now, build a model that contains all of the features present in `df`. Recall that the general process for building a multiple regression model is something like this:

```python
formula = 'y ~ x_1 + x_2 + x_3'
model = ols(formula, df).fit()
summary = model.summary()
```

Where `y` and `df` are the same as in the previous example, but now there are multiple features represented by `x_1`, `x_2`, `x_3`, etc.

Specifically, your model should have `SalePrice` as the target, and these columns as features:

* `GrLivArea`
* `GarageArea`
* `LotArea`
* `LotFrontage`


```python
# Replace None with appropriate code
multiple_formula = None
multiple_model = None
multiple_model_summary = None
# your code here
raise NotImplementedError
multiple_model_summary
```


```python
# multiple_model should be a model fit with 4 features
assert multiple_model.df_model == 4

# multiple_model_summary should be a StatsModels model summary
assert type(multiple_model_summary) == statsmodels.iolib.summary.Summary

# PUT ALL WORK FOR THE ABOVE QUESTION ABOVE THIS CELL
# THIS UNALTERABLE CELL CONTAINS HIDDEN TESTS
```

## 5. Interpret Multiple Regression Model Metrics

Now we want to know: **is our multiple linear regression model a better fit than our simple linear regression model? We'll measure this in terms of percentage of variance explained (r-squared)**, where a higher r-squared indicates a better fit.

Replace `second_model_is_better` with either `True` if this model is better, or `False` if the previous model was better (or the two models are exactly the same).


```python
# Replace None with appropriate code
second_model_is_better = None
# your code here
raise NotImplementedError
```


```python
# second_model_is_better should be True or False
assert second_model_is_better == True or second_model_is_better == False

# PUT ALL WORK FOR THE ABOVE QUESTION ABOVE THIS CELL
# THIS UNALTERABLE CELL CONTAINS HIDDEN TESTS
```

**If we need to drop one feature from this model, which should it be?** Consider the p-values in the print-out above, as well as the correlations shown below.


```python
# Run this cell without changes

# Showing the average correlation with other features
# (including itself). This does NOT include correlations
# with SalePrice, only with other features
correlations = df.drop("SalePrice", axis=1).corr().sum() / 4
correlations
```

Replace `feature_to_drop` with the name of the features, which should be one of these four:

* `GrLivArea`
* `GarageArea`
* `LotArea`
* `LotFrontage`


```python
# Replace None with appropriate code
feature_to_drop = None
# your code here
raise NotImplementedError
```


```python
# feature_to_drop should be a string
assert type(feature_to_drop) == str

# It should be one of the features in df
assert feature_to_drop in df.columns

# PUT ALL WORK FOR THE ABOVE QUESTION ABOVE THIS CELL
# THIS UNALTERABLE CELL CONTAINS HIDDEN TESTS
```
