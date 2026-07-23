# Phase 1 — Math Foundations — Notes

Concept + formula + results per completed topic. Code lives in `phase1-math/*.py` (committed separately) — not duplicated here. Dated narrative history lives in `progress-log.md`.

---

# Section 1.1 — Algebra

## 1.1.1 — Variables, Expressions, Solving for x

**Concept:** A variable is an unknown placeholder. Solving an equation means finding the value that balances both sides — whatever operation is applied to one side must be applied to the other.

**Formula:** No general formula — technique is isolate-the-variable via inverse operations (subtract, then divide).

**Worked example:** `2x + 3 = 11` → `2x = 8` → `x = 4`. Verified by substitution.

**Practice results:** 3 problems solved correctly (x=7, x=28, x=5).

**Gotcha:** divisibility of the constant term by the multiplier predicts whether the answer is a whole number or fraction, before solving.

**End-goal link:** every ML model is an equation with unknowns (weights). Training = solving for those unknowns at scale via gradient descent instead of algebra.

---

## 1.1.2 — Functions: f(x), Domain, Range

**Concept:** A function maps each input to exactly one output. Domain = valid inputs; range = possible outputs.

**Formula:** `f(x) = 2x + 3` (example); domain restriction example: `g(x) = 1/x`, domain = all reals except 0.

**Worked example:** `f(4)=11, f(0)=3, f(-1)=1`. `h(x)=x²-4`: roots at x=±2 (where h(x)=0).

**Practice results:** Correctly predicted `g(0)` raises `ZeroDivisionError` (Python, unlike JS's silent `Infinity`). Correctly computed h(2)=0, h(-2)=0, h(0)=-4, correctly identified both roots.

**Gotcha:** JS `1/0 === Infinity` (silent) vs Python `ZeroDivisionError` (loud) — real behavioral difference. First exposure to reading a Python traceback (bottom-to-top for cause, then call chain).

**End-goal link:** input validation in model-serving code exists to catch exactly this class of error before it crashes a service.

---

## 1.1.3 — Slope, Intercept (y = mx + b)

**Concept:** `m` = slope (rate of change), `b` = y-intercept (value when x=0).

**Formula:** `y = mx + b`; slope between two points: `m = (y2-y1)/(x2-x1)`.

**Worked example:** `y=2x+3`: table x=0..3 → y=3,5,7,9. Slope check on (1,5),(3,9): m=2 ✓.

**Practice results:** Verified slope constant across non-adjacent points (own extension). m=-5,b=5 → correctly decreasing. Correctly predicted m=0 → horizontal line at y=b (zero rate of change).

**End-goal link:** `y=mx+b` is the exact structural shape of linear regression (Phase 2) — m→weight, b→bias.

---

## 1.1.4 — Exponents and Logarithms

**Concept:** Exponent: repeated multiplication. Log: inverse question — "what power gives this number?" Log turns multiplication into addition, preventing underflow.

**Formula:** `logb(x) = y ⟺ bʸ = x`. `log(1) = 0` for any base. `log(a×b) = log(a)+log(b)`.

**Worked example:** `log2(16)=4`, `log10(100)=2`, `2**10=1024 ↔ log2(1024)=10`.

**Practice results:** All verified. Correctly predicted `math.log(0)` raises an error; got `ValueError: expected a positive input` (Python 3.14's updated wording for "math domain error"). Correctly reasoned: positive base to any real exponent is always >0, never reaching exactly 0.

**Gotcha:** `ZeroDivisionError` vs `ValueError` — different exception types for related but distinct undefined operations.

**End-goal link:** log-based loss functions (cross-entropy, log-likelihood) are the numerical-stability backbone of classifiers and language models from Phase 2 onward.

---

# Section 1.2 — Calculus

## 1.2.1 — Derivatives: Local Slope, Numeric Intuition

**Concept:** Derivative = slope measured locally (at one point) rather than globally (whole line). Approximated by shrinking the gap between two very close points.

**Formula:** `f'(x) ≈ (f(x+h) - f(x)) / h`, for small h.

**Worked example:** `f(x)=x²` at x=3: h=0.001 gives slope≈6.001, converging to true value 6.

**Practice results:** x=3→6.0001, x=0→~0, x=-2→-3.9999 — discovered `f'(x)=2x` pattern directly from the numbers. h-shrinking: 0.0001→error+0.0001; 1e-8→error-3.6e-8 (more accurate). Correctly reasoned lines have constant derivative = their slope (2 for 2x+3, 0 for f(x)=5).

**Gotcha:** shrinking h too far (below ~1e-12 to 1e-15) causes **catastrophic cancellation** — floating point can't distinguish `f(x+h)` from `f(x)`, accuracy gets *worse*, not better. There's a sweet spot for h, not "smaller is always better."

**End-goal link:** this numeric-derivative technique is literally "gradient checking" — sanity-checking a hand-derived analytical gradient against a numeric approximation when debugging backprop (Phase 3).

---

## 1.2.2 — Power Rule, Chain Rule

**Concept:** Power rule: exact derivative shortcut for any power of x. Chain rule: derivative of nested functions — outer derivative times inner derivative.

**Formula:** Power rule: `f(x)=xⁿ → f'(x)=n·x^(n-1)`. Chain rule: `f(x)=g(h(x)) → f'(x)=g'(h(x))·h'(x)`.

**Worked example:** `f(x)=x³→f'(x)=3x²`, f'(2)=12. Chain: `f(x)=(2x+3)²→f'(x)=8x+12`, f'(1)=20.

**Practice results:** Generalized to any n (not just cubic). x³ at x=3: exact=27, numeric≈27.0009 ✓. Chain rule on (2x+3)² at x=3: exact=36, numeric≈36.0004 ✓. Correctly predicted derivative of x¹ = 1 (matches known slope of f(x)=x).

**End-goal link:** power rule + chain rule, applied repeatedly through many nested layers, constitute backpropagation (Phase 3.5) — nothing conceptually new happens at scale, only more bookkeeping.

---

## 1.2.3 — Partial Derivatives

**Concept:** Derivative with respect to one variable, treating all others as constants. Mechanics: apply single-variable rules to the target variable only.

**Formula:** `∂f/∂x` — e.g. for `f(x,y)=x²+y²`: `∂f/∂x=2x`, `∂f/∂y=2y`. For `f(x,y)=xy`: `∂f/∂x=y`, `∂f/∂y=x`.

**Worked example:** At (3,4): ∂f/∂x=6, ∂f/∂y=8 for x²+y².

**Practice results:** Verified via generalized f(x,y,n)=xⁿ+yⁿ. Discovered the xy case independently (variables swap in each other's partial — seed of the product rule). Extended to 3 variables (x²+y²+z² at (3,4,5)): all three partials correct, each depending only on its own variable.

**End-goal link:** the atomic operation computed once per weight during real model training — one partial derivative per parameter, per step.

---

## 1.2.4 — Gradients, Gradient Descent

**Concept:** Gradient = vector of all partial derivatives, collected together. Points in direction of steepest increase. Moving opposite it decreases a function fastest — this *is* gradient descent.

**Formula:** `∇f(x,y) = [∂f/∂x, ∂f/∂y]`. Update rule: `x_new = x - learning_rate × ∇f`.

**Worked example:** f(x,y)=x²+y² at (3,4): ∇f=[6,8].

**Practice results:** Verified ∇f(3,4)=[6,8]. Ran 50-step descent from (3,4): x,y shrank toward 0, f(x,y) fell 25→4.8, step size visibly decelerating near the minimum (gradient shrinks as x,y shrink) — first exposure to Python `for`/`range`/modulo/tuple-unpacking.

**End-goal link:** this is the complete training mechanism, seen end-to-end for the first time on a toy 2-variable function — Phase 2-3 scale it up, no new core idea.

---

## 1.2.5 — Optimization, Local vs Global Minima

**Concept:** "Optimization" in ML = minimizing a loss function. Moving opposite the gradient is the direction of steepest decrease by definition. On non-bowl-shaped (bumpy) functions, gradient descent only sees local slope — starting point can determine which minimum is reached.

**Formula:** Same update rule as 1.2.4, applied to `f(x)=x⁴-4x²` (two minima at x=±√2≈±1.41421, local max at x=0).

**Practice results:** Self-caught indentation bug (return nested inside loop, causing 1-step early exit). Fixed, 100-step results: x_start=1.5→1.41416, x_start=-1.5→-1.41426 (both converged correctly to separate valleys). x_start=0.01→1.4127 (escaped the near-zero-gradient plateau near x=0 after slow start). x_start=0 exactly→0.1096 (floating-point noise in the numeric derivative broke the theoretical zero-slope unstable equilibrium; tiny nudge compounded over 100 real steps into visible movement).

**Gotcha:** unstable equilibria — theoretically balanced (zero slope), but any infinitesimal perturbation (even numerical noise) causes eventual departure, which compounds over iterations rather than staying negligible.

**End-goal link:** real deep learning loss surfaces are bumpy, not clean bowls — this is the first hands-on encounter with why training isn't a single guaranteed path, and why initialization (3.9) matters.

---

## 1.2.6 — Convex vs Non-Convex Functions

**Concept:** Convex = exactly one minimum, connecting-line-between-any-two-points test never dips below the curve. Non-convex = multiple local minima/plateaus/saddle points.

**Formula:** Convexity test: for any two points on f, the straight line between them lies on or above f.

**Practice results:** Correctly identified straight lines as the convex boundary case (line lies exactly *on* the curve). On f(x)=-x² (concave, unbounded below): corrected from "settles at endpoints" to the accurate behavior — gradient descent minimizing this diverges toward -∞, since there are no endpoints; correctly proposed gradient ascent as the fix for finding the actual maximum. Correctly concluded own future models will have non-convex loss landscapes; refined "gradients can be wrong" to "gradients are locally accurate but globally shortsighted."

**End-goal link:** convex losses (linear regression, 2.2) guarantee a single global optimum regardless of starting point; non-convex losses (all neural networks, 3+) are why initialization, momentum/Adam (3.7), and run-to-run training variance all exist.

**Milestone:** Section 1.2 (Calculus) complete — derivative → rules → partial derivatives → gradients → optimization → convexity, one continuous self-verified arc.

---

# Section 1.3 — Linear Algebra

## 1.3.1 — Vectors: Addition, Scaling

**Concept:** Ordered list of numbers = magnitude + direction (arrow from origin). Addition: place second arrow's tail at first's tip. Scaling: stretch/shrink/flip without changing line of direction (unless negative).

**Formula:** `[a1,a2]+[b1,b2]=[a1+b1,a2+b2]`. `c×[a,b]=[ca,cb]`.

**Worked example:** `[3,4]+[1,2]=[4,6]`. `3×[3,4]=[9,12]`. `-1×[3,4]=[-3,-4]`.

**Practice results:** All verified with own vectors [3,2],[1,4]. 0×v=[0,0] (zero vector, no direction). First linear combination: 2×[1,1]+3×[2,0]=[8,2].

**End-goal link:** a linear combination is exactly what a single neuron computes — weight1×input1+weight2×input2+....

---

## 1.3.2 — Dot Product

**Concept:** Multiply corresponding elements of two equal-length vectors, sum into one scalar. Geometric meaning: relates to the angle between vectors.

**Formula:** `a·b = a1b1+a2b2` (arithmetic). `a·b = |a||b|cos(θ)` (geometric) — same direction→large positive, perpendicular→exactly 0, opposite→large negative.

**Worked example:** `[3,4]·[1,2]=11`. `[3,4]·[-3,-4]=-25`. `[3,4]·[4,-3]=0` (perpendicular).

**Practice results:** All verified. Own 3D example gave 837.5 (strongly positive, roughly-similar-direction vectors). Correctly identified dot product as scalar-output vs. linear combination's vector-output; refined: dot product = linear combination where the scaling weights come from the other vector itself.

**End-goal link:** literal computation a neuron performs (before activation). Also the basis of semantic search/RAG (8.2, 8.4).

---

## 1.3.3 — Matrices: Shape, Notation

**Concept:** 2D grid of numbers. Shape = rows×columns, order matters. A whole neural network layer's weights = a matrix (one row per neuron).

**Formula:** Shape `(rows, cols)`; transpose swaps them: `(m,n)→(n,m)`.

**Worked example:** `W=[[0.1,0.2,0.3],[0.4,0.5,0.6]]`, shape (2,3) — 2 neurons, 3 weights each.

**Practice results:** All verified (shape, get_row, get_column). Correctly predicted transpose of a 2×3 gives 3×2.

**End-goal link:** matrices are the actual data structure holding every layer's weights in every real model.

---

## 1.3.4 — Matrix-Vector Multiplication

**Concept:** Produces a new vector — each entry is the dot product of one matrix row with the input vector. One dot product per row.

**Formula:** `(Mv)_i = row_i(M) · v`.

**Worked example:** `M=[[2,1],[0,4]]`, `v=[3,5]` → `[11,20]`.

**Practice results:** Verified. Applied to W(2×3)·x=[1,2,3]→[1.4,3.2] (a real layer's output for one input). Strong independent reasoning on shape mismatches: distinguished silent incomplete result (row shorter than v) vs. loud IndexError (row longer than v), based on which vector's length drives the dot-product loop.

**End-goal link:** this is the forward-pass computation for one layer given one input.

---

## 1.3.5 — Matrix-Matrix Multiplication

**Concept:** Matrix-vector multiplication extended to a whole batch at once — stack input vectors as columns of a second matrix. Shape rule follows directly from the dot product's equal-length requirement.

**Formula:** `(AB)_ij = row_i(A) · col_j(B)`. Shape rule: `(m×n)·(n×p) = (m×p)` — inner dimensions must match.

**Worked example:** `A=[[1,2],[3,4]]`,`B=[[5,6],[7,8]]` → `A·B=[[19,22],[43,50]]`.

**Practice results:** Verified. W(2×3)·X(3×2 batch of 2 inputs)=[[1.4,3.2],[3.2,7.7]] — full mini-batch forward pass. Proactively added shape-validation (own initiative, before being asked) — independently reinvented the pattern real frameworks use. Confirmed predicted IndexError when validation removed on a genuine mismatch.

**End-goal link:** the literal batch forward-pass computation used in every real training step from Phase 2 onward.

---

## 1.3.6 — Matrix Transformations & Eigenvalues

**Concept:** A matrix transforms space (stretch/rotate/reflect). Eigenvectors are special vectors whose direction a matrix doesn't change — only scales. Eigenvalue = the scale factor.

**Formula:** `M·v = λ·v`. Identity matrix: every vector is an eigenvector, λ=1 always (degenerate case).

**Worked example:** M=[[2,0],[0,1]]: [1,0]→eigenvector,λ=2; [0,1]→eigenvector,λ=1; [1,1]→not an eigenvector (direction changes).

**Practice results:** Extensive line-by-line code walkthrough of the verification logic (filter conditions, generator expressions, tolerance comparison `abs(diff)<1e-9` vs `diff>0` vs rounding). Verified M=[[2,0],[0,1]] cases. N=[[0,1],[1,0]] (reflection across y=x): [1,1]→λ=1 (on the mirror line), [1,-1]→λ=-1 (perpendicular, flips exactly) — both correctly predicted. Self-observed: a reflection has exactly two eigenvector directions.

**Gotcha:** eigenvectors are unique only up to sign (v and -v both valid).

**End-goal link:** foundation of PCA (1.3.10); explains vanishing/exploding gradients (repeated multiplication by matrices with eigenvalues consistently <1 or >1).

---

## 1.3.7 — Norms & Distances

**Concept:** Norm = vector magnitude. L2 = ordinary (Euclidean/Pythagorean) length. L1 = sum of absolute values ("Manhattan/taxicab" distance). Cosine similarity = angle only, ignores length entirely.

**Formula:** `||v||₂=√(Σxi²)`. `||v||₁=Σ|xi|`. `distance(a,b)=||a-b||₂`. `cosine_similarity(a,b)=(a·b)/(||a||×||b||)`.

**Worked example:** `[3,4]`: L1=7, L2=5. cosine_similarity([3,4],[1,2])≈0.984.

**Practice results:** All verified, matching hand-computed values. Key result: `cosine_similarity([3,4],[6,8])=1.0` — confirms cosine similarity is entirely length-invariant (only measures direction), unlike raw dot product.

**End-goal link:** L2/weight-decay used in most loss functions (3.8); L1 encourages sparsity (2.7, 8.6 LoRA); cosine similarity is the standard tool for embedding comparison in semantic search (8.2), specifically because it's length-invariant.

---

## 1.3.8 — Tensors: Shape, Axes, Broadcasting

**Concept:** Tensor generalizes scalar(0D)→vector(1D)→matrix(2D)→ND. Shape = tuple, each position is an axis. Broadcasting: implicitly stretches a smaller array to match a larger one's shape during an operation, without copying data.

**Formula:** Shape of nested list = recursive `(len(tensor),) + shape(tensor[0])`. Broadcasting example: `M(2×3) + b(3,)` → b added to every row of M.

**Worked example:** `M=[[1,2,3],[4,5,6]]`, `b=[10,20,30]` → `[[11,22,33],[14,25,36]]`.

**Practice results:** Full recursion trace worked through (tuple concatenation, base case, unwinding). Two self-produced bugs caught and fixed: a copy-paste variable-testing slip, and a flat (non-nested) comprehension that produced a wrong flat list instead of a proper matrix — fixed to nested comprehension. Verified shapes: (3,), (3,2), (2,2,2). Confirmed the same "which array's length drives the loop" mismatch pattern from 1.3.4/1.3.5, generalized correctly (silent incomplete result vs. IndexError).

**End-goal link:** real training data is almost always 3D-4D+ tensors (e.g. image batches: batch×height×width×channels). Shape-mismatch debugging is the single most-used skill from Phase 3 onward.

---

## 1.3.9 — SVD: Concept, Compression, Embeddings

**Concept:** Any matrix `M = U·Σ·Vᵀ`. Σ = diagonal, non-negative, sorted-largest-to-smallest singular values (ranked "importance"). U, V = orthonormal rotation-like matrices. Not hand-derived (advanced numerics) — used via `np.linalg.svd` as a tool.

**Formula:** `M = U·Σ·Vᵀ`. Singular values `= √(eigenvalues of MᵀM)`. Columns of V = eigenvectors of MᵀM; columns of U = eigenvectors of MMᵀ, both constrained to unit length + mutual perpendicularity (orthonormal).

**Worked example:** M1=[[3,0],[0,1]] (diagonal, symmetric) → singular values [3,1] directly (U,V=identity, no rotation needed). M2=[[4,0],[3,-5]] → singular values [6.3246,3.1623].

**Practice results:** Verified M1, M2 reconstructions. Compression demo: zeroing the smaller singular value gave a rough approximation ([[2,-2],[4,-4]] vs real [[4,0],[3,-5]]) — correctly predicted inexact, refined to: compression only works well with a large gap between important/unimportant singular values (this toy case had a ratio of only ~2x, too close). **Addendum:** hand-derived singular values via Mᵀ·M→eigenvalues→√ on M2, verified against NumPy's output exactly. **Addendum 2:** verified V's columns directly against M2's real Vt output — confirmed unit length, perpendicularity, and eigenvector identity by hand.

**Gotcha:** singular values are always non-negative (unlike ordinary eigenvalues) because they come from MᵀM/MMᵀ, which are guaranteed to have non-negative eigenvalues. Sign of eigenvectors/singular vectors is not unique (only the direction/line is).

**End-goal link:** classical (pre-neural) word embeddings were built via SVD on co-occurrence matrices. Directly underlies LoRA (8.6, low-rank adaptation).

---

## 1.3.10 — PCA, Dimensionality Reduction, t-SNE/UMAP Concept

**Concept:** Finds the directions of maximum variation in data via eigenvectors of the covariance matrix — largest eigenvalue's eigenvector is the first principal component. Deeply related to SVD (real libraries often compute PCA via SVD internally).

**Formula:** Covariance matrix: `(centeredᵀ·centered)/(n-1)`, where `centered = data - mean(data)`. Principal components = eigenvectors of the covariance matrix, ordered by eigenvalue.

**Worked example:** 4 near-linear points `[[2,3],[3,4],[4,5],[5,6]]` → dominant eigenvalue 3.333 (direction [0.707,0.707], matching the data's [1,1] line), near-zero second eigenvalue.

**Practice results:** Full line-by-line code walkthrough given (axis vocabulary, broadcasting, np.linalg.eig, argsort+reverse, 2D column indexing). Verified the predicted eigenvalue gap. Reduced 1D values evenly spaced by √2, matching the [1,1] step length. Gotcha encountered: `np.linalg.eig` returns complex dtype (`+0.j`) even for guaranteed-real eigenvalues. Conceptual PCA-vs-t-SNE/UMAP question needed correction from vague framing to the real distinction: PCA preserves global/linear structure; t-SNE/UMAP preserve local neighborhoods at the cost of global shape (better for visualizing non-linear clusters, e.g. semantically similar code snippets).

**Addendum:** t-SNE minimizes KL-divergence (previewed, formal coverage in 1.5.2) between high-D and low-D neighbor-probability distributions via gradient descent (same core mechanism as 1.2.4). UMAP is topology-based (out of scope), generally faster, better global-structure preservation, more commonly used default today.

**End-goal link:** visualizing high-dimensional embeddings (5B.3, 8.2); anticipates why some weight-space directions matter more than others during training.

---

## 1.3.11 — Linear Systems: Solving Ax = b

**Concept:** Generalizes 1.1.1 (one equation, one unknown) to many equations/unknowns via matrices. If A has an inverse, x = A⁻¹b — the matrix analog of division.

**Formula:** `A·x = b → x = A⁻¹b`. 2×2 inverse: `A⁻¹ = (1/det(A))×[[d,-b],[-c,a]]` for `A=[[a,b],[c,d]]`, `det(A)=ad-bc`.

**Worked example:** A=[[2,1],[1,-1]], b=[11,1] → det(A)=-3, x=[4,3]. Verified by substitution.

**Practice results:** Verified via `np.linalg.solve` (flagged as numerically better than the naive inverse formula). Own example A=[[3,2],[1,-1]],b=[12,1]→x=[2.8,1.8], verified by substitution. Correctly predicted det(A)=0 for A=[[2,4],[1,2]] means no inverse; confirmed `LinAlgError: Singular matrix`. Reasoning refined: not literally "1/0 crashes" (solve() doesn't use naive inverse internally) but the same underlying mathematical wall — a **singular matrix** has no inverse regardless of algorithm, here because the second row was an exact scalar multiple of the first (same line, not two independent constraints). Connected to 1.3.6: singular matrices always have 0 as an eigenvalue.

**End-goal link:** closed-form linear regression (2.2) is literally solving a linear system; appears repeatedly as a subroutine in more advanced optimization methods.

---

## 1.3.12 — Numerical Stability

**Concept:** Consolidates the floating-point theme recurring since 1.2.1. An algorithm is numerically unstable if it amplifies small input/rounding errors into large output errors. Deep networks chain thousands of operations — this is directly why exploding/vanishing gradients (3.13) are real, named problems.

**Formula:** Underflow prevention: `log(a×b) = log(a)+log(b)` (turns multiplication into addition, avoids collapse to exactly 0.0). Machine epsilon near magnitude 1.0 ≈ 2.22×10⁻¹⁶ — the smallest representable gap between two distinct floats at that scale.

**Worked example:** Multiplying 200 copies of 0.01 directly collapses to exactly 0.0 around iteration 162 (float64's absolute floor, ~5×10⁻³²⁴); the log-space sum stays precise the entire time.

**Practice results:** Underflow demo confirmed as predicted (theme, not surprising). Catastrophic cancellation, sharpest version: predicted `(1.0+1e-16)-1.0` ≈1e-16 — actual result exactly 0.0, a genuine miss. Corrected via machine epsilon: 1e-16 is smaller than the smallest gap representable near 1.0, so the addition itself silently rounds away *before* any subtraction happens — total information loss, not partial. Conceptual question on why NumPy's internal algorithms (LU/QR decomposition, named not built) beat naive inverse-via-determinant required a full rebuild, resolved by connecting directly to the cancellation result: naive inverse computation has many subtraction/division steps, each a potential cancellation site, worse as matrices grow or determinants shrink.

**Gotcha:** some floating-point failures aren't gradual accumulation — they're instant, complete information loss the moment a value crosses below the local precision floor.

**End-goal link:** direct conceptual bridge to Phase 3.13 (vanishing/exploding gradients) and explains why real training code uses log-space probabilities and library solvers rather than mathematically-equivalent-but-fragile naive formulas.

**MILESTONE: Section 1.3 (Linear Algebra) — FULLY COMPLETE.** All 12 lessons: vectors → dot product → matrices → matrix-vector → matrix-matrix → eigenvalues → norms/distances → tensors/broadcasting → SVD → PCA → linear systems → numerical stability. Every lesson hand-built and self-verified; NumPy introduced as a tool from 1.3.9 onward per the curriculum's own rule.

---

# Section 1.4 — Probability & Statistics

## 1.4.1 — Mean, Variance, Standard Deviation

**Concept:** Mean = center. Variance = average squared distance from the mean (squaring prevents cancellation, same reasoning as L2 norm). Std dev = √variance, restores original units.

**Formula:** `mean = Σx/n`. `variance = Σ(x-mean)²/n`. `std = √variance`.

**Worked example:** `[2,4,4,4,5,5,7,9]` → mean=5, variance=4, std=2.

**Practice results:** Verified. `[3,4,5,6,7]` (same mean, tighter spread) → variance=2, correctly smaller. `[5,5,5,5,5]` → variance=0, std=0, correctly predicted (every distance from mean is 0).

**End-goal link:** the covariance matrix (1.3.10 PCA) is this exact idea generalized across features jointly. Central to feature normalization (Phase 2), weight initialization (3.9), diffusion noise control (5D.5).

---

## 1.4.2 — Probability Basics: Events, Independence, Combinations

**Concept:** Probability = favorable/total outcomes. Independent events: one tells you nothing about the other; `P(A and B) = P(A)×P(B)`. Combinations: distinct ways to choose k items from n, order irrelevant.

**Formula:** `P(event) = favorable/total`. `P(A and B) = P(A)×P(B)` (independent only). `C(n,k) = n!/(k!(n-k)!)`.

**Worked example:** P(rolling a 4)=1/6. P(heads,heads)=0.25. C(4,2)=6.

**Practice results:** All verified. Three-flip case computed via recursive reuse of `independent_and` → 0.125 — noted the halving pattern as the same underflow shape as 1.3.12. C(6,3)=20 (bigger pool, more combinations, as predicted). C(n,n)=1 correctly predicted and confirmed (only one way to choose everything).

**End-goal link:** independence underlies Naive Bayes (2.12); combinations matter for counting configurations/search spaces (e.g. game-move sequences).

---

## 1.4.3 — Bayes' Theorem

**Concept:** Lets you compute a hard-to-measure conditional probability from an easier-to-measure reverse one. Prior (belief before evidence) → posterior (belief after evidence).

**Formula:** `P(A|B) = P(B|A)×P(A) / P(B)`, where `P(B) = P(B|A)×P(A) + P(B|not A)×P(not A)`.

**Worked example (medical test):** 1% prevalence, 95% sensitivity, 5% false-positive rate → `P(disease|positive) ≈ 0.161`, far below the naive "95%" intuition (false positives from the large healthy population outnumber true positives from the rare disease group).

**Practice results:** Verified. p_a=0.5 (common disease) → exactly 0.95 — prior perfectly cancels with symmetric error rates at 50/50 prevalence, collapsing posterior to raw test accuracy. Resolved a genuine conceptual confusion: `P(B|A)+P(not B|A)=1` holds (within one fixed population), but `P(B|A)` and `P(B|not A)` describe two *separate* populations (sick vs. healthy) with independently-measured, unrelated error rates — no subtraction relationship connects them. Isolated-sensitivity rerun (0.6, false-positive rate unchanged) → 0.108, correctly smaller drop than the earlier combined-parameter-change run (0.0149).

**End-goal link:** foundation of Naive Bayes (2.12) and Bayesian prior/evidence/posterior thinking, reappearing in RL (5E) and model-confidence interpretation generally.

---

## 1.4.4 — Gaussian/Normal Distribution

**Concept:** Bell curve, fully defined by mean (center) and std dev (spread). Values near the mean are likely; far values rapidly less likely. Not hand-derived (PDF formula is advanced) — used via `np.random.normal` as a tool.

**Formula:** PDF: `f(x) = (1/(σ√(2π))) × e^(-(x-μ)²/(2σ²))`, μ=mean, σ=std dev.

**Worked example:** `np.random.normal(loc=mean, scale=std, size=n)` — `loc`=μ, `scale`=σ.

**Practice results:** Real early bug: confused `np.random.seed(42)` (reproducibility) with sample count (`n=42`), and never called `.seed()` at all — caught and corrected. Good follow-up question resolved: NumPy's random generator is **stateful** (hidden global cursor all `np.random.*` calls read/advance), unlike every pure function built so far in this curriculum; contrasted with JS's unseedable `Math.random()`. After fix: mean=0,std=1,n=1000 → empirical ≈(0.019,0.979), close but not exact (sampling noise, expected — not a bug). mean=100,std=15 (IQ parameters) → min/max within ~3 std devs of the mean. std=1 vs std=10 (same mean): range ratio ≈10x, matching the std ratio almost exactly.

**Gotcha:** empirical statistics from a finite sample never exactly match the true generating parameters — a different phenomenon from floating-point precision errors seen earlier; converges with larger sample sizes.

**End-goal link:** direct groundwork for weight initialization (3.9) and diffusion models (5D.5), both literal, hands-on applications of this exact distribution.

---

## 1.4.5 — Expected Value

**Concept:** Weighted average of all possible outcomes, weighted by their probability — "the long-run average if this process repeated many times." Mean (1.4.1) is the special case where observed data points get equal weight; expected value generalizes to theoretical probabilities over all possible outcomes.

**Formula:** `E[X] = Σ(xi × P(xi))`. Sanity check: probabilities must sum to exactly 1.

**Worked example:** Fair die: `E[X] = (1+2+3+4+5+6)/6 = 3.5` (not a possible single outcome — describes the long-run average only). Game (win $10 at 0.2, win $2 at 0.5, lose $5 at 0.3): `E[X] = 2+1-1.5 = 1.5`.

**Practice results:** Real, instructive bug: initial fair-die probabilities were `[1/6,2/6,3/6,4/6,5/6,6/6]` (increasing, summing to 3.5 instead of 1) rather than equal `1/6` each — self-debugged with print statements, caught via the "probabilities must sum to 1" sanity check. Corrected → 3.5 ✓. Game example verified → 1.5 ✓. Modified game (loss probability raised to 0.5) → -0.7, correctly predicted to flip negative. Explained in own words why weighting the worst outcome more heavily pulls expected value down; refined to the precise mechanic — a bigger weight on the negative term and smaller weights on the positive terms both push the weighted sum down simultaneously.

**Gotcha:** always sanity-check that a probability list sums to 1 before trusting any downstream calculation — an easy, high-value habit.

**End-goal link:** batch loss averages during training are empirical estimates of the *true* expected loss across the full real-world input distribution — connects directly to 1.4.4's sampling theme (finite samples approximate, but don't exactly equal, the true underlying value).

---

## 1.4.6 — Sampling Methods: Monte Carlo Basics

**Concept:** When an exact answer is too hard/slow to compute directly, simulate the process many times randomly and average the results as an approximation. More samples → better, more consistent estimate.

**Formula:** π estimation via random sampling: `π ≈ 4 × (fraction of random points inside a unit circle inscribed in a 2×2 square)`, using the L2-norm-based check `x²+y² ≤ 1` (1.3.7) for "inside the circle."

**Worked example:** `np.random.uniform(-1,1,n)` generates uniformly random points (every value in range equally likely, unlike 1.4.4's Gaussian); boolean array comparison + `.sum()` counts points inside the circle (True=1, False=0 when summed).

**Practice results:** n=1000 and n=100000 both landed close to true π (3.14, 3.14) in this particular run — the small-sample case somewhat lucky. Three repeated n=1000 calls (no fixed seed) gave genuinely different results (3.168, 3.148, 3.116) — directly demonstrated sampling variance at a fixed sample size, and that variance would shrink with larger n (reinforces 1.4.4's convergence theme). Batch-size/training connection needed to be built from scratch (initial "not sure") — resolved: batch size plays the same role as n_samples; larger batches → gradient estimates closer to the "true" gradient, less run-to-run variance (mirrors 100000 vs 1000-sample stability); smaller batches → noisier gradient estimates (mirrors the 3.168/3.148/3.116 spread). Noted as a preview: gradient noise from smaller batches can help escape shallow local minima (1.2.5), so "bigger is strictly better" isn't the complete picture — deferred to Phase 3.

**Gotcha:** none new mechanically — the real lesson was internalizing sampling variance by directly observing it across repeated runs, not just being told it exists.

**End-goal link:** RL value estimation (5E.3, literally titled "Monte Carlo methods"), diffusion model sampling (5D.5), and every training step's batch-based gradient estimate are all structurally this same idea — turn an intractable exact computation into a tractable random-sampling-and-averaging one.

---

## 1.4.7 — Statistics for ML: Bias, Variance, Confidence Intervals, Hypothesis Testing

**Concept:** **Bias** = is an estimate systematically wrong in one direction (consistently over/under, averaged over infinite samples)? **Variance** (statistical sense) = how much does an estimate wobble from sample to sample — directly what was observed in 1.4.6's three different π estimates. **Confidence interval** = a range likely to contain the true value, narrowing as sample size grows. **Hypothesis testing** = formal procedure for asking "is this observed effect real, or plausibly just noise?", via a null hypothesis (the "nothing special happening" default assumption).

**Formula:** Approximate 95% CI for a Gaussian-distributed mean: `CI = sample_mean ± 1.96 × (sample_std / √n)`. The `std/√n` term is the **standard error** — shrinks as n grows, which is why CIs narrow with more samples.

**Worked example:** n=1000, mean≈0.019, std≈0.979 (reusing 1.4.4's numbers): standard_error≈0.031, CI≈[-0.042, 0.079] — correctly contains the true mean, 0.

**Practice results:** Verified n=1000 CI contains 0. Verified the √n width-scaling prediction numerically: n=100→10000 (100x samples) gave a width ratio ≈9.55 (predicted 10x, since √100=10); n=100→1000 (10x samples) gave ratio ≈3.10 (predicted √10≈3.16x) — both close matches, minor deviation attributable to different underlying random datasets rather than the formula being wrong. Correctly diagnosed 1.4.6's three π estimates (3.168, 3.148, 3.116) as demonstrating **variance**, not bias — reasoned precisely that the errors were scattered on both sides of the true value (+0.026, +0.006, -0.026) rather than consistently one-directional, which is what genuine bias would look like instead.

**Gotcha:** none new mechanically — the real payoff was correctly distinguishing bias from variance using a concrete example already lived through, rather than abstract definitions alone.

**End-goal link:** direct, explicit setup for Phase 2.5 (overfitting vs. underfitting) — underfit models show high bias (systematically, predictably wrong regardless of training data), overfit models show high variance (wildly sensitive to which specific training data they saw) — the exact same bias/variance distinction just practiced here, applied to model behavior instead of a π estimate. Also foundational to honestly reporting model performance (accuracy ± confidence interval, not just a bare number) and to correctly interpreting whether an observed improvement between two models is real or just sampling noise.

**MILESTONE: Section 1.4 (Probability & Statistics) — FULLY COMPLETE.** All 7 lessons: mean/variance/std → probability/independence/combinations → Bayes' theorem → Gaussian distribution → expected value → Monte Carlo sampling → bias/variance/confidence intervals. Every lesson hand-built or NumPy-tool-verified, with real, instructive bugs caught and fixed along the way (probability-sum-to-1 sanity check, seed/sample-count confusion).

---

*Next: Section 1.5 — Information Theory, starting with 1.5.1 — Entropy.*