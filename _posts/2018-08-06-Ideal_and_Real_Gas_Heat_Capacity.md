---
layout: post
mathjax: true
title: Ideal and Real Gas Heat Capacity
comments: true
---

## Executive Summary
An algebraic equation relating the real gas heat capacity and ideal gas heat
capacity is derived.
The equation is then re-parameterized into a form suitable for working with
pressure explicit equation of states.
Demonstration of correctiveness using the Peng-Robinson equation of state is
given with the aid of Mathematica.
<!--more-->


Contents:
* Do not remove this line (it will not be displayed)
{:toc}

# Ideal and Real Gas Heat Capacity
Consider a real gas with constant composition varying in temperature and
pressure.
Then its enthalpy can be calculated as:

$$
\begin{align*}
  dh &= \left( \frac{\partial h}{\partial T} \right)_P ~ dT + \left(
\frac{\partial h}{\partial P} \right)_T ~ dP \\
    &= C_P^{\text{real}} ~ dT + \left( -T ~ \left( \frac{\partial v}{\partial
T} \right)_P + v \right) ~ dP
\end{align*}
$$

Here $C_P^{\text{real}}$ is the real gas heat capacity, that depends on both
temperature $T$ and pressure $P$.
On the other hand, the ideal gas heat capacity $C_P^{\text{ideal}}$ is what's
usually tabulated, and conveniently depends only on the temperature $T$.
Then we can use a mathematical trick to relate those two together:

$$
\begin{equation*}
  C_P(T, P) = C_P(T) + \int_{P_{\text{ideal}}}^{P_{\text{real}}}
    \left( \frac{\partial C_P}{\partial P} \right)_T ~ dP
\end{equation*}
$$

This doesn't appear to be helpful at all, since we are still left with the
partial derivative of the real gas heat capacity with respect to pressure to
evaluate and integrate over.
Fortunately with the definition that $C_P = \left( \frac{\partial h}{\partial T} \right)_P$,
we can transform the derivative as:

$$
\begin{align*}
  \left( \frac{\partial C_P}{\partial P} \right)_T &= 
    \left( \frac{\partial}{\partial P} \left( \frac{\partial h}{\partial T} \right)_P \right)_T =
    \left( \frac{\partial}{\partial T} \left( \frac{\partial h}{\partial P} \right)_T \right)_P \\
    &= \left( \frac{\partial}{\partial T} \left( -T ~ \left( \frac{\partial v}{\partial T} \right)_P + v \right) \right)_P  \\
    &= - \left( \frac{\partial v}{\partial T} \right)_P - T \left( \frac{\partial^2 v}{\partial T^2} \right)_P + \left( \frac{\partial v}{\partial T} \right)_P \\
    &= - T \left( \frac{\partial^2 v}{\partial T^2} \right)_P
\end{align*}
$$

Thus if we know the equation of state, we can evaluate $- T \left( \frac{\partial^2 v}{\partial T^2} \right)_P$.
If in addition, expression for the ideal gas heat capacity is known,
then we can calculate the real gas heat capacity as:


$$
\begin{equation*}
  C_P^{\text{real}} = C_P^{\text{ideal}} + \int_{P_{\text{ideal}}}^{P_{\text{real}}}
    - T \left( \frac{\partial^2 v}{\partial T^2} \right)_P ~ dP
\end{equation*}
$$

As a result we can evaluate changes in the real gas enthalpy without
constructing appropriate thermodynamic just by integrating:

$$
\begin{align*}
  \Delta h =& \int_{T_1}^{T_2} C_P^{\text{ideal}} ~ dT +
      \int_{T_1}^{T_2} \int_{P_1}^{P_2} - T \left( \frac{\partial^2 v}{\partial T^2} \right)_P ~ dP ~ dT + \\
    &+ \int_{P_1}^{P_2} \left( -T ~ \left( \frac{\partial v}{\partial T} \right)_P + v \right) ~ dP

\end{align*}
$$

# Transformation for Pressure Explicit EOS

Above equation is written in a form that's best suited for volume explicit EOS
of the form $v = v(T, P)$.
However most of the commonly used EOS has the form $P = P(T, v)$.
As a result, a suitable transformation of the partial derivatives is required.

## First Order Partial Derivative

The transformation of the first order partial derivative is straight forward if
we apply the [triple product rule](https://en.wikipedia.org/wiki/Triple_product_rule):

$$
\begin{equation*}
  \left( \frac{\partial v}{\partial T} \right)_P =
    - \frac{ \left( \frac{\partial P}{\partial T} \right)_v }{ 
             \left( \frac{\partial P}{\partial v} \right)_T }
\end{equation*}
$$

However, we would be at lost trying to apply related transformation when
transforming the second order partial derivative.
Instead, we will apply a general technique via the use of the *Jacobian*.

## The Two Jacobian Rule

Suppose we have two functions $u(x, y)$ and $v(x, y)$.
Then we define the Jacobian as:

$$
\begin{equation*}
  \frac{\partial(u, v)}{\partial(x, y)} = \begin{vmatrix}
    \left(\frac{\partial u}{\partial x}\right)_y & \left(\frac{\partial u}{\partial y}\right)_x \\
    \left(\frac{\partial v}{\partial x}\right)_y & \left(\frac{\partial v}{\partial y}\right)_x
  \end{vmatrix}
\end{equation*}
$$

The most useful rule is the [two-Jacobian rule](https://ocw.mit.edu/courses/mathematics/18-02-multivariable-calculus-fall-2007/readings/non_ind_variable.pdf):

$$
\begin{equation*}
  \left(\frac{\partial u}{\partial v}\right)_w =
    \frac{ \frac{\partial(u, w)}{\partial(x, y)} }{
           \frac{\partial(v, w)}{\partial(x, y)} }
\end{equation*}
$$

Applied to the first order partial derivative, we obtain:

$$
\begin{align*}
  \frac{\partial(v, P)}{\partial(v, T)} &= \begin{vmatrix}
    \left(\frac{\partial v}{\partial v}\right)_T & \left(\frac{\partial v}{\partial T}\right)_v \\
    \left(\frac{\partial P}{\partial v}\right)_T & \left(\frac{\partial P}{\partial T}\right)_v
  \end{vmatrix} = \begin{vmatrix}
    1 & 0 \\
    \left(\frac{\partial P}{\partial v}\right)_T & \left(\frac{\partial P}{\partial T}\right)_v
  \end{vmatrix} = \left(\frac{\partial P}{\partial T}\right)_v \\

  \frac{\partial(T, P)}{\partial(v, T)} &= \begin{vmatrix}
    \left(\frac{\partial T}{\partial v}\right)_T & \left(\frac{\partial T}{\partial T}\right)_v \\
    \left(\frac{\partial P}{\partial v}\right)_T & \left(\frac{\partial P}{\partial T}\right)_v
  \end{vmatrix} = \begin{vmatrix}
    0 & 1 \\
    \left(\frac{\partial P}{\partial v}\right)_T & \left(\frac{\partial P}{\partial T}\right)_v
  \end{vmatrix} = - \left(\frac{\partial P}{\partial v}\right)_T \\

  \left(\frac{\partial v}{\partial T}\right)_P &=
    \frac{ \frac{\partial(v, P)}{\partial(v, T)} }{
           \frac{\partial(T, P)}{\partial(v, T)} } = 
    - \frac{ \left( \frac{\partial P}{\partial T} \right)_v }{ 
             \left( \frac{\partial P}{\partial v} \right)_T }
\end{align*}
$$

which is consistent with what we have obtained applying the triple product
rule.


## Second Order Partial Derivative

Here comes the fun part, where we wish to convert $ \left( \frac{\partial^2 v}{\partial T^2} \right)_P $
into an expression of partial derivatives of $P$ with respect to $T, v$.
We can start by leverage what we have done to the first order partial
derivative, letting

$$
\begin{equation*}
  f = \left(\frac{\partial v}{\partial T}\right)_P = 
    - \frac{ \left( \frac{\partial P}{\partial T} \right)_v }{ 
             \left( \frac{\partial P}{\partial v} \right)_T }
\end{equation*}
$$

However we can't apply the triple product rule here, since $f$ itself is an
expression of $P$.
Instead we have to use the two-Jacobian rule.

$$
\begin{align*}
  \frac{\partial(f, P)}{\partial(v, T)} &= \begin{vmatrix}
    \left(\frac{\partial f}{\partial v}\right)_T & \left(\frac{\partial f}{\partial T}\right)_v \\
    \left(\frac{\partial P}{\partial v}\right)_T & \left(\frac{\partial P}{\partial T}\right)_v
  \end{vmatrix} =
  \left(\frac{\partial f}{\partial v}\right)_T ~ \left(\frac{\partial P}{\partial T}\right)_v -
  \left(\frac{\partial P}{\partial v}\right)_T ~ \left(\frac{\partial f}{\partial T}\right)_v \\

  \frac{\partial(T, P)}{\partial(v, T)} &= \begin{vmatrix}
    \left(\frac{\partial T}{\partial v}\right)_T & \left(\frac{\partial T}{\partial T}\right)_v \\
    \left(\frac{\partial P}{\partial v}\right)_T & \left(\frac{\partial P}{\partial T}\right)_v
  \end{vmatrix} = \begin{vmatrix}
    0 & 1 \\
    \left(\frac{\partial P}{\partial v}\right)_T & \left(\frac{\partial P}{\partial T}\right)_v
  \end{vmatrix} = - \left(\frac{\partial P}{\partial v}\right)_T \\

  \left( \frac{\partial^2 v}{\partial T^2} \right)_P &= \left( \frac{\partial f}{\partial T} \right)_P =
  \frac{ \frac{\partial(f, P)}{\partial(v, T)} }{
         \frac{\partial(T, P)}{\partial(v, T)} } \\
  &= \frac{
      \left(\frac{\partial f}{\partial v}\right)_T ~ \left(\frac{\partial P}{\partial T}\right)_v -
      \left(\frac{\partial P}{\partial v}\right)_T ~ \left(\frac{\partial f}{\partial T}\right)_v \\
  }{  - \left(\frac{\partial P}{\partial v}\right)_T } \\
  &= \left(\frac{\partial f}{\partial T}\right)_v + \left(\frac{\partial f}{\partial v}\right)_T ~ f

\end{align*}
$$
