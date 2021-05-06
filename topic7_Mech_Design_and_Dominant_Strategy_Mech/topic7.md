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
* Preferences is not necessary. Focus on mechanism: A mechanism $\Gamma$ is technically a game via which collective decision is reached.
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
  * Want to find a mechanism that implements a good $g$: find a $(\Gamma,\sigma^*)$ such that $g^{\Gamma, \sigma^*} = g$.

### 7.B $\Gamma$ under Dominant Strategies EQ
Consider only dominant strategies equilibrium, where
every player $i$ plays an optimal $\sigma_i^*$ **regardless of** others' strategies: everyone will "no-brainer" to play the dominant strategy — no need to "know about" others’ strategies.

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

*Examples:*
* "Dictatorship": $D(g)$ is truth-compatible in dominant strategies.
* "Borda count": $D(g)$ is not truth-compatible in dominant strategies
  
*Remark:*
* If a group choice function can be implemented using a mechanism, it can be implemented using a direct mechanism: $\Gamma \to (\sigma^* EQ) \to g$, then exists $D(g) \to g$. $D(g)$ is the $\Gamma$ using on the contract.
  
---

**Question.** Now we find $\Gamma = D(g)$, such that $g^{\Gamma,\sigma^*} = g$. Then, is the direct mechanism $D(g)$ truth-compatible in dominant strategies?

---
**Gibbard-Satterthwaite Impossibility Theorem.** When $|X| > 3$, if $g$ satisfies non-dictatorship and Pareto, then D(g) is not truth-compatible in dominant strategies.

*Proof:*
* WTS: If $D(g)$ is truth-compatible in dominant strategies, then $g$ satisfies monotonicity. By [Muller-Satterthwaite Impossibility Theorem], there is no $g$ satisfying non-dictatorship, Pareto and monotonicity.
* Fix $g$, such that $D(g)$ is truth-compatible in dominant strategies. Suppose there are 2 preference profiles: $P = (\succ_i, \succ_{-i})$ and $P' = (\succ'_i, \succ_{-i})$ that differ only in $i$’s preference. 
* Given $g(P') = a$ and the set of alternatives worse than $a$ does not shrink if $i$’s preference changes from $\succ'_i$ to $\succ_i$. WTS: $g(P) = a$. If $g(P) = b \neq a$, then $b \succ_i a$ in $P$. Then $i$ will report $\succ'_{-i}$ in $P$ to get $a$, which is a contradiction. Hence, $g(P) = g(P') = a$ if $a$ over $b$ is reserved across $P$ and $P'$.
* For any 2 different $P$ and $P'$, we can construct intermediate many $P_i$s to get the result: truth-compatibility implies monotonicity.


*Remark:*
* Gibbard-Satterthwaite (GS): No $g$ is simultaneously 1. Pareto, 2. non-dictatorship, 3. implementable in dominant strategies...... on one condition: **individuals can have any preference**.
  * Example: In reality, people always prefer to pay less than more.
---

### 7.C Collective choice with money
* Collective choice with money - quasilinear or transferable utility environment:
  $$X = (q,t_1,...,t_n) \in A \times \mathbb{R}^n$$
  * $q$: allocation, the non-monetary part of the choice.
  * $t_i$: $i$ player's transfer.
  * Example: $q$ - public goods; $t_i$ - everyone's fund.
* Auction - allocation of a single object
  * $q = (q_1,...,q_n)$: probability vector for people getting the object.
  * $t_i$: how everyone pays.
  * Example: $X = ((q_1,q_{-1}=0),(t_1=10,t_{-1}=0))$, some one pays all and gets all.
  * Example: $X = ((q_i=1/n),(t_i=10/n))$, some one wins all by chance, and he pays all/or everyone pays the same.
* **Quasilinear preference.** Preference $\succeq_i$ is quasilinear if for any $x = (q,t_1,...,t_n)$ and $x' = (q,t'_1,...,t'_n)$: $x \succeq_i x'$ iff $t_i \leq t'_i$.
  * Monetary quantity $t_i$ can represent people's preference.
* **Proposition.** If player $i$’s preference $\succeq _i$ is quasilinear, then it
is represented by a utility function for some function $v_i^{\succeq _i}: A \to \mathbb{R}$, $u_i^{\succeq _i}(q,t_1,...,t_n) = v_i^{\succeq _i}(q) - t_i$.
   * $u_i^{\succeq _i}$ is "additively separable".
   * $v_i^{\succeq _i}(q)$: valuation function associated with $\succeq _i$, $i$'s (monetary) valuation of allocation $q$.
   * $t_i$ : how much $i$ pays or receives.
   * $v_i$ is not a utility function, in a sense that it only reflects the value of allocations in monetary terms.
* Type of the player:
  * Define $\Theta = \{v_i: A \to \mathbb{R}\}$, then write $v_i = v_i(q,\theta_i)$, $\theta_i$ is $i$'s private information/type.
  * $\theta_i \to v_i \to u_i \to \succeq_i$, type = preference.
* Group choice function: $g(\theta_1,...\theta_n) = (q(\theta_1,...\theta_n), t_1(\theta_1,...\theta_n),..., t_n(\theta_1,...\theta_n))$
  * Efficient allocation rule: 
    * $q:\Theta^n \to A$ is efficient if for every $\theta \in \Theta$, $q(\theta) \in argmax_{a \in A} \sum v_i(a,\theta_i)$.
    * $q$ chooses utilitarian allocation — maximizer of the **sum of valuations** across players.
    * **Proposition.** $q:\Theta^n \to A$ is efficient if and only if for any group choice function $g' = (q', t'_1,..., t'_n)$, there are transfer functions $(t_1,...,t_n)$ such that $g = (q, t_1,..., t_n)$ gives every player a weakly higher payoff for any type profile.
    * **Proposition.** [Vickery-Clarke-Groves]. If allocation rule $q$ is efficient, then group choice function $g = (q, t_1, ..., t_n)$ where $t_i(\theta) = -\sum_{j \neq i} v_j(q(\theta),\theta_j) + \tau_i(\theta_{-i})$ for any arbitrary $\tau_i: \Theta_i \to \mathbb{R}$ is implementable in dominant strategies.
      * Such $D(g)$ is truth-compatible in dominant strategies.
      * Called **VCG mechanism**. VCG work because transfer rules are designed so that maximizing individual payoff is **aligned with** maximizing utilitarian welfare $\sum_j v_j$.
  
### 7.D Second-price auction
* Allocating one painting to one of $n$ people.
  * $v_i(q_i,\theta_i) = q_i \theta_i$
  * $u_i = v_i - t_i = q_i \theta_i - t_i$
* Second-price auction with no ties:
  * $q_i(\theta) = 1$ for $\theta_i = \max \theta$, $q_i(\theta) = 0$ for others.
  * $t_i(\theta) = \max_i \theta_{-i}$ for $\theta_i = \max \theta$, $q_i(\theta) = 0$ for others.
* VCG:
  * $q$ is efficient.
  * $\tau_i(\theta_{-i}) =\max_i \theta_{-i}$ resulting a transfer rule.
* Budget balance issue.
  * $\sum_i t_i(\theta) = 0, \forall \theta$ is not possible under VCG.
  * In the case  $\Theta = \{v: A \to \mathbb{R}\}$ (all quasilinear preferences)
    * Any mechanism implementing efficient allocation in dominant strategies must be VCG (Green and Laffont).
    * No VCG mechanism satisfies uniform budget balance (Green and Laffont).

### 7.E Questions
A special case of a VCG mechanism is known as the Clarke, or pivotal mechanism. This
mechanism corresponds to the case in which
$$\tau_i(\theta_{-i}) = \sum_{j \neq i} v_j(q^*_{-i}(\theta_{-i}), \theta_j)$$
, where fore all $\theta_{-i} \in \Theta_{-i}$, $q^*_{-i}(\theta_{-i})$ satisfies
$$\sum_{j \neq i}v_j(q^*_{-i}(\theta_{-i}), \theta_j) \geq \sum_{j \neq i}v_j(q, \theta_j), \text{for all } q \in Q$$
That is, $q^*_{-i}$ is the allocation rule that would be eefficient if there were only the $I - 1$ agents $j \neq i$.

Suppose that the Clarke's pivotal mechanism is applied to allocate two objects $\mathcal{O} = \{a,b\}$ to three buyers. A buyer can buy none, one, or both of the objects. Each buyer is asked to report his valuation function. For simplicity, assume
the valuation function of each buyer depends only on the set of objects assigned to that buyer. The values are:
$$
v_1(\emptyset) = 0, \quad v_1(\{a\}) = 10, \quad v_1(\{b\}) = 3, \quad v_1(\{a,b\}) = 13 \\
v_2(\emptyset) = 0, \quad v_2(\{a\}) = 2, \quad v_2(\{b\}) = 8, \quad v_2(\{a,b\}) = 10 \\
v_3(\emptyset) = 0, \quad v_3(\{a\}) = 3, \quad v_3(\{b\}) = 2, \quad v_3(\{a,b\}) = 14 
$$
Determine the assignment of objects to buyers and the payments of the buyers.

*Sol:*
* $a_1 = \{\{a,b\}, \emptyset, \emptyset\}$,...
* $q = a_2 = \{\{a\}, \{b\}, \emptyset\}$, yielding maximum $\sum_i v_i = 18$, $v_1 = 10, v_2 = 8, v_3 = 0$.
* $\tau_1 = 14$, $\tau_2 = 14$, $\tau_3 = 18$.
* $t_1 = -8 + 14 = 6$, $t_2 = -10 + 14 = 4$, $t_3 = -18 + 18 = 0$.