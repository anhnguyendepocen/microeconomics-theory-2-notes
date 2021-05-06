## Topic 8: Bayesian Mechanism Design
### Allocation rule under quasilinearity with BNE
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

---
**Revelation Principle** (for BNE)

If $g$ is the outcome function of an arbitrary mechanism $\Gamma$ and a BNE $\sigma^*$ of it, then direct mechanism $D(g)$ is truth-compatible in BNE. 

*Proof:*


  
*Remark:*
* To implement $g$ in BNE, WLOG can focus on direct mechanisms.
* No need to worry about sequential rationality.
* If $g$ is implementable in dominant strategies, it is implementable
in BNE.
  
---