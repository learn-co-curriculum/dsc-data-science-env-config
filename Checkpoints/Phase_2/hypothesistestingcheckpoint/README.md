# Hypothesis Testing Checkpoint

This checkpoint is designed to test your understanding of the content from the Hypothesis Testing Cumulative Lab.

Specifically, this will cover:

* Identifying the null and alternative hypotheses
* Identifying Type I and Type II errors in this context
* Calculating a z-score test statistic
* Determining whether we can reject the null hypothesis based on this test statistic

## Your Task: Identifying Likely New Species

### Business Understanding

You are working for a natural resources ecology laboratory, with the goal of identifying new species of salamander. If a salamander sample seems to have different attributes than a similar, known species, then the laboratory can perform genetic testing to confirm the difference. This genetic testing is expensive, so they only want to use it when we have a statistically significant reason to believe that the sample is from a new species.

Before conducting genetic testing, they want evidence that the sample is drawn from a different population than the known species — some unknown species. They are willing to conduct unnecessary genetic testing (where it turns out that the sample is actually from the known species) 20% of the time.

In other words, we will be using an 80% significance level, i.e. $\alpha = 0.2$.

We have a new sample, and we want to know whether the sample is drawn from a population that is _smaller_ in length than the known species.

### Data Understanding

You are provided with:

* The mean length of the known species is 90mm. This is also known as $\mu_0$, the theoretical mean.
* The standard deviation of the known species length is 30mm. This is also known as $\sigma$ (sigma).
* The mean length of the salamander sample is 87mm.
* The sample contains 60 salamanders.

### Requirements

#### 1. Identify Null and Alternative Hypotheses

#### 2. Identify Type I and Type II Errors

#### 3. Calculate the z-score Test Statistic

#### 4. Determine Whether We Can Reject the Null Hypothesis

## 1. Identify Null and Alternative Hypotheses

Below we provide six possible hypotheses, labeled "A", "B", "C", "D", "E", and "F".

In this notation, $\mu$ is the mean length of the population that the sample was drawn from (possibly an unknown species), and $\mu_0$ is the known species mean length.

By default we are assuming that the sample's mean length is the same or greater than the known species mean length. ***We are seeking evidence that the sample's mean length is actually less than that of the known species***. In other words, we are completing a **one-tailed** experiment.

**A**: $\mu \neq \mu_0$

**B**: $\mu = \mu_0$

**C**: $\mu \leq \mu_0$

**D**: $\mu \geq \mu_0$

**E**: $\mu \lt \mu_0$

**F**: $\mu \gt \mu_0$

In the cell below, assign `null_hypothesis` and `alternative_hypothesis` to the appropriate string values.


```python
# Replace None with appropriate code
null_hypothesis = None
alternative_hypothesis = None

# your code here
raise NotImplementedError
```


```python
# Both values should be strings from "A" to "F"
q1_options = ["A", "B", "C", "D", "E", "F"]

assert null_hypothesis in q1_options

# PUT ALL WORK FOR THE ABOVE QUESTION ABOVE THIS CELL
# THIS UNALTERABLE CELL CONTAINS HIDDEN TESTS
```


```python
assert alternative_hypothesis in q1_options

# PUT ALL WORK FOR THE ABOVE QUESTION ABOVE THIS CELL
# THIS UNALTERABLE CELL CONTAINS HIDDEN TESTS
```

## Identify Type I and Type II Errors

Below we provide four possible scenarios, labeled "A", "B", "C", and "D". In two scenarios, an error has occurred, either Type I or Type II. In the other two scenarios, no error occurred.

**A**: We conclude with our statistical test that the sample salamanders **are smaller** than the known species salamanders, and genetic testing reveals that the sample salamanders **actually are from a different species** and are therefore smaller.

**B**: We conclude with our statistical test that the sample salamanders **are smaller** than the known species salamanders, but genetic testing reveals that the sample salamanders **actually are not from a different species** and are not actually smaller.

**C**: We conclude with our statistical test that **we don't have enough evidence to say that the sample salamanders are smaller** than the known species salamanders, but if they had run genetic testing it would have demonstrated that **they are a different species**.

**D**: We conclude with our statistical test that **we don't have enough evidence to say that the sample salamanders are smaller** than the known species salamanders, and in fact if they had run genetic testing it would have demonstrated that **they are not a different species**.

In the cell below, assign `type_1_error` and `type_2_error` to the appropriate string values.


```python
# Replace None with appropriate code
type_1_error = None
type_2_error = None

# your code here
raise NotImplementedError
```


```python
# Both values should be strings from "A" to "D"
q2_options = ["A", "B", "C", "D"]

assert type_1_error in q2_options

# PUT ALL WORK FOR THE ABOVE QUESTION ABOVE THIS CELL
# THIS UNALTERABLE CELL CONTAINS HIDDEN TESTS
```


```python
assert type_2_error in q2_options

# PUT ALL WORK FOR THE ABOVE QUESTION ABOVE THIS CELL
# THIS UNALTERABLE CELL CONTAINS HIDDEN TESTS
```

## 3. Calculate a z-score Test Statistic

In this case, we have access to the population standard deviation, so we will use this formula for the z-score:

$$ z = \frac{\bar{x} - \mu}{\sigma / \sqrt{n}} $$

Where $\bar{x}$ is the mean length of the salamander sample, $\mu$ is the mean length of the known species (population), $\sigma$ is the standard deviation of the known species, and $n$ is the number in the sample.

Calculate $z$ below.


```python
# Run this cell without changes

import scipy.stats as stats
from math import sqrt
import numpy as np
from numbers import Number

# Population mean
mu_0 = 90

# Population standard deviation
sigma = 30

# Mean length of salamander sample
x_bar = 87

# Number of salamanders in the sample
n = 60

# Alpha (1 - confidence level)
alpha = 0.2
```


```python
# Replace None with appropriate code
z = None
# your code here
raise NotImplementedError
z
```


```python
# z should be a negative floating point value
# (negative since the sample mean is smaller than the known species mean)
assert isinstance(z, Number)
assert z < 0

# PUT ALL WORK FOR THE ABOVE QUESTION ABOVE THIS CELL
# THIS UNALTERABLE CELL CONTAINS HIDDEN TESTS
```

## 4. Determine Whether We Can Reject the Null Hypothesis

Remember that our confidence level is 0.8 ($\alpha = 0.2$). Can we reject the null hypothesis at this confidence level?

Hint: Use the answer from the previous question along with the empirical rule, a Python function, or [this z-table](https://www.math.arizona.edu/~rsims/ma464/standardnormaltable.pdf).

In the cell below, perform any calculations you need, then assign `reject_null_hypothesis` to `True` or `False`.


```python
# Perform calculations

# Assign this to True or False
reject_null_hypothesis = None

# your code here
raise NotImplementedError

reject_null_hypothesis
```


```python
# This value should be True or False
assert reject_null_hypothesis == True or reject_null_hypothesis == False

# PUT ALL WORK FOR THE ABOVE QUESTION ABOVE THIS CELL
# THIS UNALTERABLE CELL CONTAINS HIDDEN TESTS
```
