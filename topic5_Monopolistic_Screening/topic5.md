## Topic 5: Monopolistic Screening
### 5.A Car Market
* Buyer's type $v$: valuation for the car, private information.
* Payment: $P(v)$.
* Buyer's utility: $v-P$.
* Seller's utility: $P$.
* Outside option: no dealing results in utilities all equal to 0.

**Seller's Strategy:**
* Selling mechanism: $\Gamma$, which is a set of infinite elements.
* Equilibrium: $\sigma^*(\Gamma)$.
  * Outcome of $\sigma$: $(x,p)$.
  * $x$: $[0,V] \to [0,1]$, probability of trading happens given the buyer's type $v$.
  * $p$: $[0,V] \to \mathbb{R}$, expected payment seller will receive given the buyer's type $v$.
* Seller's problem: $max_{\Gamma \in \mathcal{G}} \pi^*(\Gamma)$, where $\mathcal{G}$ is the set of all selling methods/games, $\pi$ is the payoff to seller.
* Outcome of the best equilibrium to seller for the given $\Gamma$: $(x^{\Gamma},p^{\Gamma})$.
* Payoff under best outcome: $\pi^*(\Gamma)=E[p^{\Gamma}(v)]$.
* Although the payoff is maximized to seller, under the equilibrium, buyer will response to his best. This is a coordination.

### 5.B Direct Mechanism
* A direct mechanism has a flexible contract/menu.
* The contract specifies two functions:
  * $x$: $[0,V] \to [0,1]$ "allocation rule"
  * $p$: $[0,V] \to \mathbb{R}$ "payment rule"
  * Denote $\Gamma = D(x,p)$.
* Mechanism:
  * Buyer decides to accept or reject the contract.
  * Buyer reports his type $v$ if he accepts.
  * Buyer gets the car with prob $x(v)$.
  * If buyer gets the car, buyer pays $p(v)$ to seller.
* Equilibrium (BNE - Bayes Nash Equilibrium):
  * Consider contract that are always accepted, $D(x,p)$ becomes a simple one-shot game.
  * Condition 1 (**no deviation**): for buyer with $v$, EQ maximizes his expected payoff under $v$.
  * Condition 2 (**acceptance**): for buyer with $v$, EQ payoff is no less than 0 (outside option).
* A special BNE: **Truth-telling**
  * $\sigma(v)=v$: buyer reveals his true type.
  * It is NOT always a BNE.
  * If it is, call $D(x,p)$ is **truth compatible**.
  
### 5.C Arbitrary Mechanism
---
**Revelation Principle**

If $(x,p)$ is the outcome of an arbitrary mechanism $\Gamma \in \mathcal{G}$ and an arbitrary equilibrium 
of $\Gamma$, then direct mechanism $D(x,p)$ is truth-compatible.

---
*Proof*:
* Outcome $(x,p)$ from any arbitrary mechanism can be used in contract as direct mechanism outcome $D(x,p)$.
* Suppose buyer's EQ outcome is $(x,p)$ and his type is $v$, then his expected payoff is 
$x(v)v-p(v)$. The equilibrium indicates buyer has no incentive to deviate to reporting a faked type $v'$. Hence, $D(x,p)$ is truth-compatible.

---
**Direct mechanism are WLOG.**
$$
max_{\Gamma \in \mathcal{G}} E[p^{\Gamma}(v)] =
max_{p \in \mathcal{P}} E[p(v)] 
$$
, where $\mathcal{P}$ is the set of all payment rules used in a truth-compatible direct mechanism.

---
*Proof:*
* $LHS \geq RHS$: Since truth-telling is always an option, the other EQ should be no less than truth-telling EQ.
* $RHS \geq LHS$: Suppose $(x,p)$ is the outcome for $LHS$, by **Revelation Principle**, $D(x,p)$ is truth-compatible. Hence, $p$ is also an option, such that $RHS \geq E[p] = LHS$.
  
### 5.D Optimal Direct Mechanism
From 5.C, it is known that solving the optimal direct mechanism(s) is enough.
The seller's problem now 
$$max_{p \in \mathcal{P}}E[p(v)]$$
, where
* $\mathcal{P} = \{p: \text{D(x,p) is true-compatible for some }x:[0,v]\to[0,1]\}$
* IC: $x(v)v-p(v) \geq x(v')v-p(v'),\forall v' \in [0,V]$
* IR: $x(v)v-p(v) \geq 0$

---
**Obs. 1: If $D(x,p)$ is truth-compatible, then $x(v)$ is non-decreasing.**

Higher types have better chance of getting the car.

*Proof:*
* IC implies truth-revealing is always an optimal strategy. Then for $v > v'$,
  $$x(v)v-p(v) \geq x(v')v-p(v')$$
  $$x(v')v'-p(v') \geq x(v)v'-p(v)$$
* Rearranging yields $x(v) \geq x(v')$.
---

---
**Obs. 2: If $D(x,p)$ is truth-compatible, then $U(v)$ is differentiable for any $v$ where $x$ is continuous, and $U'(v)=x(v)$.**

Marginal utility equals to probability of trading.

*Proof:*
* For any $v > v'$,
  $$U(v) \geq x(v')v-p(v') = x(v')v-x(v')v'+x(v')v'-p(v') \\
  = x(v')(v-v')+U(v')$$
  $$\Rightarrow \frac{U(v)-U(v')}{v-v'} \geq x(v)$$
  Similarly, 
  $$\frac{U(v)-U(v')}{v-v'} \leq x(v')$$
* Since $x$ is continuous, $x(v') \to x(v)$ as $v' \to v$.
* $$U'(v)=lim_{v' \to v}\frac{U(v)-U(v')}{v-v'}=x(v)$$

---

---
**Obs. 3: [Payoff equivalence for buyer] If $D(x,p)$ is truth-compatible, then**
$$U(v) = U(0)+\int_0^v x(t) dt$$

If two different mechanisms have the same allocation rule $x$ and charges the type 0 buyer the same amount $p(0)$, then buyer is indifferent between them regardless of their type.

*Proof:*
* $x$ is monotone, meaning it is almost every continuous.
* Hence, $U$ is almost everywhere differentiable.

---

---
**Obs. 4: [Payoff/revenue equivalence for seller] If $D(x,p)$ is truth-compatible, then**
$$p(v) = p(0)+x(v)v-\int_0^v x(t) dt$$

Payment rule is determined by $x$ and type 0's payment. \
Same allocation rule and payment for type 0 implies same payment rule. \
Seller's payoff depends only on $x$ and type 0's payment.

*Proof:*
* Obvious from **Obs. 3**.

---

---
**Obs. 5: IR is satisfied if and only if $U(0) \geq 0$.**

Buyer of any type is willing to accept contract as long as type 0 buyer is willing to accept.

*Proof:*
* $U(v) \geq U(0)$ since $x \geq 0$. Thus $U(0) \geq 0$ implies $U(v) \geq 0$, which means IR is satisfied for all types.

---

---
**Lemma. $D(x,p)$ is truth-compatible if and only if**
1. **$x$ is non-decreasing**
2. **$p(v) = \underline{p}+x(v)v-\int_0^v x(t) dt$ for some $\underline{p} \leq 0$.**

The entire contract is determined by any non-decreasing allocation rule $x$ and non-positive bottom payment $\underline{p} (=-U(0))$.

*Proof:*
* Sufficiency from **Obs. 1-5**
* Necessity: suppose $D(x,p)$ is not truth-compatible, which means buyer will make profitable deviation to reveal a false type $v'$ if his true type is $v$.
  $$x(v')v - p(v') \geq x(v)v - p(v)$$
  $$x(v')v - x(v')v' + x(v')v' - p(v') \geq x(v)v - p(v)$$
  $$x(v')(v-v') + \int_0^{v'}x(t)dt \geq \int_0^{v}x(t)dt$$
  $$x(v')(v-v') \geq - \int_0^{v'}x(t)dt + \int_0^{v}x(t)dt \geq (v-v')x(v')$$
  The "=" holds when $x(v)=x(v')$ for some $v \neq v'$.
  Hence, the buyer has no inventive to deviate, since deviation yields no better payoff.

---

---
**Obs. 6: If $(x,\underline{p})$ solves the above optimization problem then $\underline{p}=0$.** 

*Proof:*
* $\underline{p} \geq p(v)$ for any $v$ implies $\underline{p}=0$.

---

---
**Obs. 7: $\mathcal{M}$ is convex and compact in the metric space induced by $L^1$ norm.**

The optimization is simplified to 
$$max_{x \in \mathcal{M}}E[x(v)v-\int_0^vx(t)dt]$$
, where $\mathcal{M}$ is the set of all non-decreasing functions from $[0,V]$ tp $[0,1]$.

*Proof:*
* Convexity: from linearity.
* Compactness: from "closed" and "bounded".

---

---
**Obs. 8: Seller's payoff is continuous and linear in $x$.**

Seller's payoff is maximized at the extreme points of $\mathcal{M}$. \
Extreme points of $\mathcal{M}$ is known to be one-step functions.

---

---
**Lemma. If $x$ is a one-step function, $x(v)v-\int_0^vx(t)dt$ is also a one-step function.**

It implies $E[\cdot] = P(1-F(P))$, where $P$ is the step height.

---

---
**Optimal Selling Mechanism: a direct mechanism $D(x,p)$ is an optimal selling mechanism, where**
$$
x^*(v) = \begin{cases} 
0,\quad &v < P^* \\\\
1,\quad &v \geq P^*
\end{cases}
$$

$$
p^*(v) = \begin{cases} 
0,\quad &v < P^* \\\\
P^*,\quad &v \geq P^*
\end{cases}
$$
$$P^* = argmax_{P \in [0,V]} P(1-F(P)), F = F(v)$$

Seller can either put a price tag $P^*$ on the car or offer $P^*$ without any bargaining possibility.

---

### 5.E Questions
A monopolist(principle) in the market produces a good of variable quality $q \geq 0$ at cost $C(q)$ per unit of good. The consumer (agent) wants to buy one unit of the good. The consumer has different tastes over the product, characterized by $\theta$. If Agent buys quality $q$ at price $p$, his utility is $u(q,p;\theta) = \theta q -p$, and the profit for the monopolist: $\pi = p - C(q)$. The consumer's reservation utility is $U_R = 0$. The consumer knows his taste $\theta$; The monopolist has prior beliefs $\theta \in \{\theta_L,\theta_H\}$ with $\theta_L < \theta_H$ and $Pr(\theta=\theta_H) = p$. You can assume that the outside option of not buying yields zero utility.

**Q1.** If $\theta$ is observed by the monopolist, characterize the monopolist's optimal pricing scheme.

*Sol:* 
For the given $\theta$, the problem is 
$$max_{q,p} \{p - C(q)\}, s.t. \ U_{\theta}=\theta q - p \geq 0$$
, can be reduced to 
$$max_{q} \{\theta q -C(q)\}, s.t. \ q \geq 0$$
, which gives $C'(q^0) = \theta$, $p^0 = q^0\theta$. Price extracts all surplus from consumer (perfect price discrimination).

**Q2.** Under incomplete information, characterize the monopolist's optimal pricing scheme.

*Sol:* 
For $\theta$ not given , the problem is 
$$max_{p_H,p_L} E[p - C(q)]
, \text{s.t. IC, IR}$$
, can be reduced to 
$$max_{p_H,p_L} \  p[p_H - C(q_H)] + (1 - p)[p_L - C(q_L)] \\
s.t. \ U_{\theta_{H}}=\theta_H q_H - p_H \geq 0 \ (1)\\
\ \ \ \ \ \  U_{\theta_{L}}=\theta_L q_L - p_L \geq 0 \ (2)\\
\ \ \ \ \ \  \theta_H q_H - p_H \geq \theta_H q_L - p_L \ (3)\\
\ \ \ \ \ \  \theta_L q_L - p_L \geq \theta_L q_H - p_H \ (4)$$
(3) and (4) gives $q_H \geq q_L$. (1) is non-binding and can be excluded by (3). (2) is binding, $p_L = \theta_L q_L$. (4) is non-binding, since $0 \geq \theta_L q_H - p_H$ gives no upper bound on $p_H$. (3) binds necessarily: otherwise we can increase $p_H$ as much as possible while still maintaining the other constraints.

Denote high value customer's surplus as $R_H = \theta_H q_H - p_H = \theta_H q_L - p_L = q_L(\theta_H - \theta_L)$.The problem can be further reduced to 
$$max_{p_H,p_L} \  p[\theta_H q_H - C(q_H) -R_H] + (1 - p)[\theta_L q_L - C(q_L)] \\
s.t. \ q_L \leq q_H$$
, which by FOC gives $C'(q^*_H) = \theta_H$, then $q^*_H = q^0_H$; and $C'(q^*_L) = \theta_L - (\theta_H - \theta_L)\frac{p}{1-p}$. $C'(q^*_L) \leq \theta_L$ gives $0 \leq q^*_L < q^0_L$, or $q^*_L = q^0_L = 0$.


**Q3.** Compare the two pricing schemes in Question 1 and Question 2.

*Sol:* It is obvious that, under incomplete information, if a pricing scheme described in Question 1 is used, the high-taste consumer will for sure want to deviate.
That's why in Question 2, we need to offer the high-taste consumer positive surplus $R_H$. $R_H$ is called **Informational Rent**, the rent necessary to pay to obtain information revelation about $H$. In this case, we have efficient high quality for high-taste consumer (no distortion at the top): $q^*_H = q^0_H$ but inefficiency at the bottom. Low quantity is sub-optimal for low-taste consumer: $q^*_L < q^0_L$.
