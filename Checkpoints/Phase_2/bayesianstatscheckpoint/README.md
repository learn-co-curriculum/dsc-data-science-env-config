# Bayesian Statistics

This checkpoint is designed to test your understanding of applying Bayes' theorem.

Specifically, this will cover:

* Interpreting a word problem and applying Bayes' theorem
* Manipulating the elements of Bayes' theorem to a given problem context

## Your Task: Calculate Probabilities Using Bayes' Theorem

### Problem Context

Thomas is going to get a new puppy. There are two major decisions involved: what _location_ he gets the puppy from, and what _size_ the puppy is.

The possible **locations** for getting the puppy are the **pet store** or the **pound**. These are mutually exclusive and collectively exhaustive probabilities, meaning that Thomas will only go to one location, and there is a 100% probability that he will go to one of these two locations. We'll represent those probabilities as $P(Pet Store)$ and $P(Pound)$ as needed.

The possible puppy **sizes** are **small**, **medium**, or **large**. Again, these are mutually exclusive and collectively exhaustive probabilities, so a given puppy has only one size and there is a 100% probability that Thomas will get a puppy with one of these three sizes. We'll represent those probabilities as $P(Small)$, $P(Medium)$, and $P(Large)$ as needed.

### Known Probabilities

1. $P(Pet Store) = 0.2$
   * The probability of Thomas going to the pet store is 20%
2. $P(Small \mid Pet Store) = 0.6$
   * If he goes to the pet store, the probability of him getting a small puppy is 60%
3. $P(Medium \mid Pet Store) = 0.3$
   * If he goes to the pet store, the probability of him getting a medium puppy is 30%
4. $P(Large \mid Pet Store) = 0.1$
   * If he goes to the pet store, the probability of him getting a large puppy is 10%
5. $P(Small \mid Pound) = 0.1$
   * If he goes to the pound, the probability of him getting a small puppy is 10%
6. $P(Medium \mid Pound) = 0.35$
   * If he goes to the pound, the probability of him getting a medium puppy is 35%
7. $P(Large \mid Pound) = 0.55$
   * If he goes to the pound, the probability of him getting a large puppy is 55%

### Formula Reminders

This is the formula for Bayes' theorem:

$$P(A \mid B) = \dfrac{P(B \mid A)P(A)}{P(B)}$$

In other words, the probability of A given B is the probability of B given A times the probability of A, divided by the probability of B.

Additionally, recall the law of total probability:

$$P(A) = \sum_i P(A \mid B_i)P(B_i)$$

In other words, the probability of A is the sum of all (probability of A given B times the probability of B) for all B.

### Requirements

#### 1. What is the probability of Thomas getting a small puppy?

#### 2. Given that he got a large puppy, what is the probability that Thomas went to the pet store?

## 1. What is the probability of Thomas getting a small puppy?

In other words, what is $P(Small)$?

We recommend that you make as many intermediate variables as you need, to represent the known probabilities listed above and to plug them into the appropriate formula. It is also helpful to include comments to help you keep track of your logic.

Assign your answer to `p_small`.


```python
# Replace None with appropriate code
p_small = None
# your code here
raise NotImplementedError
p_small
```


```python
# PUT ALL WORK FOR THE ABOVE QUESTION ABOVE THIS CELL
# THIS UNALTERABLE CELL CONTAINS HIDDEN TESTS

# p_small should be a floating point probability between 0 and 1
assert type(p_small) == float
assert 0 <= p_small and p_small <= 1
```


```python
# PUT ALL WORK FOR THE ABOVE QUESTION ABOVE THIS CELL
# THIS UNALTERABLE CELL CONTAINS HIDDEN TESTS
```

## 2. Given that he got a large puppy, what is the probability that Thomas went to the pet store?

In other words, what is $P(Pet Store \mid Large)$?

Hint: In order to calculate this answer, you will need to calculate $P(Large)$. Note that there are 3 sizes of puppy (small, medium, and large), so you can't just subtract $P(Small)$ from 1.

Assign your answer to `p_pet_store_given_large`.


```python
# Replace None with appropriate code
p_pet_store_given_large = None
# your code here
raise NotImplementedError
p_pet_store_given_large
```


```python
# PUT ALL WORK FOR THE ABOVE QUESTION ABOVE THIS CELL
# THIS UNALTERABLE CELL CONTAINS HIDDEN TESTS

# p_small should be a floating point probability between 0 and 1
assert type(p_pet_store_given_large) == float
assert 0 <= p_pet_store_given_large and p_pet_store_given_large <= 1
```


```python
# PUT ALL WORK FOR THE ABOVE QUESTION ABOVE THIS CELL
# THIS UNALTERABLE CELL CONTAINS HIDDEN TESTS
```
