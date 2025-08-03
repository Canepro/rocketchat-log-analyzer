# Contribution Guidelines

## Branch Strategy and Git Workflow

We follow a modified GitFlow workflow:

### Main Branches
- `main`: Production-ready code, always stable
- `develop`: Integration branch for features, relatively stable

### Supporting Branches
- `feature/XXX-description`: New features (XXX = issue number)
- `bugfix/XXX-description`: Bug fixes
- `release/vX.Y.Z`: Release preparation
- `hotfix/XXX-description`: Urgent production fixes

## Workflow Steps

### Starting New Work

1. **Always start from the latest develop branch:**
   ```bash
   git checkout develop
   git pull origin develop
   ```

2. **Create a new branch:**
   - For features:
     ```bash
     git checkout -b feature/123-add-charts
     ```
   - For bug fixes:
     ```bash
     git checkout -b bugfix/124-fix-upload
     ```

### Daily Work

1. **Make frequent commits with clear messages:**
   ```bash
   git commit -m "Add timeline chart component"
   ```

2. **Keep your branch updated with develop:**
   ```bash
   git checkout develop
   git pull origin develop
   git checkout your-branch
   git rebase develop
   ```

### Completing Work

1. **Ensure tests pass:**
   ```bash
   pytest tests/     # Backend tests
   ```

2. **Clean up unnecessary files:**
   ```bash
   ./scripts/clean.ps1
   ```

3. **Create a pull request to the develop branch**
   - Include issue number in title
   - Add a clear description
   - Request code review

### Releases

1. **Create a release branch:**
   ```bash
   git checkout develop
   git checkout -b release/v2.2.0
   ```

2. **Bump version numbers:**
   - Update version in app.py
   - Update CHANGELOG.md

3. **Merge to main and tag:**
   ```bash
   git checkout main
   git merge --no-ff release/v2.2.0
   git tag -a v2.2.0 -m "Version 2.2.0"
   git push origin main --tags
   ```

4. **Merge back to develop:**
   ```bash
   git checkout develop
   git merge --no-ff release/v2.2.0
   git push origin develop
   ```

## Code Standards

### Python
- Follow PEP 8 style guide
- Use type hints
- Document functions with docstrings
- Maximum line length: 100 characters

### JavaScript/TypeScript
- Use ESLint and Prettier
- Use TypeScript for type safety
- Use functional components with hooks in React
- Follow shadcn/ui component patterns

## Pull Request Checklist

Before submitting a PR, ensure:

- [ ] Code follows project style guidelines
- [ ] All tests pass
- [ ] New code has appropriate tests
- [ ] Documentation is updated
- [ ] No unnecessary files are included
- [ ] No secrets or sensitive data is committed
