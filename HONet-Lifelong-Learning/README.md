# HONet: A Composable Architecture for Lifelong Learning

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![PyTorch](https://img.shields.io/badge/PyTorch-1.10+-ee4c2c.svg)
[![arXiv](https://img.shields.io/badge/arXiv-2310.XXXXX-b31b1b.svg)](https://arxiv.org/abs/2310.XXXXX)

This repository contains the official PyTorch implementation and benchmarks for **HONet (Hierarchical Octave Network)**, a novel architecture that enables AI models to learn new skills sequentially **without catastrophic forgetting**.

## Core Concept: AI Without Amnesia

HONet solves the "plasticity-stability dilemma" by treating learned skills as immutable, foundational layers. Its process combines the perfect memory of architectural methods with a practical, linear `O(N)` scaling law, making it ideal for building truly adaptive AI systems.

---

## Strong Evidence of Capabilities

We validated HONet on the challenging **Split CIFAR-10 benchmark**, where it sequentially learned 5 distinct tasks.

### 1. Definitive Proof of Zero Forgetting

A standard model that is finetuned catastrophically forgets prior knowledge. In contrast, HONet's performance on Task 1 remains perfect after learning all subsequent tasks.

![Perfect Recall Proof](./example_outputs/proof_perfect_recall.png)
*Figure 1: Side-by-side reconstruction of Task 1 images. Left: A naive model after finetuning on Task 2 shows complete forgetting. Right: HONet's reconstruction is perfect after learning all 5 tasks.*

### 2. Consistent Performance Across All Tasks

By implementing a robust functional distiller, HONet effectively transfers knowledge and learns new, complex tasks without performance degradation.

| Task | Final HONet Reconstruction Loss |
| :--- | :--- |
| **Task 1 (Classes 0-1)** | **508.55** |
| **Task 2 (Classes 2-3)** | **547.27** |
| **Task 3 (Classes 4-5)** | **536.85** |
| **Task 4 (Classes 6-7)** | **573.18** |
| **Task 5 (Classes 8-9)** | **494.17** |
*Table 1: Final reconstruction loss on the test set for each task, showing consistently strong performance.*

---

## Getting Started

### 1. Setup Environment
Clone this repository and install the required packages.
```bash
git clone https://github.com/anuragdongare1/HONet-Lifelong-Learning.git
cd HONet-Lifelong-Learning
pip install -r requirements.txt