# AI From Scratch — Learner's Curriculum

> Combined from personal tutoring plan + rohitg00/ai-engineering-from-scratch (503 lessons, 20 phases)
> Cross-references included per topic — no manual checking needed.

**Starting point:** 10 yrs frontend dev (JS/React/Next.js), strong logical reasoning, math and ML at true zero.
**Goal:** Build/train AI models across any domain from scratch — own code, own math, own training loops.
**End goal:** A personal Jarvis-style AI platform — business revenue model, game generation, coding assistant, website generation, 3D generation — all specialized AIs orchestrated under one unified interface. Not one model, a platform of specialized models that talk to each other. Every phase of this curriculum maps directly toward this.
**Method:** Concept → worked numeric example → code mapping → you write it → verify. No phase skipped.

---

## What "from scratch" means here (read this)

Literal: model, training loop, backprop, attention — written in raw Python/NumPy by you.

- **NumPy** = allowed. It's just fast arithmetic, not thinking-for-you.
- **PyTorch / `.backward()` / pretrained models** = NOT allowed as foundation. Introduced in Phase 5+ only after you've hand-built the equivalent yourself, so you know exactly what they automate.
- **Frameworks become tools you use with full understanding — not a black box you depend on.**

---

## Note to self (Claude): documentation rule

After every topic, before moving on:

1. Tick the checkbox `[x]`
2. Add a one-line dated entry to the **Progress Log**
3. Append a full entry to that phase's file in `notes/` (concept + worked example + key code + gotchas)
4. Note the repo cross-reference so the learner can read their angle as a second pass

Never write detailed notes inline in this tracker. It stays an index.
Never use the learner's name anywhere in docs — refer to "the learner" if needed.

---

## Tutor-mode instructions (read at the start of every session)

1. **Check this file first** — find first unchecked box. If learner says "where are we," answer from here directly, no questions asked.
2. **Teaching order per topic always**: (a) plain-language concept, (b) worked numeric example with real numbers, (c) map math to code line-by-line, (d) learner writes and runs it in VS Code, (e) predict-then-verify question before moving on.
3. **Never skip ahead** unless learner explicitly asks.
4. **Enforce from-scratch rule** — no frameworks until Phase 5+.
5. **After each topic**: tick box, log entry, notes file entry — before next topic. One commit per topic, everything bundled — never separate commits for notes vs code.
6. **Sessions end at clean checkpoints** — one topic fully closed, not mid-explanation.
7. **Math is zero** — never assume recall. Rebuild every concept as if it's new.
8. **Tone**: full math explanations from scratch; never explain basic programming logic the learner already knows (10 yrs JS/React/Next.js experience). Never be condescending about programming basics.
9. **Repo cross-reference**: after each topic closes, always point to the exact lesson in rohitg00/ai-engineering-from-scratch for a second-pass read. Format: `→ repo: phases/NN-phase-name/NN-lesson-name`. The learner reads their code/angle after our session — never instead of it.
10. **ML jargon**: when ML terms come up before they're formally taught (tensors, weights, gradients etc.), give a one-line plain-language note and move on. Don't explain them fully until their scheduled lesson — the gap fills itself as we go.
11. **End goal awareness**: examples, datasets, and projects should connect to the end goal wherever possible — game AI, 3D generation, business agents, coding assistants, website generation. Make it relevant, not abstract.
12. **No names in any docs** — notes, curriculum, progress log — never use the learner's name. Refer to "the learner" if a reference is needed.

---

## Repo reference workflow (rohitg00/ai-engineering-from-scratch)

After every completed topic:

- Point to the exact repo lesson — `→ repo: phases/NN-phase-name/NN-lesson-name`
- Learner reads their version as a second pass — different angle, sometimes different code
- If their lesson adds something beyond what was covered, flag it explicitly: "their lesson adds X which we didn't cover — worth reading"
- Learner can also go through repo independently and raise questions — those get answered in the next session

The repo is a textbook. Our sessions are the actual teaching. Never the other way around.

---

## Git commit conventions

Format: `Phase X.Y: <what was built>`
Examples:

- `Phase 0.1: algebra and functions from scratch`
- `Phase 2.2: linear regression hand-coded, no libraries`
- `Phase 3.5: autograd engine (micrograd-style)`
- `Phase 3.8: nanoGPT — own tokenizer, attention, training loop`

Commit once per topic, after code runs and concept clicked — not mid-debug.

---

## Folder structure

```
ai-from-scratch/
├── ai-curriculum.md              # this file — index only
├── notes/                        # detailed lesson notes, one file per phase
│   ├── phase0-setup.md
│   ├── phase1-math.md
│   ├── phase2-ml.md
│   ├── phase3-deep-learning.md
│   ├── phase4-neural-nets.md
│   ├── phase5-domains/
│   │   ├── vision.md
│   │   ├── nlp.md
│   │   ├── speech-audio.md
│   │   ├── generative-ai.md
│   │   └── rl.md
│   ├── phase6-transformers-llms.md
│   ├── phase7-agents.md
│   └── phase8-production.md
├── phase0-setup/
├── phase1-math/
├── phase2-ml/
├── phase3-deep-learning/
├── phase4-neural-nets/
│   ├── perceptron/
│   ├── autograd-engine/
│   ├── makemore/
│   └── nanogpt/
├── phase5-domains/
│   ├── vision/
│   ├── nlp/
│   ├── speech-audio/
│   ├── generative-ai/
│   └── rl/
├── phase6-transformers-llms/
├── phase7-agents/
└── phase8-production/
```

---

## Phase 0 — Setup & Environment

_Get the machine ready before any math or code._
→ repo: `phases/00-setup-and-tooling/`

- [x] **0.1** Python environment (venv, pip, folder structure)
- [x] **0.2** VS Code setup (Python + Jupyter extensions, linting)
- [x] **0.3** Git basics — init, commit, log, branch (used every session from here)
- [x] **0.4** Jupyter notebooks — when to use vs plain `.py`
- [x] **0.5** GPU setup & cloud basics (Google Colab as fallback when compute needed)
- [x] **0.6** Docker for AI — containers for reproducibility (intro only, used in Phase 8)
- [x] **0.7** Data management basics — file formats (CSV, JSON, Parquet), folder conventions
- [x] **0.8** Debugging & profiling Python — `pdb`, `cProfile`, `line_profiler`

---

## Phase 1 — Math Foundations (rebuild from zero)

_Every concept explained with real numbers before any code._
→ repo: `phases/01-math-foundations/`

### 1.1 Algebra

- [x] **1.1.1** Variables, expressions, solving for x
- [x] **1.1.2** Functions: what `f(x)` means, domain, range
- [x] **1.1.3** Graphing lines: slope, intercept (`y = mx + b`)
- [x] **1.1.4** Exponents and logarithms — why `log` is everywhere in ML
      → repo: no direct match confirmed (see notes)

### 1.2 Calculus

- [x] **1.2.1** What a derivative is — rate of change, slope of a curve, numeric intuition
- [x] **1.2.2** Derivative rules: power rule, chain rule — worked examples by hand
- [ ] **1.2.3** Partial derivatives — multi-variable functions
- [ ] **1.2.4** Gradients — vector of partial derivatives, what "gradient descent" literally means
- [ ] **1.2.5** Optimization — minimizing a function, why we move against the gradient
- [ ] **1.2.6** Convex vs non-convex functions — why it matters for training
      → repo: `04-calculus-for-ml`, `05-chain-rule-and-autodiff`, `18-convex-optimization`

### 1.3 Linear Algebra

- [ ] **1.3.1** Vectors — what they are, addition, scaling, geometric intuition
- [ ] **1.3.2** Dot product — computed by hand, geometric meaning (angle, similarity)
- [ ] **1.3.3** Matrices — what they represent, shapes, notation
- [ ] **1.3.4** Matrix-vector multiplication — by hand on 2×2 example
- [ ] **1.3.5** Matrix-matrix multiplication — by hand, why the shapes must match
- [ ] **1.3.6** Matrix transformations & eigenvalues — what a matrix "does" to space
- [ ] **1.3.7** Norms & distances — L1, L2, cosine distance, why they matter
- [ ] **1.3.8** Tensor operations — N-dimensional arrays, shape, axes, broadcasting
- [ ] **1.3.9** Singular Value Decomposition (SVD) — concept + why it underlies embeddings & compression
- [ ] **1.3.10** Dimensionality reduction — PCA from scratch, t-SNE/UMAP concept
- [ ] **1.3.11** Linear systems — solving Ax = b
- [ ] **1.3.12** Numerical stability — why floating point errors matter in deep learning
      → repo: `02-vectors-matrices-operations`, `03-matrix-transformations`, `11-svd`, `12-tensor-operations`, `13-numerical-stability`, `14-norms-and-distances`, `10-dimensionality-reduction`, `17-linear-systems`

### 1.4 Probability & Statistics

- [ ] **1.4.1** Mean, variance, standard deviation — by hand on a small dataset
- [ ] **1.4.2** Probability basics — events, independence, combinations
- [ ] **1.4.3** Bayes' theorem — worked example, why it's foundational
- [ ] **1.4.4** Distributions — Gaussian/normal (shows up in weight init, noise, diffusion)
- [ ] **1.4.5** Expected value — definition + worked example
- [ ] **1.4.6** Sampling methods — Monte Carlo basics, why we sample instead of compute exactly
- [ ] **1.4.7** Statistics for ML — bias, variance, confidence intervals, hypothesis testing
      → repo: `06-probability-and-distributions`, `07-bayes-theorem`, `15-statistics-for-ml`, `16-sampling-methods`

### 1.5 Information Theory

- [ ] **1.5.1** Entropy — what it measures, why it appears in loss functions
- [ ] **1.5.2** KL Divergence — measuring distance between distributions
- [ ] **1.5.3** Cross-entropy loss — derived from information theory, used in classification
      → repo: `09-information-theory`

### 1.6 Advanced Math (deferred, covered when domain needs it)

- [ ] **1.6.1** Complex numbers for AI (relevant for Fourier, signal processing)
- [ ] **1.6.2** Fourier Transform — frequency domain, why audio/signal AI needs this
- [ ] **1.6.3** Graph theory for ML — nodes, edges, adjacency, relevance to GNNs
- [ ] **1.6.4** Stochastic processes — random walks, Markov chains (relevant for diffusion & RL)
      → repo: `19-complex-numbers`, `20-fourier-transform`, `21-graph-theory`, `22-stochastic-processes`

---

## Phase 2 — ML Fundamentals (hands-on, no frameworks)

_Classical ML — still the backbone of most production AI._
→ repo: `phases/02-ml-fundamentals/`

- [ ] **2.1** What machine learning actually is — map from data to prediction, types (supervised/unsupervised/RL)
- [ ] **2.2** Linear regression from scratch — gradient descent loop in raw Python/NumPy
- [ ] **2.3** Logistic regression from scratch — classification, sigmoid, binary cross-entropy
- [ ] **2.4** Train / validation / test split — why it exists, how to do it right
- [ ] **2.5** Overfitting vs underfitting — visualized with learning curves
- [ ] **2.6** Model evaluation — accuracy, precision, recall, F1, ROC/AUC, confusion matrix
- [ ] **2.7** Feature engineering & selection — what it is, why it matters, worked example
- [ ] **2.8** Decision trees from scratch — how splits are chosen (information gain)
- [ ] **2.9** Random forests — bagging, why ensembles beat single trees
- [ ] **2.10** Support Vector Machines — margin, kernel trick concept
- [ ] **2.11** KNN & distance metrics — simplest possible classifier, built by hand
- [ ] **2.12** Naive Bayes — probabilistic classifier from scratch
- [ ] **2.13** Unsupervised learning — K-Means and DBSCAN from scratch
- [ ] **2.14** Ensemble methods — boosting (AdaBoost, gradient boosting), stacking
- [ ] **2.15** Hyperparameter tuning — grid search, random search, what to tune
- [ ] **2.16** ML pipelines & experiment tracking — structure of a real training run
- [ ] **2.17** Time series fundamentals — stationarity, autocorrelation, ARIMA concept
- [ ] **2.18** Anomaly detection — isolation forest, statistical methods
- [ ] **2.19** Handling imbalanced data — oversampling, undersampling, class weights
      → repo: `01` through `18` lessons in `phases/02-ml-fundamentals/`

---

## Phase 3 — Deep Learning Core (from scratch, no autograd)

_Neural networks built by hand. Frameworks don't appear until lesson 3.11._
→ repo: `phases/03-deep-learning-core/`

- [ ] **3.1** The perceptron — simplest neural net, by hand, with worked numbers
- [ ] **3.2** Multi-layer networks — forward pass by hand on a tiny 2-layer net
- [ ] **3.3** Activation functions — ReLU, sigmoid, tanh, GELU — why nonlinearity matters
- [ ] **3.4** Loss functions — MSE, cross-entropy, contrastive — derived, not memorized
- [ ] **3.5** Backpropagation — derive it by hand on a 2-layer net using chain rule
- [ ] **3.6** Build a tiny neural net in pure Python/NumPy — forward + backward pass
- [ ] **3.7** Optimizers — SGD, Momentum, Adam, AdamW — intuition + coded from scratch
- [ ] **3.8** Regularization — dropout, weight decay, batch normalization — why each helps
- [ ] **3.9** Weight initialization — why random init matters, Xavier/He init
- [ ] **3.10** Learning rate schedules & warmup — cosine decay, linear warmup
- [ ] **3.11** **Build your own autograd engine (micrograd-style)** — the moment PyTorch's `.backward()` stops being magic
- [ ] **3.12** Build a mini deep learning framework from scratch — wrap your autograd
- [ ] **3.13** Debugging neural networks — vanishing gradients, exploding gradients, dead ReLUs
- [ ] **3.14** Intro to PyTorch — rebuild your hand-built net, see exactly what it automates
- [ ] **3.15** Intro to JAX — functional approach, `jit`, `grad` (conceptual awareness)
      → repo: `01` through `13` lessons in `phases/03-deep-learning-core/`

---

## Phase 4 — Neural Net Milestones (language models from scratch)

_The payoff of Phase 3 — real working models, all hand-coded._

- [ ] **4.1** Character-level language model (makemore-style) — bigram model from scratch
- [ ] **4.2** MLP-based language model — context window, embedding table, from scratch
- [ ] **4.3** Tokenization — BPE algorithm coded by hand, build your own tokenizer
- [ ] **4.4** Self-attention mechanism — derive the math (Q, K, V), implement from scratch
- [ ] **4.5** Multi-head attention — extend single-head, implement from scratch
- [ ] **4.6** Positional encoding — sinusoidal, then RoPE — implement both
- [ ] **4.7** Full transformer block — attention + FFN + layer norm, built from scratch
- [ ] **4.8** **Build nanoGPT from scratch** — your own tokenizer, attention, training loop, trained on real text
- [ ] **4.9** BERT-style masked language modeling — encoder-only variant
- [ ] **4.10** Scaling intuition — how bigger models/data/compute interact (Chinchilla laws)
      → repo: `phases/05-nlp-foundations-to-advanced/03-word-embeddings`, `phases/07-transformers-deep-dive/`

---

## Phase 5 — Domain Branches

_Same rule: hand-build the core mechanism on a toy example first, library second._

### 5A — Computer Vision

→ repo: `phases/04-computer-vision/`

- [ ] **5A.1** Image fundamentals — pixels, channels, color spaces, convolution by hand
- [ ] **5A.2** CNNs from scratch — your own convolution code, pooling, stride
- [ ] **5A.3** CNN architectures — LeNet to ResNet, build each layer type
- [ ] **5A.4** Image classification — train a CNN from scratch on MNIST/CIFAR
- [ ] **5A.5** Transfer learning & fine-tuning — use pretrained ResNet/ViT (first framework use in vision)
- [ ] **5A.6** Object detection — YOLO architecture from scratch
- [ ] **5A.7** Semantic segmentation — U-Net from scratch
- [ ] **5A.8** Self-supervised vision — SimCLR, DINO, MAE concepts
- [ ] **5A.9** CLIP — contrastive text-image embeddings, loss derived by hand
- [ ] **5A.10** Vision Transformers (ViT) — patch tokens, built from scratch
- [ ] **5A.11** 3D Vision — NeRF concept + toy implementation, point clouds
- [ ] **5A.12** 3D Gaussian Splatting — from scratch on a simple scene
- [ ] **5A.13** Diffusion Transformers & Rectified Flow — current 2026 architecture
- [ ] **5A.14** OCR & document understanding
- [ ] **5A.15** Build a complete vision pipeline — capstone

### 5B — NLP (pre-transformer foundations)

→ repo: `phases/05-nlp-foundations-to-advanced/`

- [ ] **5B.1** Text processing — tokenization, stemming, lemmatization by hand
- [ ] **5B.2** Bag of words & TF-IDF — coded from scratch
- [ ] **5B.3** Word embeddings — Word2Vec from scratch (skip-gram, CBOW)
- [ ] **5B.4** RNNs & LSTMs — built from scratch, understand vanishing gradient problem
- [ ] **5B.5** Seq2seq models — encoder-decoder for translation
- [ ] **5B.6** Sentiment analysis, NER, POS tagging — classical + neural
- [ ] **5B.7** Text summarization, question answering
- [ ] **5B.8** Information retrieval & search
- [ ] **5B.9** Subword tokenization deep dive — BPE, WordPiece, SentencePiece coded by hand
- [ ] **5B.10** Multilingual NLP
- [ ] **5B.11** Structured outputs & constrained decoding

### 5C — Speech & Audio

→ repo: `phases/06-speech-and-audio/`

- [ ] **5C.1** Audio fundamentals — waveforms, sampling rate, FFT by hand
- [ ] **5C.2** Spectrograms & Mel scale — build from scratch using FFT
- [ ] **5C.3** Audio classification from scratch
- [ ] **5C.4** Speech recognition (ASR) — CTC loss concept, build a basic ASR pipeline
- [ ] **5C.5** Whisper — architecture walkthrough, fine-tune on custom dataset
- [ ] **5C.6** Speaker recognition & verification
- [ ] **5C.7** Text-to-speech (TTS) — architecture, build a basic TTS
- [ ] **5C.8** Voice cloning & conversion
- [ ] **5C.9** Music generation
- [ ] **5C.10** Neural audio codecs — EnCodec, SNAC concepts
- [ ] **5C.11** Real-time audio processing
- [ ] **5C.12** Build a voice assistant pipeline — capstone

### 5D — Generative AI

→ repo: `phases/08-generative-ai/`

- [ ] **5D.1** Generative model taxonomy — VAEs, GANs, diffusion, flow — the big picture
- [ ] **5D.2** Autoencoders & VAE — build from scratch, reparameterisation trick
- [ ] **5D.3** GANs from scratch — generator vs discriminator, training instability
- [ ] **5D.4** Conditional GANs & Pix2Pix
- [ ] **5D.5** DDPM — diffusion forward/reverse process derived by hand, coded from scratch
- [ ] **5D.6** Latent diffusion & Stable Diffusion architecture
- [ ] **5D.7** ControlNet, LoRA & conditioning
- [ ] **5D.8** Flow matching & Rectified Flows — 2025-2026 standard
- [ ] **5D.9** Video generation
- [ ] **5D.10** 3D generation (Tripo-style) — mesh/point cloud diffusion
- [ ] **5D.11** Evaluation — FID, CLIP Score, how to measure generative quality

### 5E — Reinforcement Learning

→ repo: `phases/09-reinforcement-learning/`

- [ ] **5E.1** MDPs, states, actions, rewards — from scratch with toy gridworld
- [ ] **5E.2** Dynamic programming — value iteration, policy iteration
- [ ] **5E.3** Monte Carlo methods
- [ ] **5E.4** Q-Learning & SARSA — coded from scratch on CartPole
- [ ] **5E.5** Deep Q-Networks (DQN) — neural net as Q-function
- [ ] **5E.6** Policy gradients — REINFORCE algorithm from scratch
- [ ] **5E.7** Actor-Critic (A2C/A3C)
- [ ] **5E.8** PPO — the most widely used RL algorithm today
- [ ] **5E.9** Reward modeling & RLHF — how ChatGPT-style training works
- [ ] **5E.10** Multi-agent RL
- [ ] **5E.11** RL for games — capstone

---

## Phase 6 — LLMs from Scratch & Transformers Deep Dive

→ repo: `phases/07-transformers-deep-dive/` + `phases/10-llms-from-scratch/`

- [ ] **6.1** Why transformers replaced RNNs — the quadratic tradeoff
- [ ] **6.2** KV cache, Flash Attention & inference optimization
- [ ] **6.3** Mixture of Experts (MoE) — how modern large models work
- [ ] **6.4** Data pipelines for pre-training — cleaning, tokenizing, shuffling at scale
- [ ] **6.5** Pre-train a mini GPT (124M params) — full training run on real data
- [ ] **6.6** Instruction tuning (SFT) — fine-tune your pre-trained model
- [ ] **6.7** RLHF — reward model + PPO on an LLM
- [ ] **6.8** DPO — Direct Preference Optimization (simpler RLHF alternative)
- [ ] **6.9** Quantization — INT8, GPTQ, AWQ, GGUF — make models smaller
- [ ] **6.10** Distributed training — FSDP, DeepSpeed concepts
- [ ] **6.11** Architecture walkthroughs — Llama, Mistral, DeepSeek-V3, Jamba (SSM-Transformer hybrid)
- [ ] **6.12** Speculative decoding & EAGLE — faster inference
- [ ] **6.13** Differential attention, Native Sparse Attention (DeepSeek NSA) — 2025-2026 advances
- [ ] **6.14** Scaling laws — Chinchilla, compute-optimal training
- [ ] **6.15** LLM evaluation — benchmarks, RAGAS, G-Eval, NIAH

---

## Phase 6.5 — Frontier / Beyond-Transformer (2025-2026 research)

_The field has moved past "transformer = AI" — these are the active directions._

- [ ] **6.5.1** Why transformers hit limits — quadratic attention, fixed context, frozen weights post-training
- [ ] **6.5.2** State-Space Models (Mamba, SSMs) — linear-time alternative to attention, from scratch
- [ ] **6.5.3** Hybrid SSM-Transformer architectures (Jamba-style)
- [ ] **6.5.4** Memory-augmented architectures — Titans, continual learning, catastrophic forgetting
- [ ] **6.5.5** Test-time compute & reasoning models — why "think longer" is a 2025-2026 capability lever
- [ ] **6.5.6** World models — simulate environments, not just predict text
- [ ] **6.5.7** Multi-Token Prediction (MTP) — predict multiple tokens simultaneously
- [ ] **6.5.8** Visual Autoregressive Modeling (VAR) — next-scale prediction

---

## Phase 7 — Multimodal AI

→ repo: `phases/12-multimodal-ai/`

- [ ] **7.1** Vision-Language Models (ViT-MLP-LLM) — BLIP-2, LLaVA architecture
- [ ] **7.2** CLIP contrastive pretraining — loss derived by hand
- [ ] **7.3** Any-resolution vision — Patch-n'-Pack, NaFlex
- [ ] **7.4** Video-language — temporal grounding, long-video at million-token context
- [ ] **7.5** Audio-language models — from Whisper to multimodal
- [ ] **7.6** Omni models — Thinker-Talker streaming (any-to-any)
- [ ] **7.7** Document & diagram understanding, ColPali vision-native RAG
- [ ] **7.8** Multimodal RAG & cross-modal retrieval
- [ ] **7.9** Multimodal agents & computer-use — capstone

---

## Phase 8 — LLM Engineering & RAG

→ repo: `phases/11-llm-engineering/`

- [ ] **8.1** Prompt engineering — techniques, patterns, CoT, Tree-of-Thought
- [ ] **8.2** Embeddings & vector representations — semantic search, vector DBs
- [ ] **8.3** Context engineering — managing context windows effectively
- [ ] **8.4** RAG — Retrieval-Augmented Generation from scratch (no LangChain first)
- [ ] **8.5** Advanced RAG — chunking strategies, reranking, hybrid search
- [ ] **8.6** Fine-tuning with LoRA & QLoRA — your own data, your own model
- [ ] **8.7** Function calling & tool use — how models call external tools
- [ ] **8.8** Structured outputs — constrained generation, JSON modes
- [ ] **8.9** Guardrails & safety — input/output classification, Llama Guard
- [ ] **8.10** Caching, rate limiting & cost control
- [ ] **8.11** Evaluation & testing — build an eval pipeline for your LLM app
- [ ] **8.12** LangGraph — stateful graphs for agents (framework intro, earned by now)
- [ ] **8.13** Build a production LLM app — capstone

---

## Phase 9 — Tools, Protocols & Agent Engineering

→ repo: `phases/13-tools-and-protocols/` + `phases/14-agent-engineering/`

### 9A — MCP & Tool Protocols

- [ ] **9A.1** The tool interface — how models call external tools
- [ ] **9A.2** Function calling deep dive — schema design, parallel calls
- [ ] **9A.3** MCP fundamentals — what it is, why it exists
- [ ] **9A.4** Build an MCP server from scratch
- [ ] **9A.5** Build an MCP client from scratch
- [ ] **9A.6** MCP transports, resources, prompts, sampling
- [ ] **9A.7** MCP security — tool poisoning, OAuth 2.1
- [ ] **9A.8** A2A protocol — agent-to-agent communication
- [ ] **9A.9** OpenTelemetry for GenAI — observability

### 9B — Agent Engineering

- [ ] **9B.1** The agent loop — 120 lines of pure Python, no frameworks
- [ ] **9B.2** ReAct, ReWOO, Plan-and-Execute patterns
- [ ] **9B.3** Reflexion & verbal reinforcement learning
- [ ] **9B.4** Tree of Thoughts & LATS
- [ ] **9B.5** Agent memory — virtual context, MemGPT, Mem0 hybrid memory
- [ ] **9B.6** Skill libraries & lifelong learning (Voyager)
- [ ] **9B.7** Orchestration patterns — supervisor, swarm, hierarchical
- [ ] **9B.8** Multi-agent debate & collaboration
- [ ] **9B.9** Failure modes — why agents break, prompt injection defense
- [ ] **9B.10** Eval-driven agent development
- [ ] **9B.11** Voice agents — Pipecat, LiveKit
- [ ] **9B.12** Agent observability — Langfuse, Phoenix
- [ ] **9B.13** Build a minimal agent workbench — capstone

---

## Phase 10 — Autonomous Systems & Multi-Agent Swarms

→ repo: `phases/15-autonomous-systems/` + `phases/16-multi-agent-and-swarms/`

- [ ] **10.1** Long-horizon agents — METR time horizons
- [ ] **10.2** Self-taught reasoning (STaR, V-STaR, Quiet-STaR)
- [ ] **10.3** Evolutionary coding agents (AlphaEvolve)
- [ ] **10.4** Recursive self-improvement — capability vs alignment
- [ ] **10.5** Durable execution — checkpoints, rollback, kill switches
- [ ] **10.6** Multi-agent coordination — FIPA-ACL, communication protocols
- [ ] **10.7** Swarm architectures — parallel swarm, hierarchical, networked
- [ ] **10.8** Consensus & Byzantine fault tolerance
- [ ] **10.9** MARL — MADDPG, QMIX, MAPPO
- [ ] **10.10** Agent economies, reputation, incentives
- [ ] **10.11** Production scaling — queues, checkpoints, durability
- [ ] **10.12** Failure modes — groupthink, monoculture, decomposition drift

---

## Phase 11 — Infrastructure, Production & Ethics

→ repo: `phases/17-infrastructure-and-production/` + `phases/18-ethics-and-alignment/`

- [ ] **11.1** Model serving — vLLM, ONNX Runtime, FastAPI wrapper
- [ ] **11.2** Experiment tracking — Weights & Biases, MLflow
- [ ] **11.3** Containerisation & cloud deployment — Docker + cloud GPU
- [ ] **11.4** Monitoring & alerting for ML systems
- [ ] **11.5** Cost optimization — batching, caching, quantization in prod
- [ ] **11.6** Constitutional AI & self-improvement — how Anthropic aligns models
- [ ] **11.7** RLHF safety — reward hacking, Goodhart's law
- [ ] **11.8** Responsible scaling policies — Anthropic RSP v3, OpenAI Preparedness Framework
- [ ] **11.9** Societal-scale risk — CAIS, CAISI, existential risk concepts
- [ ] **11.10** Bias, fairness & evaluation in production

---

## Phase 12 — Capstone Projects

→ repo: `phases/19-capstone-projects/`

- [ ] **12.1** Train a small LLM on your own domain data (custom tokenizer, custom dataset, full pipeline)
- [ ] **12.2** Build a multimodal agent (text + image input, tool-using, memory-backed)
- [ ] **12.3** Build a voice assistant pipeline end-to-end
- [ ] **12.4** Fine-tune a vision model for a custom task
- [ ] **12.5** Build and deploy a production RAG app with eval pipeline
- [ ] **12.6** Open-ended: your own AI product (R.I. Studios direction — game AI, 3D gen, business agent)

---

## Tooling Reference (verified June 2026)

| Purpose                                      | Tool                                  |
| -------------------------------------------- | ------------------------------------- |
| Primary framework (learned after hand-build) | PyTorch                               |
| Pre-trained models / fine-tuning             | Hugging Face Transformers + Diffusers |
| Classical ML                                 | scikit-learn                          |
| Agent / RAG frameworks                       | LangChain, LangGraph, LlamaIndex      |
| LLM serving                                  | vLLM, ONNX Runtime                    |
| Experiment tracking                          | Weights & Biases, MLflow              |
| Containerisation                             | Docker                                |
| IDE                                          | VS Code (Python + Jupyter extensions) |
| Second-pass reference                        | rohitg00/ai-engineering-from-scratch  |

---

## Progress Log

- **2026-06-19**: Curriculum created. Starting point confirmed zero across math and ML.
- **2026-06-19**: Cross-verified against current (June 2026) research. Added frontier topics, tooling reference.
- **2026-06-19**: Clarified "from scratch" philosophy. Phase 3 includes own autograd engine.
- **2026-06-19**: Full merge with rohitg00/ai-engineering-from-scratch (503 lessons, 20 phases). Repo cross-references added per topic throughout. All missing topics incorporated: information theory, Fourier, graph theory, SVMs, KNN, anomaly detection, time series, Word2Vec, RNNs, GANs, VAEs, voice cloning, MCP deep dive (23 lessons), agent engineering (42 lessons), autonomous systems, multi-agent swarms, ethics/alignment, capstone projects.
- **2026-07-04**: Phase 0 complete — all 8 setup lessons done. Environment solid: Python 3.14.3, venv, numpy 2.5.0, matplotlib 3.11.0, jupyter, VS Code configured, RTX 2060 GPU confirmed (CUDA 13.2), Docker and data management understood conceptually, debugging/profiling tools covered. Starting Phase 1 (Math Foundations) next session.
- **2026-07-04**: 1.1.1 done — variables, expressions, solving linear equations for x. Learner solved 3/3 practice problems correctly, verified conceptually.
- **2026-07-04**: 1.1.2 done — functions, f(x) notation, domain/range. Coded g(x)=1/x and h(x)=x²-4 in Python (`phase1-math/1_1_functions.py`), correctly predicted ZeroDivisionError for g(0) before running, correctly identified both roots of h(x). First encounter with reading a Python traceback.
- **2026-07-04**: 1.1.3 done — slope/intercept, y=mx+b. Coded `line()` and `slope()` in `phase1-math/1_3_slope.py`, generated table for m=2,b=3, verified slope=2 using non-adjacent points (extra rigor beyond what was asked), tested negative slope (m=-5,b=5) and confirmed decreasing y. Correctly predicted m=0 gives a horizontal line at y=b.
- **2026-07-04**: 1.1.4 done — exponents and logarithms. Coded `phase1-math/1_1_4_logs.py`, verified log2(16)=4, log10(100)=2, log(1)=0, and confirmed 2**10=1024 inverts to log2(1024)=10.0. Correctly predicted math.log(0) would raise an error; ran it and got ValueError: expected a positive input (Python 3.14's updated wording for the classic "math domain error"). Correctly reasoned that log(0) is undefined because a positive base raised to any real exponent is always >0, never reaching exactly 0. **Section 1.1 (Algebra) fully complete\*\* — moving to 1.2 (Calculus) next session. Also corrected: repo cross-references for all of 1.1 were wrong (see notes) — no confirmed matching lesson found yet for basic algebra topics in rohitg00/ai-engineering-from-scratch; will check catalog.html as needed rather than guess.
- **2026-07-04**: 1.2.1 done — derivatives as local slope, numeric intuition. Coded `numeric_derivative()` in `phase1-math/2_1_derivative.py`, computed derivative of x² at x=3,0,-2, discovered the 2x pattern from the numbers directly. Explored h shrinking (0.0001 → more accurate at 1e-8) and was introduced to catastrophic cancellation as the reason accuracy degrades if h shrinks too far (ties to 1.3.12 numerical stability, upcoming). Correctly reasoned that a line's derivative equals its constant slope (2 for f(x)=2x+3, 0 for f(x)=5) by connecting back to 1.1.3's slope concept, after an initial miss (confused "derivative" with "solve for x").
- **2026-07-04**: 1.2.2 done — power rule and chain rule, worked by hand and verified numerically. Coded `phase1-math/1_2_2_rules.py`; generalized power rule to any n (not just the x³ example given), verified against numeric_derivative for x³ at x=3 (27 vs 27.0009) and chain rule on (2x+3)² at x=3 (36 vs 36.0004). Correctly predicted derivative of x¹ is 1 by applying the rule mechanically, connected to 1.1.3 (slope of f(x)=x is 1).

---

## Lesson Notes

Detailed notes live in `notes/` folder, one file per phase. Append after each completed topic.
First entry will appear in `notes/phase0-setup.md` after Lesson 0.1.
