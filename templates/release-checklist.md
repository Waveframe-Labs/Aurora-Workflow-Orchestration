# AWO Release Checklist

This checklist ensures that each release of Aurora Workflow Orchestration (AWO) meets governance standards defined in ADR-0010.

## Pre-Release

- [ ] All code validated against schemas (`run_manifest`, `provenance`, `claim`).
- [ ] Latest run passes audit gates (scope + human approval).
- [ ] ADRs up to date and numbered sequentially.
- [ ] Logs/decisions folder contains rationale for major changes.
- [ ] Whitepaper in `docs/` updated with version bump.

## Release

- [ ] Tag the release with semantic version (e.g., `v1.1.0`).
- [ ] Update `README.md` with release highlights.
- [ ] Upload artifacts to Zenodo (or archive service) to mint DOI.
- [ ] Update DOI badge in README and whitepaper.
- [ ] Verify `CITATION.cff` matches new version + DOI.

## Post-Release

- [ ] Announce release in project communication channels.
- [ ] Record the release decision in `/logs/decisions/` with timestamp.
- [ ] Archive older release branch if deprecated.

---

✅ If every box is checked, the release is compliant with ADR-0010.
