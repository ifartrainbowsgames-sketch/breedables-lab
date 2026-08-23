# Promotion rules

A tool enters `tools/approved/` only after **all** of the following:

1. License and dependency review **recorded** in the registry and/or a research report
2. Reproducible setup **documented** on this wiki
3. A concrete Breedables Studio **experiment completed** (see [experiments](experiments.md))
4. Output **artifact saved** in the repo or linked storage with provenance
5. Measured result **documented**
6. Explicit **PASS** decision by a human reviewer

## Not sufficient for approval

- A compelling demo video
- GitHub star count
- AI hype or blog posts without measured studio evidence

## Librarian status flow

Typical path:

```
DISCOVERED → REVIEWING → EXPERIMENTAL → USE_NOW / APPROVED
```

Discovery commands (`discover-github`, `ingest-feed`) deliberately store candidates as `DISCOVERED` with `UNKNOWN` commercial type until curated evidence exists.

## Related

- [Decision model](decision-model.md)
- [Tool registry](tools/index.md)
- [Phase 0 survey](../research/phase-0-survey.md)
