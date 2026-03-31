# Sampling Protocol

This repository uses a small BIPIA-inspired subset rather than the full benchmark.

The subset contains:
- 24 attack examples
- 12 benign controls

The examples vary across:
- application task
- attack type
- attack position in the external content

Tasks include summarization, question answering over documents, email and PDF summarization, translation, note rewriting, and support-ticket summarization.

Attack types include:
- direct instruction override
- data exfiltration
- authority claim / role hijacking
- obfuscated leakage
- boundary confusion
- debug-pretext attacks

Attack positions include:
- prefix
- middle
- suffix

The subset is intended for a small-scale reproduction study, not for full benchmark replication.
