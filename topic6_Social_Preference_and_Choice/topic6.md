## Topic 6: Social Preference and Choice
### 6.A Individual Preference and Social Choice
* Individual preference:
  * $X$: set of alternatives.
  * Preference is a binary relation on $X$
    ($x \succ y$ or $x \prec y$ or $x \sim y$ or $x ? y$).
  * Preference is rational when it is complete and transitive.
  * Alternatives can be completely ranked if preference is rational.

* Group choice:
  * A group of people $N = \{1,...,n\}$ makes a single choice.
  * For $i \in N$, each has a rational preference $\succ_i$ over $X$. $P = \{\succ_i\}_{i \in N}$ is the **preference profile**.
  * $(N,X,P)$ is a **collective choice environment**. 
  * Preference set:
    * $\mathcal{Q}$: the set of strict preferences $\succ$ over $X$.
    * $\mathcal{R}$: the set of rational strict preferences over $X$, hence $\mathcal{R} \subset \mathcal{Q}_X$.
    * $\mathcal{D}=\mathcal{R}^n$: **preference domain**, which includes all rational strict preference profiles over $X$.
  * A good preference generator $f$, $f: \mathcal{D} \to \mathcal{Q}$.
    * For a person in group with preference $P$, $\succ^* = f(P)$ is the preference of the group.
    * Only consider strict group preference ($\succ^*$) for now.

### 6.B "Dictatorship" and "Majority"
---
**Example 1: (Dictatorship) $f(\succ_1,...\succ_n) = \succ_1$**

* Group preference is always the same as the dictator's (agent 1's).

---

---
**Example 2: (Majority) $\succ^* := f(\succ_1,...\succ_n)$ satisfies $x \succ^* y$ when the number of people preferring $x$ to $y$ is more than the number of people preferring $y$ to $x$.**

* $\succ^*$ may not be transitive.
* $\succ^*$ may form a "Candorcet cycle" ($x \succ y \succ z \succ x$).

---

### 6.C Features of group preference
* **Completeness:** $f(P)$ is a complete relation for any $P \in \mathcal{D}$.
  * "Dictatorship" satisfies.
  * "Majority" satisfies when $n$ is odd.
* **Transitivity:** $f(P)$ is a transitive relation for any $P \in \mathcal{D}$.
  * "Dictatorship" satisfies.
  * "Majority" satisfies when $n \leq 2$.
* **Pareto:** If $x \succ_i y$ for every $i=1,...,n$, then $x \succ^* y$ where $\succ^* = f(\succ_1,...,\succ_n)$.
  * Both satisfy.
  * If the preference is not Pareto, there is some room for pareto efficiency improvement. All are willing to deviate to their preferred choice.
* **Democracy:** If $P'$ is a permutation of $P$ then $f(P)=f(O')$
  * Everyone is treated equally: "symmetry" or "anonymity".
  * "Majority" satisfies while "dictatorship" does not.
  * **Non-dictatorship:** There is no such $i \in N$ such that $f(\succ_1,...,\succ_n)=\succ_i$ for every $(\succ_1,...,\succ_n) \in \mathcal{D}$. **Democracy implies non-dictatorship, but not vice versa.**
* **Independence of Irrelevant Alternatives (IIA):** Given two preference profiles $(\succ_1,...,\succ_n)$ and $(\succ_1',...,\succ_n')$, if $x \succ_i y \Leftrightarrow x \succ_i' y$ for everyone $i \in N$, then $x \succ^* y \Leftrightarrow x \succ^\# y$ where $\succ^* = f(\succ_1,...\succ_n)$ and $\succ^\# = f(\succ_1',...\succ_n')$.
  * When a pair $(x,y)$ has the same priority across different preference profiles, they are irrelavant to group choice strategy, since they maintain the same priority in the group preference.
  
$f$, which satisfies all 5 (non-dictatorship, or better democracy) properties, is a nice preference generator. "Dictatorship" satisfies all but 4. "Majority" satisfies all but 2 when $n$ is odd; satisfies all when $|X|=2$.

### 6.D Arrow's Impossibility Theorem
---



---