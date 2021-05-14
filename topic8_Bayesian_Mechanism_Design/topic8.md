## Topic 8: Bayesian Mechanism Design
### 8.A Allocation rule under quasilinearity with BNE
**Question.** Does there exist $D(q,t)$ such that
1. $q$ is efficient.
2. $\sum_i t_i(\theta) = 0$ for all $\theta$.
3. Truthful reporting is a BNE of $D(q,t)$?

* Bayesian Nash Equilibrium (BNE)
  * Need players’ beliefs about other players types. 
    * A player’s utility depends on the group choice outcome
    -> Group choice outcome depends on other players’ strategies
    -> Other players’ strategies depend on their types.
    * Dominant strategy is best response to all realized strategy profiles; but BNE only needs best response to one's belief.
    * Beliefs: $\theta_i, i=1,...,n$ are independently distributed with $F_i$ with density $f_i$.
      * <mark>Why independent?</mark>
  * **Proposition.** [d’Aspremont and G´erard-Varet] If types are independently distributed, then the direct mechanism $D(q,t)$ such that $q$ is efficient and 
    $$
    t_i(\theta) = \mathbb{E}[-\sum_{j \neq i} v_j(q(\theta), \theta_j] + \tau_i(\theta_{-i})
    $$
    for any function $\tau_i: \Theta_{-i} \to \mathbb{R}$ is truth-compatible in BNE.
    * $\mathbb{E}[-\sum_{j \neq i} v_j(q(\theta), \theta_j]$ only depends on $\theta_i$.
    * Budget constraint is easily satisfied: set 
        $$\tau_i(\theta_{-i}) = -\frac{1}{n-1} \sum_{j \neq i} K_j(\theta_j)$$
        , where $K_j = \mathbb{E}[k_j(\theta_j, \theta_{-j})]$ for $k_j(\theta_j, \theta_{-j}) := -\sum_{i \neq j} v_i(q(\theta), \theta_i)$.
  * Bayesian implementation:
    * In general, types are jointly distributed over $n$ by $F$.
      * $F$ is common prior.
      * If $i$’s type is $\theta_i$, his conditional belief is $F(\theta_{-i} | \theta_i)$.
      * If types are independent, $F(1,...,n) = \prod F_i(\theta_i) \Rightarrow F(\theta_{-i} | \theta_i) = \prod_{j \neq i} F_j(\theta_j)$.

**Question.** $D(q,t)$ can be a BNE. Does there exist $(\Gamma,\sigma^*)$ such that
1. $\sigma^*$ is a BNE of $\Gamma$
2. $g^{\Gamma,\sigma^*} = g$?

**Truth-compatible in BNE.**
$D(g)$ is truth-compatible in BNE if everyone reporting truthfully is a BNE of the mechanism.
* If $D(g)$ is truth-compatible in dominant strategies, it must be also truth-compatible in BNE. Not vice versa.
* BNE is weaker in true-compatible, in a sense that one is willing to report truthfully, on the condition that everyone else reports truthfully.



---
**Revelation Principle** (for BNE)

If $g$ is the outcome function of an arbitrary mechanism $\Gamma$ and a BNE $\sigma^*$ of it, then direct mechanism $D(g)$ is truth-compatible in BNE. 

<mark>*Proof:*</mark>


  
*Remark:*
* To implement $g$ in BNE, WLOG can focus on direct mechanisms.
* No need to worry about sequential rationality (one-shot game is deterministic).
* If $g$ is implementable in dominant strategies, it is implementable
in BNE.
  
---

### 8.B Bayesian Implementation: One-dimensional types
* Assume "One-dimensional types" to pin down all BNE-implementable
group choice functions.
  * $\Theta = \mathbb{R}_+$: types are one-dimensional and bounded from below.
  * $v_i(q,\theta_i) = \theta_iw_i(q)$: Valuation is linear in type.
  * Types are independently distributed.
* BNE truth-compatible direct mechanisms $D(q,t)$:
  * $U_i(\theta_i)$: expected payoff from truth-telling eq
    $$U_i(\theta_i) = \theta_i\mathbb{E}[w_i(q(\theta_i,\theta_{i}))] - \mathbb{E}[t_i(\theta_i,\theta_{i})]$$
  * $D(q,t)$ is truth-compatible in BNE iff $U_i(\theta_i) = \theta_i W_i(\theta_i) - T_i(\theta_i) \geq \theta_i W_i(\theta'_i) - T_i(\theta'_i)$ for any misreporting $\theta'_i$. [IC]
* **Proposition.** [Characterization] $D(q,t)$ is truth-compatible in BNE (and hence $(q,t)$ is implementable in BNE) if and only if
  * $W_i(\theta_i)$ is non-decreasing in i .
  * $U_i(\theta_i)$ is a.e. differentiable, and when it is differentiable,
    $$U'_i(\theta_i) = W_i(\theta_i)$$
    *Proof:*\
    Suppose truth-compatible, then pick any $\theta'_i > \theta_i$, from IC,
    $$U_i(\theta_i) = \theta_i W_i(\theta_i) - T_i(\theta_i) \geq \theta_i W_i(\theta'_i) - T_i(\theta'_i) \quad (1)$$
    $$U_i(\theta'_i) = \theta'_i W_i(\theta'_i) - T_i(\theta'_i) \geq \theta'_i W_i(\theta_i) - T_i(\theta_i) \quad (2)$$
    (1)+(2) gives $(\theta_i - \theta'_i)(W_i(\theta_i) - W_i(\theta'_i)) \geq 0$, which implies $W_i(\theta_i)$ is non-decreasing.\
    From (1), $\frac{U_i(\theta_i) - U_i(\theta'_i)}{\theta_i - \theta'_i} \geq W_i(\theta'_i)$.\
    From (2), $\frac{U_i(\theta_i) - U_i(\theta'_i)}{\theta_i - \theta'_i} \leq W_i(\theta_i)$.\
    Let $\theta'_i \to \theta_i$, then we have $U'_i(\theta_i) = W_i(\theta_i)$.
* **Corollary.** [Revenue Equivalence]
  * $U_i(\theta_i) = U_i(0) + \int_0^{\theta_i} W_i(s)ds = T_i(0) + \int_0^{\theta_i} W_i(s)ds$ 
    * Utility is decided by allocation, given the lowest utility level.
  * $T_i(\theta_i) = T_i(0) + \theta_i W_i(\theta_i) - \int_0^{\theta_i} W_i(s)ds$
    * Transfer is pinned by allocation, given the lowest transfer level.
* To pin down $D(q,t)$, can think about $q$ and $t$ separately.
  * Step 1. First think about allocation rule $q$ making $W_i$ non-decreasing and implementable.
  * Step 2. Freely choose $T_i(0)$ for the type 0 guy.
  * Step 3. Set transfer rules $t_i(\theta) = T_i(\theta_i)$ using Corollary.

### 8.C Application 1: Literal Revenue Equivalence in Auctions
**Proposition.** [Revenue Equivalence for Auctions] If $(\Gamma^A,\sigma^A)$ and $(\Gamma^B,\sigma^B)$ are two auctions (and corresponding BNE) in which
* The highest valuation player gets the painting,
* Type 0 player pays nothing,

then they generate the same expected revenue.

*Proof:*

*Remark:*
* First-price, second-price, English, Dutch generate same revenue, because they all have BNE in which only highest valuation guy wins and pays.
* The expected revenues are the same as long as two mechanisms imply
  * the same allocation rule as part of the outcome function, 
  * the same expected payment from the type 0 player.

### 8.D Application 2: Optimal Auction
**Proposition.** [Myerson Optimal Auction] If  $\psi_i(\theta_i) = \theta_i - \frac{1 - F_i(\theta_i)}{f_i(\theta_i)}$ is increasing for every $i$, direct mechanism $D(q,t)$ given as the
following is a revenue-maximizing auction:
$$
q_i(\theta_i,\theta_{-i}) = \begin{cases}
1,\quad &\psi_i(\theta_i) > max_{j \neq i}(\psi_j(\theta_j),0)  \\\\
0,\quad &otherwise
\end{cases}
$$
$$t_i(\theta) = \theta_i W_i(\theta_i) - \int_o^{\theta_i} W_i(s)ds$$

*Remark:*
* $q$ is not necessarily efficient.
* Gives painting to guy with highest non-negative $\psi_i$ — virtual type.
  * Highest virtual type guy is not necessarily the highest type guy.
  * Highest virtual type guy is highest type guy if $F1 = ... = F_n$.
* Highest virtual type can be 0 — some chance of not selling
  * q is not efficient even if $F1 = ... = F_n$, since $\psi_i(0) < 0$.

**Optimal auction when types are i.i.d.**
* Suppose $F1 = ... = F_n$, then $\psi_1 = ... = \psi_n = \psi$.
* $\rho$: $\psi(\rho) = 0$.
  * $\theta_i > \rho$: some chance of winning.
  * $\theta_i < \rho$: no chance of winning.
* $$
  q_i(\theta_i,\theta_{-i}) = \begin{cases}
  1,\quad &\theta_i > max_{j \neq i}(\theta_j,\rho)  \\\\
  0,\quad &otherwise
  \end{cases}
  $$
* **Corollary.** If types are **i.i.d**, then second-price auction with reserve price is a revenue-maximizing mechanism.

**Correlated types.**
* For $(q,t)$ being implementable in BNE, one can find a truth-compatible direct mechanism $D(q,\hat{t})$ that implements $(q,t)$ "in expectation".
* Design of "bonus" system $\nu_i(\theta)$, such that $\mathbb{E}[\nu_i(\theta) | \theta_i] = 0$.
  * Let $\hat{t_i}(\theta) = t_i(\theta) - \nu_i(\theta)$, then $\mathbb{E}[\hat{t_i}(\theta) | \theta_i] = \mathbb{E}[t_i(\theta) | \theta_i]$.
* Apply IC constraint, such that $D(q,\hat{t})$ is truth-compatible in BNE.
* Implementation:
  * Infer from guess, reward or punish by $\nu_i(\theta)$.
  * Apply $D(q,\hat{t})$ from revealed type.
  * Final transfer is $t_i = \hat{t_i} + \nu_i$.
* **Proposition.** [Cr´emer and McLean] If the players’ preferences are quasilinear, and types are "sufficiently correlated", then for any group choice function $(q,t)$ there is a BNE-implementable group choice function $(\hat{q},\hat{t})$ such that:
  * $q = \hat{q}$
  * $\mathbb{E}[\hat{t_i}(\theta_i,\theta_{-i}) | \theta_i] = \mathbb{E}[t_i(\theta_i,\theta_{-i}) | \theta_i]$
  * *Remark*: 
    * **Sufficiently correlated**: types are distributed as $F$ such that $F(\cdot | \theta_i)$ is not in the convex hull of $\{F(\cdot | \theta'_i): \theta'_i \neq \theta_i \}$ for all $i$ and $\theta_i$.
    * Sufficiently correlated is violated if $F(\cdot | \theta_i) = F(\cdot | \theta'_i)$ for some $\theta'_i \neq \theta_i$, which is the case in independently distributed types.
    * What would seller do if the seller knows the types in the first place?
      * Sell to the highest valuation guy.
      * Charge him exactly his type.
      * Let $(q,t)$ be this “ideal” group choice function.
    * Even if seller doesn’t know the types, he can use $D(q,\hat{t})$ that implements $(q,t)$ in expectation.
      * Since the expected transfers are the same under t and ^t, expected
      revenues are also the same.
      * In expectation seller’s revenue is the same as ideal.
      * Full surplus extraction: $U_i(\theta_i) = 0$.


### 8.E Questions
Consider a seller who wants to allocate a painting to one of the two buyers, where the type
(value of the painting) of the buyers are not statistically independent. We consider a discrete
case. Each of two buyer may have a value of $\theta_i = 10$ or $\theta_i = 100$ for the painting. Let us
assume that the joint probability distribution for value $(\theta_1,\theta_2)$ is:
$$Pr(10,10) = Pr(100,100) = \frac{1}{3}$$
$$Pr(10,100) = Pr(100,10) = \frac{1}{6}$$
Assume that the seller has zero valuation of the painting. The buyer's utility is given by $u_i = \theta_i q_i(\theta) - t_i(\theta)$, where $q_i$ is the allocation probability and $t_i(\theta)$ is the payment, which can be negative. Characterize the optimal auction $(q^*(\theta),t^*(\theta))$. Compare it with the independent case.

*Sol:*
* $p := \frac{p_h}{p_l + p_h} = \frac{2}{3}$
* $\nu_i(100,100) = \nu_i(10,10) = (1-p)C$, $\nu_i(10,100) = \nu_i(100,10) = -pC$
  * Let $C = 90$, guess right, reward $(1-p)C = 30$; guess wrong, punish $pC = -60$.
* $100$ will guess $100$, $10$ will guess $10$.
* $(q,\hat{t})$: 
  * $$
    q_i(\theta) = \begin{cases}
    1,\quad &\theta_i = max(\theta), \theta_1 \neq \theta_2  \\\\
    \frac{1}{2},\quad &\theta_1 = \theta_2  \\\\
    0,\quad &otherwise
    \end{cases}
    $$
  * $$
    \hat{t_i}(\theta) = \begin{cases}
    \theta_i,\quad &\theta_i = max(\theta), \theta_1 \neq \theta_2  \\\\
    \frac{1}{2}\theta_i,\quad &\theta_1 = \theta_2  \\\\
    0,\quad &otherwise
    \end{cases}
    $$
* $(q,t)$:
  * $$
    q_i(\theta) = \begin{cases}
    1,\quad &\theta_i = max(\theta), \theta_1 \neq \theta_2  \\\\
    \frac{1}{2},\quad &\theta_1 = \theta_2  \\\\
    0,\quad &otherwise
    \end{cases}
    $$
  * $$
    t_i(\theta) = \begin{cases}
    \theta_i + \nu_i(\theta),\quad &\theta_i = max(\theta), \theta_1 \neq \theta_2  \\\\
    \frac{1}{2}\theta_i + \nu_i(\theta),\quad &\theta_1 = \theta_2  \\\\
    \nu_i(\theta),\quad &otherwise
    \end{cases}
    $$
  * $q(10,10)=q(100,100)=1/2,q(10,100)=(0,1),q(100,10)=(1,0)$,\
    $t(10,10)=(35,35),t(100,100)=(80,80),t(10,100)=(-60,40),t(100,10)=(40,-60)$
  * $U_{max} = 70$.