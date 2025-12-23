# async-exception-semantics
A case study on exception visibility gaps in Python async systems
Silent Failures: Exception Semantics in Asynchronous Transaction Systems

This repository documents a real failure mode observed in high-throughput
asynchronous transaction systems using Python's asyncio runtime.

The case study examines how exceptions raised in fire-and-forget async tasks
can become invisible to the spawning context, leading to violations of
system-level correctness invariants in production systems.

## Overview

- Domain: Distributed systems, async runtimes, system reliability
- Language: Python (asyncio)
- Focus: Semantic gap between developer mental models and runtime guarantees

## Contents

- `reproduction.py` — Minimal, deterministic reproduction of the failure
- `case-study.md` — Technical analysis and system-level implications
- `notes.md` — References to Python documentation and PEPs

## Why This Matters

This is not a bug in application code.
It is a consequence of underspecified exception observability semantics
in asynchronous runtimes.

The failure mode:
- Passes code review
- Survives integration testing
- Manifests only under production concurrency patterns

## Status

This repository is intentionally minimal.
It is designed for clarity and reproducibility, not popularity.
