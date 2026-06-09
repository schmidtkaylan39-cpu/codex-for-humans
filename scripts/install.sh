#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
SOURCE_SKILLS="$REPO_ROOT/skills"

REQUIRED_SKILLS=(
  "nontechnical-codex-project-controller"
  "nontechnical-project-readiness-auditor"
)

TARGET_PATH="${1:-${CODEX_SKILLS_DIR:-}}"

if [[ -z "$TARGET_PATH" ]]; then
  if [[ -d "$HOME/.agents/skills" ]]; then
    TARGET_PATH="$HOME/.agents/skills"
  elif [[ -d "$HOME/.codex/skills" ]]; then
    TARGET_PATH="$HOME/.codex/skills"
  else
    TARGET_PATH="$HOME/.codex/skills"
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

