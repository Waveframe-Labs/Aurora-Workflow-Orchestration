# Release Checklist

1) Update docs
   - [ ] README links
   - [ ] CHANGELOG.md
   - [ ] /docs/FALSIFIABILITY_MANIFEST.md
   - [ ] /decisions/ (new ADRs)

2) Update metadata
   - [ ] CITATION.cff (version/date/DOI if known)
   - [ ] .zenodo.json (description/keywords)

3) Evidence
   - [ ] Save figures/notebooks/data and link in logs/manifest
   - [ ] Verify reproducible steps in notebooks or scripts

4) Tag & archive
   - [ ] Create tag (semver)
   - [ ] Publish GitHub release with notes
   - [ ] Confirm Zenodo concept+version DOIs
