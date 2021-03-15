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