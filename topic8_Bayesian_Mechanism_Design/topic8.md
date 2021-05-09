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

*Proof:*


  
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