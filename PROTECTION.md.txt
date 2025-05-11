# Branch Protection Rules Justification

Applying branch protection rules on the `main` branch is essential for maintaining code integrity and supporting collaborative development. The following measures help achieve that:

-  **Require pull request reviews**: This ensures that all code changes are reviewed and approved by team members before being merged, which improves code quality and reduces bugs.
-  **Require status checks to pass**: This guarantees that automated tests and checks run successfully before any code can be merged into `main`, helping to avoid introducing broken or unstable code.
-  **Direct pushes not disabled**: While not currently enforced, disabling direct pushes is recommended in team environments to prevent unreviewed changes from entering the main branch.

## Screeshot for rules
- ![Project Screenshot](![Screenshot (118)](https://github.com/user-attachments/assets/82d3a24b-2eca-4cf6-a4ba-637a9f7ebeb5))
