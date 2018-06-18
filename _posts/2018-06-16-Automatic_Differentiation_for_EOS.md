---
layout: post
mathjax: true
title: Automatic Differentiation for Higher Order Derivatives
comments: true
---

## Executive Summary
Automatic differentiation as implemented in the Python package [`PyTorch`](https://pytorch.org/) is introduced.
Using the moderately complicated Redlich-Kwong equation of state, the ease of
obtaining higher order derivatives is illustrated.


The intended audience is for anyone interested in implementing thermodynamic
calculations from scratch, and is adventurous enough to try out the latest
tools developed by computer scientists. 
<!--more-->


Contents:
* Do not remove this line (it will not be displayed)
{:toc}


{% comment %}
# Automatic Differentiation
There are 3 ways to take derivatives of a known expression:

* Symbolic differentiation, either by hand or by computer algebra systems such
as [Mathematica](https://www.wolfram.com/mathematica/)
* Numerical differentiation, by computing finite difference
* Automatic differentiation


The reader should already be familiar with symbolic differentiation by hand.
Unlike integration, derivatives of any known expression can also be expressed
in similar simple symbols or elementary functions.
If we human can do it, what is so hard about it that we would need a computer
and at least few other ways to do it?

The typical challenge with human taking derivatives is that it is tedious,
error-prone, and still requires human implementation into software codes to be
useful.
For example the AGA8 equations of state includes about a dozen equations (see
equations 1 to 14 of [this journal paper](http://www.ijcea.org/papers/4-A504.pdf)).
Taking the partial derivatives, converting into software, and verify
correctness in those steps, surely take a good chunk of time.


Numerical differentiation reduce some of the pain but does not eliminate the
problem.
Here the expression is implemented in a programming language, then the function
is evaluated at few points close each other, whose rate of change over those
points can be used as an approximation of the derivative.
The problem with this approach lies in accuracy, and computational cost in
approximating the higher order derivatives.
To evaluate the gradient of a function that takes a vector of length $n$, we
would need 1 reference evaluation, plus $n$ more evaluations each time changing
only one element of the vector; that's already $n+1$ function evaluations.
Similarly to evaluate the Hessian matrix of second order partial derivatives,
we would need even more function evaluations.
Better hope the original function can be evaluate fast and cheaply, else it
would take a very long time.


Can we do better?
That is, can the computer be given a piece of code that implements the original
function, and then it can come up the correct partial derivatives readily
available for computing?
Turns out the recent advances in deep learning has just the solution for that.
And no we will not be training advanced neural networks to learn how to
manipulate symbols; rather the corner stone of the latest deep learning
packages leverages a computer science technique called automatic
differentiation that will take derivatives of functions implemented in a piece
of code.


At the risk of greatly simplify things, the core mathematical concept of
automatic differentiation lies in the chain rule.
Just as how we humans were taught on differentiation, we can teach the computer
to take derivative by recursively apply the chain rule until the resulting
terms to take derivative of is simple enough whose derivative is already known
or implemented.
Then for a given piece of computer program, the computer traces the
computational dependency consist of sub-function calls etc. and apply
appropriate 


# `PyTorch` Package in Python
{% endcomment %}

# Automatic Differentiation and `PyTorch`

Imagine that you have already implemented a function that does some
mathematical computation in the programming language of your choice.
Now you would like to evaluate the function's derivative.
How should you go about this?

You could write down the mathematical expression of the function you just
implemented, and with sufficient amount of patient, work out the derivatives on
paper.
Equivalently you could use computer algebra system such as [Mathematica](https://www.wolfram.com/mathematica).
Either way do you are doing symbolic differentiation, where the manipulations
are done on mathematical symbols (by you or by the computer), so that the
expression of the derivative is obtained.
Of course, unless you program within those computer algebra systems, you still
need to implement the derivatives in the programming language of your choice.
That is still work.

Alternatively we can try numerical differentiation.
Small perturbations are introduced to the inputs, and the finite difference
will be used for approximating the derivative.
Although requires the least human effort, it suffers from lower accuracy, and the
computational cost for higher order derivatives is just too much.

Can we do better?
Can the computer manipulate the program or function we just wrote and deduce
the derivative for us, such that we don't need to implement another function,
and get as accurate results as would have been obtained if we implement the
analytical derivatives by hand?
This is indeed possible with the computer science method called automatic
differentiation.
Although decades of research has been done on this topic, recent popularity of
deep learning saw engineering efforts pour into making packages out of it.
I claim ignorant of the principles and challenges of automatic differentiation
beyond what's mentioned in the [Wikipedia article](https://en.wikipedia.org/wiki/Automatic_differentiation), nonetheless this doesn't stop me from using software that implements
it.

I learned of the feasibility and practicality of automatic differentiation in
Python from [`PyTorch`](https://pytorch.org/), a free open source Python
package that does deep learning (i.e. think advanced neural networks),
developed by [Facebook](https://opensource.fb.com/#artificial).
Although the more mature and popular solution for deep learning on Python would
be [Google's `TensorFlow`](https://www.tensorflow.org/), I had chosen `PyTorch`
over `TensorFlow` mainly because `PyTorch` is much easier to debug.
That is a deal breaker for prototyping or R&D activities, especially since I
don't think I will ever deploy my code developed here on production
environment.

Finally I should point out that the automatic differentiation in `PyTorch` is
actually done by the [Python package `autograd`](https://github.com/HIPS/autograd)
written by [the HIPS group from Harvard University](http://hips.seas.harvard.edu/).
As a result, we really don't need `PyTorch`'s tensor objects to do automatic
differentiation; `autograd` can work with `numpy` directly.
Nonetheless anticipating that I will explore deep learning eventually, I chose
to study `PyTorch` rather than `autograd`.


# Illustration

Let's go over an example to see this in action.

## Evaluate the EOS
Before we jump into derivative computation, it would be wise to implement the
original function first, and check its validity.

### The Redlich-Kwong EOS
The [Redlich-Kwong equation of state](https://en.wikipedia.org/wiki/Redlich%E2%80%93Kwong_equation_of_state#Equation) states that:

$$
\begin{equation*}
  P = \frac{R ~ T}{v - b} - \frac{a}{\sqrt{T} ~ v ~ (v + b)}
\end{equation*}
$$

For this illustration, we shall take $R = 8.314$, $a = 29.08$, and $b = 8.09 \times 10^{-5}$, ignoring all units.
We can implemented this in Python:

{% highlight python linenos %}
def pressure(T, v):
    return 8.314 * T / (v - 8.09e-5) - 29.08 / (T**(0.5) * v * (v + 8.09e-5))
{% endhighlight %}


Suppose that we are interested in finding the pressure at temperatures
$T = \\{298.15, 313.15, 328.15, 343.15, 358.15\\}$, and corresponding molar
volumes of $v = \\{ 1.27, 1.6, 1.93, 2.26, 2.59\\} \times 10^{-3}$.
Utilizing the [`numpy` package](http://www.numpy.org/), we can do:

{% highlight python linenos %}
import numpy as np
T = np.arange(25 + 273.15, 100 + 273.15, 15)
v = np.linspace(1.27e-3, 2.59e-3, T.shape[0])
print(pressure(T, v))
{% endhighlight %}

Thanks to [`numpy`'s boardcasting rule](https://docs.scipy.org/doc/numpy/user/basics.broadcasting.html),
although both `T` and `v` are vectors, the operations defined in the `pressure`
function is computed element-wise.
As a result we should see a vector of 5 elements printed on screen:

```
[1102982.77629077 1102841.60120427 1061813.15861421 1012503.00041889
  964615.26519787]
```

### Switch to `PyTorch`
Without modifying the `pressure` function, we can perform the above calculation
using `PyTorch` as follows:

{% highlight python linenos %}
import torch
T = torch.tensor(np.arange(25 + 273.15, 100 + 273.15, 15), requires_grad=True)
v = torch.tensor(np.linspace(1.27e-3, 2.59e-3, T.shape[0]), requires_grad=True)
tc_pres = pressure(T, v)
print(tc_pres)
{% endhighlight %}

Here we leverage `PyTorch`'s synergy with `numpy` to create `PyTorch`'s tensor
objects directly from `numpy` array.
At the same time we enable gradient tracking whose purpose will be demonstrated
later.
As a result we should see the following printed on screen:

```
tensor(1.00000e+06 *
       [ 1.1030,  1.1028,  1.0618,  1.0125,  0.9646], dtype=torch.float64)
```

There are two programming "tricks" in play here.
The first is [broadcasting rule](https://pytorch.org/docs/master/notes/broadcasting.html), allowing element-wise computation just like
in the `numpy` case.
The other is [operator overloading](https://docs.python.org/3/reference/datamodel.html#special-method-names).
Under the hood both `numpy`'s `array` and `PyTorch`'s `tensor` are implemented
as classes that defines special methods such as `__mul__`.
Whenever the `*` is operated on such objects, the corresponding special methods
are called, and performing the corresponding calculation.
For example, the reader is invited to check that `T * 3` and `T.__mul__(3)`
returns the same results.
Hence we say the operator `*` typically only defined for numbers has been
overloaded for this class.


Finally we should check that the two methods returns the same calculations,
especially since `PyTorch`'s results are rounded to only 4 decimal places after
the period.
To do that we merely convert the `PyTorch`'s tensor back to `numpy` array and
compare using [`numpy`'s `allclose` function](https://docs.scipy.org/doc/numpy/reference/generated/numpy.allclose.html):

{% highlight python linenos %}
print(np.allclose(tc_pres.detach().numpy(), np_pres))
{% endhighlight %}


That's the beauty of `PyTorch`, who promises tight integration with `numpy` and
minimal disruption when migrating codes from `numpy` to `PyTorch`.


## The First Derivative
Now comes the main goal of this post: how to compute the derivatives
painlessly.
Specifically with $P = P(T, v)$ given by the Redlich-Kwong EOS, we would like
to find
$\left(\frac{\partial P}{\partial T}\right)_v$
and
$\left(\frac{\partial P}{\partial v}\right)_T$.

### Using `PyTorch`

The observant reader would probably already noted that when creating the `T`
and `v` tensors we specified `requires_grad=True`.
That is one half of the trick for using `PyTorch` to do automatic
differentiation.
That flag indicates that both `T` and `v` will participates in computations,
the derivatives of those results we are interested for, and we will be taking
derivatives with respect to `T` and `v`.
The second half of the trick would be asking `PyTorch` to compute the
derivatives for us.
To do that we simply write:

{% highlight python linenos %}
dPdT, dPdv = torch.autograd.grad(
    [tc_pres.sum()], [T, v],
    retain_graph=True,
    create_graph=True,
    allow_unused=True)
print("dP/dT:", dPdT)
print("dP/dv:", dPdv)
{% endhighlight %}

Here we are saying please take derivative of the element-wise sum of all values
in the vector `tc_pres` (i.e. `tc_pres.sum()`), and then take the gradient of
the sum with respect to `T` and `v`.
The keyward arguments are there to enable us computing higher order derivatives
later in this blog post without having to re-evaluate `tc_pres` first.

We should have the following printed on console:

```
dP/dT: tensor([ 8638.0527,  6448.5822,  5126.4844,  4247.6982,  3623.6443], dtype=torch.float64)
dP/dv: tensor(1.00000e+08 *
       [-2.5351, -3.8281, -3.7792, -3.4276, -3.0405], dtype=torch.float64)
```


### Mathematical Basis for `PyTorch` Code

Why do we need to take the sum of the resulting pressure vector first before
taking the derivative?
Well that's to get around some of the `PyTorch`'s limitations, namely, as of
version 0.4.0, we can only take derivative of a scalar with respect to any
tensor.

Traditionally one would first find the expression of the derivative, then plug
in the values to get the numerical results.
In our case we have 5 $T, v$ combinations at which we seek the gradient of $P$,
thus we would evaluate the gradient 5 times.
We can do the same thing in `PyTorch`, that is, iteratively compute a scalar
value of $P$ from scalars $T, v$, then use above to get the gradient, and
finally assemble them together.
However this would not be efficient since we will be managing the looping plus
it will prevent us from utilizing vectorized operations.

Instead observe that each element of the $\mathbf{P}$ vector depends only on 
the corresponding elements of the $\mathbf{T}, \mathbf{v}$ vectors.
When we take the derivative of the element sum of $\mathbf{P}$ with respect to
the elements of $\mathbf{T}$, each element of $\mathbf{T}$ contributes to
exactly one summand of sum of $\mathbf{P}$.
As a result the derivative of the sum of $\mathbf{P}$ with the $i$-th element
of $\mathbf{T}$ is the same as the derivative of the $i$-th element of
$\mathbf{P}$ with respect to the same variable.
In mathematical notation, we have:

$$
\begin{align*}
  \frac{\partial}{\partial T_i} \sum_j P_j &= \sum_j \frac{\partial}{\partial
T_i} P_j \\
  &= \sum_j \frac{\partial P_j}{\partial T_j} \times \frac{\partial T_j}{\partial T_i} \\
  &= \sum_j \frac{\partial P_j}{\partial T_j} \times \delta_i^j \\
  &= \frac{\partial P_i}{\partial T_i}
\end{align*}
$$

Where the second line follows the chain rule and $\delta_i^j$ is the [Kronecker
delta](https://en.wikipedia.org/wiki/Kronecker_delta) function.


### Compare Against Symbolic Differentiation

It is time to show that the derivatives evaluate above is actually correct.
The reader is invited to check that:

$$
\begin{align*}
  \frac{\partial P}{\partial T} &= \frac{R}{v - b} + \frac{a}{2 ~ T^{\frac{3}{2}} ~ v ~ (v + b)} \\
  \frac{\partial P}{\partial v} &= -\frac{R ~ T}{(v - b)^2} + \frac{a ~ (2 ~ v + b)}{\sqrt{T} ~ v^2 ~ (v + b)^2}
\end{align*}
$$

Implementing in Python with the following script:

{% highlight python linenos %}
def dP_by_dT(T, v):
    return 8.314 / (v - 8.09e-5) + 29.08 / (2 * T**(3 / 2) * v * (v + 8.09e-5))
def dP_by_dv(T, v):
    numerator = 29.08 * (2 * v + 8.09e-5)
    denominator = T**(1 / 2) * v**2 * (v + 8.09e-5)**2
    return -8.314 * T / (v - 8.09e-5)**2 + numerator / denominator
print(np.allclose(dPdT.detach().numpy(), dP_by_dT(T, v).detach().numpy()))
print(np.allclose(dPdv.detach().numpy(), dP_by_dv(T, v).detach().numpy()))
{% endhighlight %}

We see that both `print` statements print `True`, meaning the automatic
differentiation results agrees with the symbolic differentiation.

## Higher Order Derivatives

Have worked out the first order partial derivatives, the generalization into
the higher order derivatives is straight forward.
However care must be taken so that when summing a vector to work around the
scalar derivative limitation of `PyTorch`, the contributions of each elements
of $\mathbf{T}, \mathbf{v}$ vectors appears exactly once in the summands.

{% highlight python linenos %}
print(
    torch.stack(
        torch.autograd.grad(
            [dPdT.sum()], [T, v],
            retain_graph=True,
            create_graph=True,
            allow_unused=True)))
print(
    torch.stack(
        torch.autograd.grad(
            [dPdv.sum()], [T, v],
            retain_graph=True,
            create_graph=True,
            allow_unused=True)))
{% endhighlight %}

The results of running above commands are:

```
tensor([[-8.2821e+00, -4.6732e+00, -2.8809e+00, -1.8900e+00, -1.2988e+00],
        [-8.3948e+06, -4.7929e+06, -3.0715e+06, -2.1269e+06, -1.5564e+06]], dtype=torch.float64)
tensor([[-8.3948e+06, -4.7929e+06, -3.0715e+06, -2.1269e+06, -1.5564e+06],
        [-4.8874e+11,  1.2110e+11,  2.2322e+11,  2.1477e+11,  1.8428e+11]], dtype=torch.float64)
```

The reader is invited to check that those numerical values indeed can be
computed from:

$$
\begin{align*}
  \frac{\partial P}{\partial T^2} &= -\frac{3 ~ a}{4 ~ T^{\frac{5}{2}} ~ v ~ (v + b)} \\
  \frac{\partial P}{\partial T \partial v} &= -\frac{R}{(v - b)^2} - \frac{a ~ (2 ~ v + b)}{2 ~ T^{\frac{3}{2}} ~ v^2 ~ (v + b)^2} \\
  \frac{\partial P}{\partial v^2} &= -\frac{2 ~ R ~ T}{(v - b)^3} - \frac{2 ~ a ~ (b^2 + 3 ~ b ~ v + 3 ~ v^2)}{\sqrt{T} ~ v^3 ~ (v + b)^3}
\end{align*}
$$


