## Topic 7: Intro to Mech Design and Dominant Strategy Mech
### 7.A Collective Choice Problem
**(a) Collective choice given preference profile:**
* $N = \{1,...,n\}$: A group of people.
* $X$: Collective alternatives.
* $P = (\succ_1,...,\succ_n)$: Preference profile.
* $\mathcal{D}$: Preference domain, where $P \in \mathcal{D}$.
* A group choice function/generator $g: \mathcal{D} \to X$.
  * Takes in $P$ and produce $g(P)$.
  * Needs to specify $P$.
  
**(b) Collective choice given actions:**
* $N = \{1,...,n\}$: A group of people.
* $\Sigma_i$: A set of available actions for player $i$.
* $\sigma = (\sigma_1,...,\sigma_n)$: action profile.
* $d(\sigma)$: a decision rule. 
* Game:
  * Period 1: Player $i$ finds his preference $\succ_i$.
  * Period 2: Player $i$ follows his EQ strategy $\sigma_i^*(\succ_i)$,
    and so preference profile 
    $\sigma^*(P) = (\sigma_1^*(\succ_1),...,\sigma_n^*(\succ_n))$.
  * Period 3: Group choice is made to be $d(\sigma^*(P))$. 
* Outcome function: 
  $$g^{\Gamma, \sigma^*} := d \circ \sigma^*$$
  * Condition on each player plays EQ strategy $\sigma_i^*$.
  * Gives group choice for any $P$.
  * For $g$ with the same outcome as the $g^{\Gamma, \sigma^*}$,
    we say $\Gamma$ implements $g$ in EQ $\sigma^*$.

### 7.B $\Gamma$ under Dominant Strategies EQ
Consider only dominant strategies equilibrium, where
every player $i$ plays an optimal $\sigma_i^*$ **regardless of** others' strategies.

**Question.** Does there exist $(\Gamma, \sigma^*)$ such that
1. $\sigma^*$ is a dominant strategies equilibrium of $\Gamma$.
2. $g^{\Gamma,\sigma^*} = g$.

Consider only direct mechanism $\Gamma = D(g)$. $D(g)$ is **truth-compatible in dominant strategies** if everyone reporting truthfully is a dominant strategy equilibrium of the mechanism.

Examples:
* "Dictatorship": It is. Since everyone has no incentive to report fake preference.
* "Borda count": It is NOT. Since players may report fake preference for a better result.

---
**Revelation Principle** (for dominant strategies)

If $g$ is the outcome function of an arbitrary mechanism $\Gamma$ and a dominant strategy equilibrium of it, then direct mechanism $D(g)$ is truth-compatible in dominant strategies.  

*Proof:*
* Suppose $g$ is the outcome of $\Gamma$ and a dominant strategy EQ $\sigma^*$ of it.
* Suppose the contrary $D(g)$ is not truth-compatible. Then for some players, they can pretend their preference for profitable deviation. Suppose for player $i$, he can pretend his true preference $\succ_i$ to be $\succ_i'$, such that his outcome
$$g(\succ_i',P_{-i}) \succ_i g(\succ_i,P_{-i})$$
, where $P_{-i}$ is others' preferences, staying unchanged.
* $g$ is the outcome function of $\Sigma$, which implies 
$$d(\sigma^*(\succ_i',P_{-i})) \succ d(\sigma^*(\succ_i,P_{-i}))$$
, which contrasts the equilibrium condition.

---