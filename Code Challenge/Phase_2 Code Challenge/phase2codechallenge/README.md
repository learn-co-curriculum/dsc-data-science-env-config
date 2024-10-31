# Phase 2 Code Challenge

This code challenge is designed to test your understanding of the Phase 2 material. It covers:

- Normal Distribution
- Statistical Tests
- Bayesian Statistics
- Linear Regression

_Read the instructions carefully_. You will be asked both to write code and to answer short answer questions.

## Code Tests

We have provided some code tests for you to run to check that your work meets the item specifications. Passing these tests does not necessarily mean that you have gotten the item correct - there are additional hidden tests. However, if any of the tests do not pass, this tells you that your code is incorrect and needs changes to meet the specification. To determine what the issue is, read the comments in the code test cells, the error message you receive, and the item instructions.

## Short Answer Questions 

For the short answer questions...

* _Use your own words_. It is OK to refer to outside resources when crafting your response, but _do not copy text from another source_.

* _Communicate clearly_. We are not grading your writing skills, but you can only receive full credit if your teacher is able to fully understand your response. 

* _Be concise_. You should be able to answer most short answer questions in a sentence or two. Writing unnecessarily long answers increases the risk of you being unclear or saying something incorrect.


```python
# Run this cell without changes to import the necessary libraries

import itertools
import numpy as np
import pandas as pd 
from numbers import Number
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

import pickle
```

---
## Part 1: Normal Distribution [Suggested time: 20 minutes]
---
In this part, you will analyze check totals at a TexMex restaurant. We know that the population distribution of check totals for the TexMex restaurant is normally distributed with a mean of \\$20 and a standard deviation of \\$3. 

### 1.1) Create a numeric variable `z_score_26` containing the z-score for a \\$26 check. 

**Starter Code**

    z_score_26 = 


```python
# your code here
raise NotImplementedError
```


```python
# This test confirms that you have created a numeric variable named z_score_26

assert isinstance(z_score_26, Number)

```

### 1.2) Create a numeric variable `p_under_26` containing the approximate proportion of all checks that are less than \\$26.

Hint: Use the answer from the previous question along with the empirical rule, a Python function, or this [z-table](https://www.math.arizona.edu/~rsims/ma464/standardnormaltable.pdf).

**Starter Code**

    p_under_26 = 


```python
# your code here
raise NotImplementedError
```


```python
# This test confirms that you have created a numeric variable named p_under_26

assert isinstance(p_under_26, Number)

# These tests confirm that p_under_26 is a value between 0 and 1

assert p_under_26 >= 0
assert p_under_26 <= 1

```

### 1.3) Create numeric variables `conf_low` and `conf_high` containing the lower and upper bounds (respectively) of a 95% confidence interval for the mean of one waiter's check amounts using the information below. 

One week, a waiter gets 100 checks with a mean of \\$19 and a standard deviation of \\$3.

**Starter Code**

    n = 100
    mean = 19
    std = 3
    
    conf_low = 
    conf_high = 


```python
# your code here
raise NotImplementedError
```


```python
# These tests confirm that you have created numeric variables named conf_low and conf_high

assert isinstance(conf_low, Number)
assert isinstance(conf_high, Number)

# This test confirms that conf_low is below conf_high

assert conf_low < conf_high

# These statements print your answers for reference to help answer the next question

print('The lower bound of the 95% confidence interval is {}'.format(conf_low))
print('The upper bound of the 95% confidence interval is {}'.format(conf_high))

```

### 1.4) Short Answer: Interpret the 95% confidence interval you just calculated in Question 1.3.

YOUR ANSWER HERE

---
## Part 2: Statistical Testing [Suggested time: 20 minutes]
---
The TexMex restaurant recently introduced queso to its menu.

We have a random sample containing 2000 check totals, all from different customers: 1000 check totals for orders without queso ("no queso") and 1000 check totals for orders with queso ("queso").

In the cell below, we load the sample data for you into the arrays `no_queso` and `queso` for the "no queso" and "queso" order check totals, respectively.


```python
# Run this cell without changes

# Load the sample data 
no_queso = pickle.load(open('./no_queso.pkl', 'rb'))
queso = pickle.load(open('./queso.pkl', 'rb'))
```

### 2.1) Short Answer: State null and alternative hypotheses to use for testing whether customers who order queso spend different amounts of money from customers who do not order queso.

YOUR ANSWER HERE

### 2.2) Short Answer: What would it mean to make a Type I error for this specific hypothesis test?

Your answer should be _specific to this context,_  not a general statement of what Type I error is.

YOUR ANSWER HERE

### 2.3) Create a numeric variable `p_value` containing the p-value associated with a statistical test of your hypotheses. 

You must identify and implement the correct statistical test for this scenario. You can assume the two samples have equal variances.

Hint: Use `scipy.stats` to calculate the answer - it has already been imported as `stats`. Relevant documentation can be found [here](https://docs.scipy.org/doc/scipy/reference/stats.html#statistical-tests).

**Starter Code**

    p_value = 


```python
# your code here
raise NotImplementedError
```


```python
# These tests confirm that you have created a numeric variable named p_value

assert isinstance(p_value, Number)

```

### 2.4) Short Answer: Can you reject the null hypothesis using a significance level of $\alpha$ = 0.05? Explain why or why not.

YOUR ANSWER HERE

---
## Part 3: Bayesian Statistics [Suggested time: 15 minutes]
---
A medical test is designed to diagnose a certain disease. The test has a false positive rate of 10%, meaning that 10% of people without the disease will get a positive test result. The test has a false negative rate of 2%, meaning that 2% of people with the disease will get a negative result. Only 1% of the population has this disease.

### 3.1) Create a numeric variable `p_pos_test` containing the probability of a person receiving a positive test result.

Assume that the person being tested is randomly selected from the broader population.

**Starter Code**
    
    false_pos_rate = 0.1
    false_neg_rate = 0.02
    population_rate = 0.01
    
    p_pos_test = 


```python
# your code here
raise NotImplementedError
```


```python
# This test confirms that you have created a numeric variable named p_pos_test

assert isinstance(p_pos_test, Number)

# These tests confirm that p_pos_test is a value between 0 and 1

assert p_pos_test >= 0
assert p_pos_test <= 1

```

### 3.2) Create a numeric variable `p_pos_pos` containing the probability of a person actually having the disease if they receive a positive test result.

Assume that the person being tested is randomly selected from the broader population.

Hint: Use your answer to the previous question to help answer this one.

**Starter Code**
    
    false_pos_rate = 0.1
    false_neg_rate = 0.02
    population_rate = 0.01
    
    p_pos_pos = 


```python
# your code here
raise NotImplementedError
```


```python
# This test confirms that you have created a numeric variable named p_pos_pos

assert isinstance(p_pos_pos, Number)

# These tests confirm that p_pos_pos is a value between 0 and 1

assert p_pos_pos >= 0
assert p_pos_pos <= 1

```

---

## Part 4: Linear Regression [Suggested Time: 20 min]
---

In this section, you'll run regression models with advertising data. The dataset includes the advertising spending and sales for 200 products. These products are a random sample of 200 products from a larger population of products. 

The dataset has three features - `TV`, `radio`, and `newspaper` - that describe how many thousands of advertising dollars were spent promoting the product. The target, `sales`, describes how many millions of dollars in sales the product had.


```python
# Run this cell without changes

import statsmodels
from statsmodels.formula.api import ols

data = pd.read_csv('./advertising.csv').drop('Unnamed: 0', axis=1)
X = data.drop('sales', axis=1)
y = data['sales']
```

### 4.1) Create a variable `tv_mod_summ` containing the summary of a fit StatsModels `ols` model for a linear regression using `TV` to predict `sales`. 

**Starter Code**

    tv_mod = ols(
    tv_mod_summ = tv_mod.summary()


```python
# your code here
raise NotImplementedError
```


```python
# This test confirms that you have created a variable named tv_mod_summ containing a StatsModels Summary

assert type(tv_mod_summ) == statsmodels.iolib.summary.Summary

# This statement prints your answer for reference to help answer the next question

print(tv_mod_summ)

```

### 4.2) Short Answer: Is there a statistically significant relationship between TV advertising spend and sales in this model? How did you determine this from the model output? 

This question is asking you to use your findings from the sample in your dataset to make an inference about the relationship between TV advertising spend and sales in the broader population.

YOUR ANSWER HERE

### 4.3) Short Answer: Run the cell below to produce a correlation matrix. Given the output, would you expect any collinearity issues if you included all of these features in one regression model? 


```python
# Run this cell

X.corr()
```

YOUR ANSWER HERE

### 4.4) Create a variable `all_mod_summ` containing the summary of a fit StatsModels `ols` model for a multiple regression using `TV`, `radio`, and `newspaper` to predict `sales`. 

**Starter Code**

    all_mod = ols(
    all_mod_summ = all_mod.summary()


```python
# your code here
raise NotImplementedError
```


```python
# This test confirms that you have created a variable named all_mod_summ containing a StatsModels Summary

assert type(all_mod_summ) == statsmodels.iolib.summary.Summary

# This statement prints your answer for reference to help answer the next question

print(all_mod_summ)

```

### 4.5) Short Answer: Does this model do a better job of explaining sales than the previous model using only the `TV` feature? Explain how you determined this based on the model output. 

YOUR ANSWER HERE
