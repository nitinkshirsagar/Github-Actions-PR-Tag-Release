# Changelog

## 0.1.4

- Modifications on Release workflow:
  - Allow running Release workflow without publishing release
  - Checkout the specific detected tag
  - Allow specifying custom ref to checkout
  - Internal change: set input version to env instead of exporting to file and reading

## 0.1.3

- Add workflow dispatch on Release workflow

## 0.1.2

- Use "Tag on PR merge" external action on Tag workflow

## 0.1.1

- Write workflow-generated files on /tmp

## 0.0.5

- Fix extract_tag_from_pr detection of "Tags" prefix
- Fix extract_changelog script for new Changelog file format

## 0.0.3

- Fix wrong Python requirements filename in Release workflow

## 0.0.2

- Fix wrong branch name in Tag workflow

## 0.0.1

- Add file1.txt
