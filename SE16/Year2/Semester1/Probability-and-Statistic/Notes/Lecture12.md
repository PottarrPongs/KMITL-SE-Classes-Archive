# Lecture 12: Pair of Random Variables I | Joint CDF, Joint CDF, Joint PMF and Marginal PMF

$$\forall X, Y \text{where} X \text{and} Y \text{are RVs}$$

- $0 \le F_{X,Y}(x, y) \le 1$
- $F_{X}(x) = F_{X,Y}(x, \infty) \rightarrow \text{Marginal CDF of } X$
- $F_{Y}(y) = F_{X,Y}(\infty, y) \rightarrow \text{Marginal CDF of } Y$
- $F_{X,Y}(x, -\infty) = F_{X,Y}(\infty, y) = 0 \because P[x = -\infty] = P[y = -\infty] = P[\phi] = 0$
- $x \le x_{1} \text{ and } y \le y_{1} \rightarrow F_{X,Y}(x, y) \le F_{X,Y}(x_{1}, y_{1})$
- $F_{X,Y}(\infty, \infty) = 1$

$$F_{X,Y}(x, y) = P[X \le x, Y \le y]$$  
$$P_{X,Y}(x, y) = P[X = x, Y = y]$$  
$$S_{X,Y} = \{(x, y) | P_{X,Y} > 0\}$$



