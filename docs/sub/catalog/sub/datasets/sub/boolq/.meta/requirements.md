# Documentation Requirements

## Requirements

- Identify BoolQ as the 2019 Google Research natural yes/no question-answering dataset. It contains 15,942 examples according to the pinned README, with question, passage and answer Boolean fields; optional title is evidence metadata.
- The original release provides separate JSONL files/splits for train, dev and test; do not conflate them or treat them as separate benchmark identities. Test labels and evaluation protocols can differ from visible development data.
- The README states the dataset is released under **Creative Commons Attribution-ShareAlike 3.0** (CC BY-SA 3.0); no root LICENSE file was found in this pinned repository snapshot. This source declaration does not automatically override third-party rights in copied passages.
- Questions are naturally occurring rather than written to fit a fixed answer template; changing passage truncation, tokenization, retrieval context, prompt or answer parsing can materially change measured performance.
- Original public questions and passages can leak into pretraining. Record a dataset split/revision and keep test sets out of model training and tuning where feasible.
- The publisher repository is archived at the verified revision. No model testing, data rights audit, data download or whole-catalog clean pass was performed.

## Validation

- One canonical dataset identity, pinned upstream publisher sources and a resolvable index link.
- Keep distinct code/data/right boundaries; no runtime, security, complete citation audit or clean-group gate is inferred.
