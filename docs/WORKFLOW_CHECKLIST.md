# Development Workflow Checklist

## Starting Work

- [ ] Pull latest `develop` branch
- [ ] Create a new branch with proper naming (feature/bugfix/release)
- [ ] Set up local environment properly

## During Development

- [ ] Follow code style guidelines
- [ ] Write tests for new code
- [ ] Make frequent, small commits with clear messages
- [ ] Keep branch updated with `develop` (rebase regularly)
- [ ] Document new features/APIs
- [ ] Clean up temporary files regularly

## Before Committing

- [ ] Run linting tools (auto-run by pre-commit)
- [ ] Run unit tests
- [ ] Check for hardcoded secrets or credentials
- [ ] Verify no unnecessary files are being committed

## Before Pull Request

- [ ] Run the full test suite
- [ ] Clean up the repository (`./scripts/clean.ps1`)
- [ ] Update documentation if needed
- [ ] Make sure branch is up to date with develop
- [ ] Self-review the changes in GitHub

## Release Process

- [ ] Create release branch from develop
- [ ] Update version numbers and CHANGELOG.md
- [ ] Perform final testing
- [ ] Merge to main with a tag
- [ ] Merge back to develop
