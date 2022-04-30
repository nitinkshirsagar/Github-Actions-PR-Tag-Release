# Github-Actions-PR-Tag-Release

Example repository with GitHub Actions Workflows that create a new version tag when a Release PR is merged, and create a new release from it.

## How it works

- Our repository uses main-develop branching:
  - New features, fixes and other incorporations are commited to the develop branch.
  - When a new version is ready to be released, a "develop to main" Pull Request must be created, whose description contains a line like "Tags x.y.z", being "x.y.z" the new version that will be released.
- Merging a pull request triggers the ["Tag" Workflow](.github/workflows/tag.yaml) which analyzes the closed-merged PR and, if it contains the described line in the PR description,
  extracts the version specified and creates a new tag on the repository, over the merge commit.
  The ["Tag on PR merge" Action](https://github.com/David-Lor/action-tag-on-pr-merge/actions) is used for detecting and pushing the new tag.
- Creating a new tag triggers the ["Release" Workflow](.github/workflows/release.yaml) which generates a new Release on the Repository. This second Workflow could also be used for building and publishing packages, Docker images, and so on.
