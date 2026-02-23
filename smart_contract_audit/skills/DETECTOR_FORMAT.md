# Detector Skill Format (Fixed)

All detector skills in `detector/` must follow this exact section order:

1. Frontmatter
2. `# <Detector Name>`
3. One-line usage statement
4. `## Detection Targets`
5. `## Workflow`
6. `## Remediation Patterns`

## Required Rules

1. Do not include:
   - False positive filter section
   - Severity section
   - Output format section
2. Keep detector logic focused on:
   - What to detect
   - How to detect
   - How to fix
3. Use concise, implementation-oriented bullets.

## Minimal Skeleton

```md
---
name: <detector-name>
description: <what this detector finds>
---

# <Detector Name>

Use this skill when auditing <scope>.

## Detection Targets

1. ...
2. ...

## Workflow

1. ...
2. ...

## Remediation Patterns

1. ...
2. ...
```

