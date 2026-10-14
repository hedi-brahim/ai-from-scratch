# AI From Scratch

A long-term personal project to understand modern AI by building it:
neural networks and small language models from scratch, reproduced and
original experiments, and an autonomous coding agent evaluated on real tasks.

The goal is understanding, not competing with frontier models. Every phase
ends with working code, measured results, and a short write-up.

## Tracks

- **Model track:** backpropagation, tokenization, transformers, training a
  small GPT-style model, reproducing a published experiment.
- **Agent track:** a coding agent built on an existing model, with tools,
  a sandbox, and an evaluation harness to measure every change.

## Structure

| Folder          | Contents                                     |
| --------------- | -------------------------------------------- |
| `01-micrograd/` | Scalar autograd engine and a tiny neural net |
| `notes/`        | Study notes and write-ups                    |
| `log.md`        | Weekly progress log                          |

More folders are added as each phase starts.

## Setup

    python -m venv .venv
    source .venv/bin/activate      # Windows: .venv\Scripts\activate
    pip install -r requirements.txt
    python check_setup.py

## Progress

- [x] Phase 0: workspace setup
- [ ] Phase 1: foundations (micrograd, makemore)
- [ ] Phase 2: small language model
- [ ] Phase 3: reproduce a paper
- [ ] Agent baseline and eval set

## Resources

- [Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html), Andrej Karpathy
- [PyTorch tutorials](https://docs.pytorch.org/tutorials/)
- [Stanford CS336: Language Modeling from Scratch](https://cs336.stanford.edu/)