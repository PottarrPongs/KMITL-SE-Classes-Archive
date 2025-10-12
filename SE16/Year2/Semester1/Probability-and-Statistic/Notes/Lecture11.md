# Lecture 11: Continuous Random Variable II | Families of Continuous RVs

## CDF of Continuous Random Variables


$$F_{X}(x) = P[X \le x]$$

- $F_{X}(-\infty) = 0$  
- $F_{X}(\infty) = 1$
- $P[x_{1} < X \le x_{2}] = F_{X}(x_{2}) - F_{X}(x_{1})$

$$f_{X}(x) = \frac{d \, F_{X}(x)}{d \, x}$$

- $\forall x. f_{X}(x) \ge 0$
- $F_{X}(x) = \displaystyle\int_{-\infty}^{\infty} f_{u}(u) \, dx$
- $\displaystyle\int_{-\infty}^{\infty} f_{X}(x) \, dx = 1$

$$E[X] = \displaystyle\int_{-\infty}^{\infty} x f_{X}(x) \, dx$$

  

$$E[g(X)] = \displaystyle\int_{-\infty}^{\infty} g(x) f_{X}(x) \, dx$$

$$Var[X] = \displaystyle\int_{-\infty}^{\infty}(x - \mu_{X})^2 f_{X}(x) \, dx$$

- $Var[X] = E[X^{2}] - \mu^{2}^{2}_{2}$


