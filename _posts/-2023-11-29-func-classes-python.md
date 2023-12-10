---
layout: post
title: Functions and classes in python:advance
date: 2023-11-29 # 10:14:00-0400
description: an example of a blog post with table of contents on a sidebar
categories: sample-posts toc sidebar
giscus_comments: true
related_posts: false
toc:
  sidebar: left
---

This post is about improving the understanding of functions and classes and utilising them better in Python and in general. After all, we have taken a course that teaches OOPs or watched some YouTube videos, but when we write independently, we struggle and look for help online. It is about moving from a copy-paster to writing your functions and classes with much clarity of what I am doing, making the code more beautiful and understandable by myself and everyone else. I will also try to draw some examples of popular machine learning libraries with the hope of making us a better programmer in general and using what pyhton offers us in a better way. 

On a personal note: Tutorials don't work because they mostly use very simple exmaples or problems, which takes away the importance of some concepts, and we are left with the just the term which we don't understand unless we use the same concept to work on some real problem. Hence I'll try to give some examples that might stuck and stop you from scrolling mindlessly, because our attention requires something dramatic these days to stick.

However if you're a person who reads from the official documentation of the language and use it for your work, all this might be redundant for you.

way to learn and use:
1. read the idea: what is this about and why it is important. It's not just about something a programming language provides, it is useful only if we can apply to solve some problem with a appreciatable advantage where something simple works and there is no future need to change or expand. 
2. example and execute it yourself
3. how to implement in your code? 

### Contents:
1. Why we use functions and classes? 
    - Why we use functions? ; 
    - Why are classes needed in programming? 
    - 
2. How are they written in good way? Taking examples from sklearn and pytorch.
3. What extra functionalities or capabilties do we have with them?


## Why do we use functions and classes?
Although the way we use computers is so beautifully abstracted that we even forget that everything at the end involves opertations with 0s and 1s, many of the things in computers have relation to mathematics. As per wikipedia, ["In mathematics, a function from a set X to a set Y assigns to each element of X exactly one element of Y"](https://en.wikipedia.org/wiki/Function_(mathematics)). The function we use in programming are not much different either. Whether you are using some in-built functions like [dir(), sort() and others](https://docs.python.org/3/library/functions.html#abs) of the language or writing your own. Func fact: the built-in functions are written in C language.  Now you're saying "yeah we all know this stuff and we don't want the same boring stuff". 

### Example 1: arguments of a function
You might already know that *args and **kwargs are followed by positional arguments and you can use them in the following way: 

[\\]: https://docs.python.org/3/tutorial/controlflow.html#function-examples
### Example 2: partial functions

### Example 3: wrappers and decorators

In maths, we can have composition of functions, for example, composition of $$ f(x) = |x| $$ and  $$ g(x) = sin(x) $$  as  $$ f(g(x)) = |sin(x)| $$. We can also have $$ g(f(x)) = sin(|x|) $$, i.e. we enhance the normal functions by composing them. Even neural networks are composition of functions (in the form of layers) that form a complex function. Here in programmming, we can do something with an existing function or before or after its call or simply modify it's output(Avoidig redundancy and adding/extending behaviour and higher order functions). In python, we can wrap an existing function inside another function by passing the existing function and do something over it. In python there are two different ways of doing something on top of an existing function with different functionality.
Let's first define an existing function on which we want to add some extra functionality.
```python
def existing_function(x):
    return x * 3
```
#### 1. Wrapper
A wrapper takes a function as input with arguments that the existing function requires and does something on it and returns the result.
```python
def wrapper_func(f, *args, **kwargs):
    return 2 * f( *args, **kwargs)

```
The above wrapper simply takes an existing function and arguments and returns the output of existing function multiplied by 2.

```python
wrapper_func(existing_function,"4")
'444444'
wrapper_func(existing_function,4)
24

```
#### 2. Decorators
The use of wrapper is quite nice but as python keeps on adding more abstract API that makes it easy for us. Here it is in the form of decorators which can be simply used with @ followed by the function name. There are few built-in decorators like @abstractmethod, @property etc. We can also define our own decorators and use them with existing functions as many times as we like.


```python

def twice_decorator(f):
  def wrapper_function(*args, **kwargs):
      return 2* f(*args, **kwargs)
    return wrapper_function

```
```python
@twice_decorator
def existing_function(x):
  return x * 3
```
```python
existing_function("4")
'444444'
existing_function(4)
24
```
```python
@twice_decorator
@twice_decorator
def existing_function(x):
  return x * 3
```
```
existing_function(4)
48
existing_function("4")
'444444444444'

```
What about mathematical way of composition of functions? Here it is:
```
def some_function(x):
    return x * x
decorated_some_function = twice_decorator(some_function)
```
```
decorated_some_function(10)
200
```
Yes, it's fun to play with these toy examples, that's why they are called so. But real world examples more of complex toys which requires more understanding before we can enoy playing them.
Let's have a look at the code of [NearestNeighbors](https://github.com/scikit-learn/scikit-learn/blob/3f89022fa04d293152f1d32fbc2a5bdaaf2df364/sklearn/neighbors/_unsupervised.py#L154) from sklearn package. The fit method in the NearestNeighbors class had a "@_fit_context()" decorator. Similarly fit methods in other estimator classes also has this. 

```python
sklearn/neighbors/_unsupervised.py

"""Unsupervised nearest neighbors learner"""
from ..base import _fit_context
from ._base import KNeighborsMixin, NeighborsBase, RadiusNeighborsMixin

class NearestNeighbors(KNeighborsMixin, RadiusNeighborsMixin, NeighborsBase):
    """Unsupervised learner for implementing neighbor searches.
    ...SKIPPED FOR THIS BLOG...
    """

    def __init__(
        self,
        *,
        n_neighbors=5,
           ...SKIPPED FOR THIS BLOG...

    ):
        super().__init__(
            n_neighbors=n_neighbors,
               ...SKIPPED FOR THIS BLOG...

        )

    @_fit_context(
        # NearestNeighbors.metric is not validated yet
        prefer_skip_nested_validation=False
    )
    def fit(self, X, y=None):
        """Fit the nearest neighbors estimator from the training dataset.
    ...SKIPPED FOR THIS BLOG...

        Returns
        -------
        self : NearestNeighbors
            The fitted nearest neighbors estimator.
        """
        return self._fit(X)
```
Now let's have a look at the _fit_context() method in the base class. It turns out there is another decorator inside fit_context() that decorates the above fit() method and returns the decorated fit method. Hence it's decorator inside decorator where the outer decorator simply returns the inner decorator utilising the argument "prefer_skip_nested_validation", which does the actual stuff as running the fit method within context manager. It's not easy to  wrap head around this. 

```python
sklearn/base.py

def _fit_context(*, prefer_skip_nested_validation): 
    """Decorator to run the fit methods of estimators within context managers.
    ...SKIPPED FOR THIS BLOG...

    Parameters
    ----------
    prefer_skip_nested_validation : bool
        ...SKIPPED FOR THIS BLOG...

    Returns
    -------
    decorated_fit : method
        The decorated fit method.
    """

    def decorator(fit_method):
        @functools.wraps(fit_method)
        def wrapper(estimator, *args, **kwargs):
            global_skip_validation = get_config()["skip_parameter_validation"]

            # we don't want to validate again for each call to partial_fit
            partial_fit_and_fitted = (
                fit_method.__name__ == "partial_fit" and _is_fitted(estimator)
            )

            if not global_skip_validation and not partial_fit_and_fitted:
                estimator._validate_params()

            with config_context(
                skip_parameter_validation=(
                    prefer_skip_nested_validation or global_skip_validation
                )
            ):
                return fit_method(estimator, *args, **kwargs)

        return wrapper

    return decorator
```



<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">First column **fields**</td>
<td markdown="span">Some descriptive text. This is a markdown link to [Google](http://google.com). Or see [some link][mydoc_tags].</td>
</tr>
<tr>
<td markdown="span">def _fit_context(*, prefer_skip_nested_validation) </td>
<td markdown="span">Here the * is used to force the usage of keyword argument. It is done so that user of this function always mention the keyword before passing some value to it.
</td>
</tr>
</tbody>
</table>

[//]: source code of builtin in pythons https://github.com/python/cpython/blob/d4a6229afe10d7e5a9a59bf9472f36d7698988db/Python/bltinmodule.c#L295