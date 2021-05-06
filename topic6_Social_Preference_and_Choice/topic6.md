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
**Arrow's Impossibility Theorem:** If $|X| > 2$, then there does not exist $f$ that satisfies all of the following:
1. Completeness
2. Transitivity
3. Pareto
4. Non-dictatorship
5. IIA

*Proof:* Suppose there is a $f$ for $|X| > 2$, and it satisfies features 1-5. Proof follows following 4 observations. Obs.3 and Obs.4 imply that there is an agent $j$, whose preference is exactly the group's preference. It means such $j$ is a dictator, which contrasts the feature 4 (Non-dictatorship).

---


---
**Obs.1:** If under preference profile $P$, any alternative $x \in X$ is either ranked at the top or at the bottom by everyone in the group, then the group preference $f(P)$ ranks $x$ either at the top or at the bottom.

*Proof:*
* Suppose not, then there are $y,z \in X$, such that $y \succ^* x \succ^* z$, where $\succ^* = f(P)$.
* Now in $P$, for anyone who has $z$ below $y$, swap $y$ and $z$, such that $z$ is always above $y$. Denote this new profile as $P'$, and $\succ^\# = f(P')$. Note that $x$ will not change its position since it is at either top or bottom.
* Now for pairs $(x,y)$ and $(x,z)$, by IIA, we will have $y \succ_\# x$ and $x \succ_\# z$, and so $y \succ_\# z$ by transitivity. However, it contrasts Pareto.


---

---
**Obs.2:** For every alternative $x$, there exist two preference profiles $P_I$ , $P_{II}$ and one guy $j$, such that $P_I$ and $P_{II}$ differ only in $j$’s preference, and moreover $x$ is at the bottom under $f(P_I)$, whereas it is at the top under $f(P_{II})$.

*Proof:*
* Let $P$ be the profile where all people have $x$ at the bottom. By Pareto, $f(P)$ will have $x$ at the bottom.
* Move $x$ to the top from $i=1$, and stop until the moving for $i=j$ makes $f(P')$ have $x$ at the top. Denote the new profile as $P_{II}$ and the profile one-step before as $P_{I}$
* By **Obs.1**, such $P_{II}$ is gauranted to exist, since $x$ will be either at the bottom or the top and when $i=n$, $x$ is certainly at the top.
* Guy $j$ can single-handedly change $x$ from socially worst to socially best.

---

---
**Obs.3:** Given $x$ in **Obs.2**, fix any preference profile $(\succ_1,...,\succ_N )$ and let
$\succ^* = f(\succ_1,...,\succ_N)$. For any two alternatives $y \neq x$ and $z \neq x$,
$y \succ^* z$ if and only if $y \succ_j z$.

*Proof:*
* Consider a $P_{III}$:
  1. Everyone before j has $x$ on the top, and everyone after has $x$ on the bottom.
  2. $j$ has $y$ above $x$ and $x$ above $z$. 
* Now for the pair $(x,y)$, everyone has the same preference under $P_{III}$ as under $P_{I}$. Hence, $y$ is above $x$. Similarly, $x$ is above $z$ since everyone has the same preference under $P_{II}$ and $P_{III}$. Hence, by $f(P_{III})$, $y \succ z$ is solely due to $y \succ_j z$.
* For any fix preference profile $P$, we can always let $P_{III}$ copy everyone but $j$'s preference on $y$ and $z$, so then $y \succ^* z$ will solely depend on whether $y \succ_j z$.

---

---
**Obs.4:** Fix any preference profile $(\succ_1,...,\succ_N )$ and let
$\succ^* = f(\succ_1,...,\succ_N )$. For any alternative $y \neq x$, $y \succ^* x$ if and only if $y \succ_j x$.

*Proof:*
* Under $P_I$, group preference on $(x,y)$ will solely depend on $j$'s preference.
* Let $P_{I}'$ copy everyone but $j$'s preference from any fix $P$. Let $i$ be in front of $j$ if $y$ is preferred in $P$, and be after $j$ if otherwise. The $P_{I}'$ is exactly same as $P_{I}$, where group preference on pair $(x,y)$ will sole depend on $j$'s choice.

---

### 6.E Group choice instead of group alternative
* Arrow's Impossibility Theorem indicates a group cannot come up with a group preference $\succ_* \in \mathcal{Q}$ in a systematic way.
* Make group choice $g:\mathcal{D} \to X$ instead of make complete ranking is easier.

---
**Example 1: (Dictatorship) $g(\succ_1,...\succ_n) = \succ_1$**

* There is some guy $i$ such that for any $(\succ_1,...,\succ_n)$, $g(\succ_1,...,\succ_n)$ is $i$’s top choice under $\succ_i$.

---

---
**Example 2: (Borda count with tie-breaking index) Index the alternatives as $x^1,...,x^{|X|}$, such that $g(\succ_1,...,\succ_n)$ has the highest Borda score. In case of a tie, $g(\succ_1,...,\succ_n)$ is the alternative with the lowest index among those with the highest score.**

---

### 6.F Features of Gourp Choice
1. **Pareto:** If $x \succ_i y$ for every $i=1,...,n$, then $f(\succ_1,...,\succ_n) \neq y$. 
2. **Non-dictatorship:** $g$ is not a dictatorship.
3. **Monotonicity:** Given two preference profiles $(\succ_1,...,\succ_n)$ and $(\succ_1',...,\succ_n')$, if $x = g(\succ_1,...,\succ_n)$ and moreover for every $i$, the set of alternatives worse than $x$ weakly expands under $\succ_i'$, then $g(\succ_1',...,\succ_n') = x$.
   * Example: $X=\{a,b,c\}$
    $$P:\{a \succ_1 b \succ_1 c, b \succ_1 c \succ_1 a\}$$
    $$P':\{b \succ_2' a \succ_2' c, c \succ_2' b \succ_2' a\}$$
    Then if $g(P)=c$, $g(P')=c$ since $c$ is more desirable in $P'$ than in $P$.

---
**Muller-Satterthwaite Impossibility Theorem.** If $|X| > 2$ then there does not exist a group choice function $g$ that satisfies all of the
following:
1. Pareto
2. Non-dictatorship
3. Monotonicity

*Proof:*
Similar to **Obs.3** and **Obs.4**, a $g$ satisfying Pareto and Monotonicity will be a dictatorship, which is a contrast.

---