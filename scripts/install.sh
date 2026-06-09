#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
SOURCE_SKILLS="$REPO_ROOT/skills"

REQUIRED_SKILLS=(
  "nontechnical-codex-project-controller"
  "nontechnical-project-readiness-auditor"
)

DRY_RUN=0
TARGET_PATH="${CODEX_SKILLS_DIR:-}"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --dry-run)
      DRY_RUN=1
      shift
      ;;
    --target)
      if [[ $# -lt 2 ]]; then
        echo "--target requires a path" >&2
        exit 1
      fi
      TARGET_PATH="$2"
      shift 2
      ;;
    *)
      TARGET_PATH="$1"
      shift
      ;;
  esac
done

if [[ -z "$TARGET_PATH" ]]; then
  if [[ -d "$HOME/.agents/skills" ]]; then
    TARGET_PATH="$HOME/.agents/skills"
  elif [[ -d "$HOME/.codex/skills" ]]; then
    TARGET_PATH="$HOME/.codex/skills"
  else
    TARGET_PATH="$HOME/.agents/skills"
  fi
fi

for skill in "${REQUIRED_SKILLS[@]}"; do
  if [[ ! -f "$SOURCE_SKILLS/$skill/SKILL.md" ]]; then
    echo "Missing required file: $SOURCE_SKILLS/$skill/SKILL.md" >&2
    exit 1
  fi

  if [[ ! -f "$SOURCE_SKILLS/$skill/agents/openai.yaml" ]]; then
    echo "Missing required file: $SOURCE_SKILLS/$skill/agents/openai.yaml" >&2
    exit 1
  fi
done

echo ""
echo "Codex for Humans install plan"
echo "Target Skills folder: $TARGET_PATH"
echo "Skills to copy:"
for skill in "${REQUIRED_SKILLS[@]}"; do
  echo "- $skill"
done
echo ""
echo "If this target is not the Skills folder shown by your Codex app or CLI, rerun with:"
echo "bash ./scripts/install.sh --target /path/to/skills"

if [[ "$DRY_RUN" -eq 1 ]]; then
  echo ""
  echo "Dry run only. No files were copied."
  exit 0
fi

mkdir -p "$TARGET_PATH"

for skill in "${REQUIRED_SKILLS[@]}"; do
  rm -rf "$TARGET_PATH/$skill"
  cp -R "$SOURCE_SKILLS/$skill" "$TARGET_PATH/$skill"
done

echo ""
echo "Codex for Humans installed."
echo "Target Skills folder: $TARGET_PATH"
echo ""
echo "Restart Codex, then verify these Skills are visible:"
for skill in "${REQUIRED_SKILLS[@]}"; do
  echo "- $skill"
done
echo ""
echo "Tip: try /skills or type '$' in Codex to view available Skills."
echo "No secrets, logs, sessions, or private Codex data were copied."
