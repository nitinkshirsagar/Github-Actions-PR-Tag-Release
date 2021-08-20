# Github-Actions-PR-Tag-Release

Example repository with Github Actions that create a tag when a Release PR is merged, and generate a release from it.

The detailed workflow is the following:

- Our repository use main-develop branching.
- New features, fixes and other incorporations are commited to the develop branch.
- When a new version is ready to be released, a develop to main Pull Request is created, which description contains a line "Tags x.y.z", being "x.y.z" a version.
- Merging a pull request triggers a Github Actions Workflow that analyzes the closed-merged PR and, if it contains the described line in its description, extracts the version specified and creates a new tag on the repository, on the merge commit.
- Creating a new tag triggers another Workflow that generates a new Release on the Repository. This second Workflow could also build and publish packages, Docker images, and so on.
