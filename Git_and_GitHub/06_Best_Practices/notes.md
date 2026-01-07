# Best Practices - Comprehensive Notes ✨

## Introduction to Git Best Practices

Best practices transform Git from a tool you use into a professional workflow that makes your team more productive, your code more maintainable, and your history more meaningful.

### Why Best Practices Matter

- **Team Harmony**: Everyone follows same conventions
- **Readable History**: Understand changes months/years later
- **Easier Debugging**: Find when bugs were introduced
- **Professional Growth**: Industry-standard practices
- **Automation**: CI/CD integration works smoothly
- **Onboarding**: New team members adapt quickly

---

## Commit Message Conventions

### The 7 Rules of Great Commit Messages

1. **Separate subject from body with blank line**
2. **Limit subject line to 50 characters**
3. **Capitalize the subject line**
4. **Do not end subject with period**
5. **Use imperative mood** ("Add feature" not "Added feature")
6. **Wrap body at 72 characters**
7. **Use body to explain what and why, not how**

### Commit Message Template

```
Short summary (50 chars or less)

More detailed explanatory text if needed. Wrap it to 72 characters.
Explain the problem this commit solves. Focus on why you made the
change rather than how you made it (the code explains the how).

- Bullet points are okay
- Use a hyphen or asterisk with space

Resolves: #123
See also: #456, #789
```

### Conventional Commits

**Format**: `<type>(<scope>): <subject>`

**Types**:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation only
- `style`: Formatting, no code change
- `refactor`: Code change that neither fixes bug nor adds feature
- `perf`: Performance improvement
- `test`: Adding or updating tests
- `chore`: Maintenance tasks
- `ci`: CI/CD changes

**Examples**:
```bash
feat(auth): Add OAuth2 login support
fix(api): Handle null response in user endpoint
docs(readme): Update installation instructions
style(css): Format navigation styles
refactor(database): Optimize query performance
test(auth): Add unit tests for login flow
chore(deps): Update dependencies to latest
ci(github): Add automated testing workflow
```

### Good vs Bad Commit Messages

**❌ Bad messages**:
```
Update
Fix stuff
asdfasdf
WIP
Changes
Fix bug
Update file.js
```

**✅ Good messages**:
```
Add user authentication with JWT
Fix login redirect after password reset
Update README with Docker setup instructions
Refactor database connection to use pool
Remove deprecated API endpoints
```

---

## Branch Naming Conventions

### Standard Prefixes

```
feature/    - New features
feat/       - New features (shorter)
bugfix/     - Bug fixes
fix/        - Bug fixes (shorter)
hotfix/     - Urgent production fixes
release/    - Release preparation
docs/       - Documentation
test/       - Testing improvements
refactor/   - Code refactoring
chore/      - Maintenance tasks
```

### Naming Patterns

**Good patterns**:
```
feature/user-authentication
feature/add-payment-gateway
bugfix/fix-login-redirect
bugfix/navbar-mobile-responsive
hotfix/security-vulnerability-123
release/v2.0.0
docs/api-documentation
test/unit-tests-for-auth
refactor/optimize-database-queries
```

**Best practices**:
- Lowercase with hyphens (kebab-case)
- Be descriptive but concise
- Include issue number if applicable
- Avoid generic names

**❌ Bad names**:
```
test            # Too vague
johns_branch    # About person, not feature
bug             # Not specific
temp            # Not descriptive
fix             # What fix?
my-branch       # Not about the work
```

---

## Git Workflows

### GitHub Flow (Recommended for Most Teams)

**Simple, continuous deployment workflow**:

```
1. main branch is always deployable
2. Create descriptive feature branch from main
3. Commit to that branch locally and push regularly
4. Open Pull Request when ready
5. Discuss and review code
6. Deploy and test from branch (optional)
7. Merge to main after approval
8. Deploy main immediately
```

**Advantages**:
- ✅ Simple to understand
- ✅ Great for continuous deployment
- ✅ Works well with CI/CD
- ✅ Fast iteration

**When to use**: Web applications, APIs, continuous deployment

### Git Flow

**Structured workflow with multiple long-lived branches**:

**Branches**:
- `main`: Production code (tagged releases)
- `develop`: Integration branch for next release
- `feature/*`: New features (from develop)
- `release/*`: Release preparation (from develop)
- `hotfix/*`: Urgent fixes (from main)

**Workflow**:
```
1. Feature development:
   develop → feature/new-feature → develop

2. Release preparation:
   develop → release/v1.0 → main + develop

3. Hotfix:
   main → hotfix/bug → main + develop
```

**Advantages**:
- ✅ Structured releases
- ✅ Multiple versions in production
- ✅ Clear separation of concerns

**When to use**: Scheduled releases, desktop apps, multiple production versions

### Trunk-Based Development

**Everyone commits to main (trunk) frequently**:

```
main ──────────────────────────
      \  /\  /\  /
       feat feat feat
```

**Rules**:
- Short-lived feature branches (hours/days, not weeks)
- Feature flags for incomplete work
- Very frequent integration
- Strong CI/CD required

**When to use**: Large teams, Google/Facebook scale, high maturity

---

## .gitignore Best Practices

### Essential Ignores

```gitignore
# Dependencies
node_modules/
venv/
vendor/
*.gem

# Environment variables (CRITICAL!)
.env
.env.local
.env.*.local
*.key
*.pem
secrets.yml

# Build outputs
dist/
build/
out/
target/
*.war
*.jar

# Logs
*.log
logs/
npm-debug.log*

# IDE / Editor
.vscode/
.idea/
*.swp
*.swo
*~
.DS_Store

# OS files
Thumbs.db
.DS_Store

# Test coverage
coverage/
.nyc_output/

# Temporary files
*.tmp
*.temp
.cache/
```

### Security: Never Commit

**❌ NEVER commit**:
```gitignore
# Secrets
.env
*.key
*.pem
secrets.*
credentials.*

# API keys
*api-key*
*secret-key*

# Certificates
*.crt
*.cer

# Passwords
*password*
```

### Use GitHub Templates

When creating repository, GitHub offers templates for:
- Python
- Node.js
- Java
- Ruby
- Go
- And many more

---

## Repository Structure

### Organized Repository

```
my-project/
├── .github/
│   ├── workflows/        # GitHub Actions
│   ├── ISSUE_TEMPLATE/   # Issue templates
│   └── PULL_REQUEST_TEMPLATE.md
├── docs/                 # Documentation
├── src/                  # Source code
│   ├── components/
│   ├── utils/
│   └── index.js
├── tests/                # Tests
├── .gitignore
├── .env.example          # Example environment
├── README.md
├── LICENSE
├── CONTRIBUTING.md
└── package.json
```

### Essential Files

**README.md**:
```markdown
# Project Name
Brief description

## Features
- Feature 1
- Feature 2

## Installation
\`\`\`bash
npm install
\`\`\`

## Usage
\`\`\`javascript
const app = require('./app');
\`\`\`

## Contributing
See CONTRIBUTING.md

## License
MIT
```

**CONTRIBUTING.md**:
```markdown
# Contributing

## How to Contribute
1. Fork repository
2. Create feature branch
3. Commit changes
4. Push to fork
5. Create Pull Request

## Code Style
- Use ESLint
- Follow existing patterns

## Running Tests
\`\`\`bash
npm test
\`\`\`
```

**LICENSE**:
- Choose appropriate license (MIT, Apache 2.0, GPL)
- Add via GitHub interface or manually

---

## Git Hooks

### What are Git Hooks?

Scripts that run automatically on Git events (pre-commit, pre-push, etc.).

### Common Hooks

**Pre-commit** (runs before commit):
```bash
#!/bin/sh
# .git/hooks/pre-commit

# Run linter
npm run lint || exit 1

# Run tests
npm test || exit 1

echo "Pre-commit checks passed ✓"
```

**Pre-push** (runs before push):
```bash
#!/bin/sh
# .git/hooks/pre-push

# Run tests
npm test || exit 1

echo "Pre-push checks passed ✓"
```

**Commit-msg** (validate commit message):
```bash
#!/bin/sh
# .git/hooks/commit-msg

commit_msg=$(cat "$1")

# Check conventional commit format
if ! echo "$commit_msg" | grep -qE "^(feat|fix|docs|style|refactor|test|chore)(\(.+\))?: .+"; then
    echo "Error: Commit message must follow conventional commits format"
    echo "Example: feat(auth): Add login functionality"
    exit 1
fi
```

### Using Husky (Easier Hook Management)

```bash
# Install husky
npm install --save-dev husky

# Initialize
npx husky install

# Add pre-commit hook
npx husky add .husky/pre-commit "npm test"
```

---

## Code Review Best Practices

### For Authors

**Before requesting review**:
- [ ] Code is tested
- [ ] Lint/format passing
- [ ] Self-review completed
- [ ] PR description is clear
- [ ] Related issues linked
- [ ] Screenshots added (if UI)

**Small PRs**:
- Aim for < 400 lines
- One feature/fix per PR
- Easy to review = faster merges

### For Reviewers

**Be constructive**:
```
✅ "Consider using a switch statement here for better readability"
✅ "Great error handling! One suggestion: we could also log the error"
✅ "This works, but have we considered edge case X?"

❌ "This is wrong"
❌ "Why did you do it this way?"
❌ "I don't like this"
```

**Focus on**:
- Logic errors
- Security issues
- Performance problems
- Missing edge cases
- API design

**Don't nitpick**:
- Code style (use automated tools)
- Personal preferences
- Micro-optimizations

---

## Collaboration Best Practices

### Pull Request Etiquette

**Creating PRs**:
- Clear, descriptive title
- Detailed description
- Link related issues
- Add screenshots for UI
- Request specific reviewers
- Keep it small!

**Responding to feedback**:
- Address all comments
- Ask questions if unclear
- Don't take it personally
- Thank reviewers
- Resolve conversations when addressed

### Issue Management

**Writing good issues**:
```markdown
## Bug Report

**Description**
Clear description of the problem

**Steps to Reproduce**
1. Go to...
2. Click on...
3. See error

**Expected Behavior**
What should happen

**Actual Behavior**
What actually happens

**Environment**
- OS: macOS 12.1
- Browser: Chrome 98
- Version: 2.0.0

**Screenshots**
[If applicable]
```

---

## Security Best Practices

### Never Commit Secrets

**Use environment variables**:
```javascript
// ❌ DON'T DO THIS
const API_KEY = "sk_live_abc123xyz";

// ✅ DO THIS
const API_KEY = process.env.API_KEY;
```

**.env file** (in .gitignore):
```
API_KEY=sk_live_abc123xyz
DATABASE_URL=postgres://localhost/mydb
```

**.env.example** (committed to repo):
```
API_KEY=your_api_key_here
DATABASE_URL=your_database_url_here
```

### Audit Your History

**Check for secrets**:
```bash
# Search for potential secrets
git log -p | grep -i "password\|api_key\|secret"
```

**If you committed secrets**:
1. Rotate/revoke the secrets immediately
2. Remove from history (complex, may need help)
3. Use tools like `git-secrets` or `truffleHog`

---

## Performance Best Practices

### Keep Repository Clean

**Remove large files**:
```bash
# Find large files
git rev-list --objects --all | \
  git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' | \
  awk '/^blob/ {print substr($0,6)}' | \
  sort --numeric-sort --key=2 | \
  tail -10
```

**Use Git LFS for large files**:
```bash
# Install Git LFS
git lfs install

# Track large files
git lfs track "*.psd"
git lfs track "*.mp4"
```

### Shallow Clones

**For CI/CD** (don't need full history):
```bash
git clone --depth 1 https://github.com/user/repo.git
```

---

## Team Conventions

### Team Agreement Template

```markdown
# Git Conventions

## Branches
- main: Production
- develop: Integration
- feature/*: New features
- bugfix/*: Bug fixes
- hotfix/*: Urgent fixes

## Commits
- Follow Conventional Commits
- Max 50 chars for subject
- Use imperative mood

## Pull Requests
- Keep under 400 lines
- Require 2 approvals
- All checks must pass
- Delete branch after merge

## Code Review
- Review within 24 hours
- Be constructive and kind
- Test locally if needed
```

---

## Automation with CI/CD

### GitHub Actions Example

```yaml
# .github/workflows/test.yml
name: Test

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Setup Node
      uses: actions/setup-node@v2
      with:
        node-version: '16'
    
    - name: Install dependencies
      run: npm install
    
    - name: Run linter
      run: npm run lint
    
    - name: Run tests
      run: npm test
```

---

## Key Takeaways

✅ **Commit messages** should be clear, consistent, and follow conventions

✅ **Branch names** should be descriptive with standard prefixes

✅ **Choose a workflow** that fits your team and product

✅ **.gitignore** prevents committing unwanted files and secrets

✅ **Git hooks** automate quality checks

✅ **Small PRs** are easier to review and merge

✅ **Never commit secrets** - use environment variables

✅ **Code review** improves quality and shares knowledge

✅ **Documentation** (README, CONTRIBUTING) helps onboarding

✅ **Automation** (CI/CD) catches issues early

---

**Happy Professional Git Usage!** ✨

*"The best way to predict the future is to create it." - Build great software with great practices!*
