import argparse
import fnmatch
import zipfile
from pathlib import Path


EXCLUDE_DIRS = {
    ".git",
    ".codex",
    ".agents",
    ".aws",
    ".azure",
    ".cache",
    ".config",
    ".gcloud",
    ".ssh",
    ".turbo",
    ".vscode",
    ".idea",
    "__pycache__",
    "attachments",
    "credentials",
    "sessions",
    "secret",
    "secrets",
    "private",
    "logs",
    "output",
    "node_modules",
    "dist",
    "build",
    "coverage",
}
EXCLUDE_SUFFIXES = {
    ".pyc",
    ".zip",
    ".7z",
    ".rar",
    ".tar",
    ".gz",
    ".key",
    ".pem",
    ".p12",
    ".pfx",
}
EXCLUDE_NAMES = {
    ".DS_Store",
    ".env",
    ".netrc",
    ".npmrc",
    ".pypirc",
    "Thumbs.db",
    "desktop.ini",
    "id_ed25519",
    "id_rsa",
}
EXCLUDE_NAMES_LOWER = {name.lower() for name in EXCLUDE_NAMES}
EXCLUDE_PATTERNS = {
    ".env.*",
    "*private*",
    "*secret*",
    "*secrets*",
    "*token*",
    "*credential*",
    "*credentials*",
}
EXCLUDE_PATH_PREFIXES = {
    "reports/private",
}


def matches_exclude_pattern(value: str) -> bool:
    lower_value = value.lower()
    return any(fnmatch.fnmatch(lower_value, pattern.lower()) for pattern in EXCLUDE_PATTERNS)


def should_include(path: Path, root: Path, output: Path) -> bool:
    if path.is_symlink():
        return False

    if not path.is_file():
        return False

    resolved_path = path.resolve()
    if resolved_path == output.resolve():
        return False

    try:
        resolved_path.relative_to(root)
    except ValueError:
        return False

    relative = path.relative_to(root)
    relative_posix = relative.as_posix()
    parts = {part.lower() for part in relative.parts}

    if parts & EXCLUDE_DIRS:
        return False

    if path.suffix.lower() in EXCLUDE_SUFFIXES:
        return False

    if path.name.lower() in EXCLUDE_NAMES_LOWER:
        return False

    if any(matches_exclude_pattern(part) for part in relative.parts):
        return False

    for prefix in EXCLUDE_PATH_PREFIXES:
        if relative_posix == prefix or relative_posix.startswith(prefix + "/"):
            return False

    return True


def package(root: Path, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    if output.exists():
        output.unlink()

    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(root.rglob("*")):
            if not should_include(path, root, output):
                continue
            arcname = path.relative_to(root).as_posix()
            archive.write(path, arcname)


def verify(output: Path) -> None:
    required = {
        "README.md",
        "SECURITY.md",
        "docs/BEGINNER_TUTORIAL.zh-TW.md",
        "docs/assets/tutorial-card-image2.png",
        "docs/assets/tutorial-decision-map-image2.png",
        "docs/assets/tutorial-install-steps-image2.png",
        "docs/assets/tutorial-proof-loop-image2.png",
        "skills/nontechnical-codex-project-controller/SKILL.md",
        "skills/nontechnical-codex-project-controller/agents/openai.yaml",
        "skills/nontechnical-project-readiness-auditor/SKILL.md",
        "skills/nontechnical-project-readiness-auditor/agents/openai.yaml",
        "scripts/install.ps1",
        "scripts/install.sh",
        "prompts/05-quick-daily-task.md",
        "prompts/06-full-project-task.md",
        "prompts/07-high-risk-task.md",
    }
    forbidden_names = {
        ".env",
        ".env.local",
        ".codex/sessions/session.txt",
        ".agents/skills/private.txt",
        "logs/run.log",
        "output/debug.txt",
        "reports/private/report.txt",
        "old.zip",
        "secrets/data.txt",
        "private/data.txt",
        "credentials_folder/data.txt",
        ".ssh/id_rsa",
        ".aws/config",
        ".azure/config.json",
        ".gcloud/config.json",
        ".config/private-app/config.json",
        ".npmrc",
        ".pypirc",
        ".netrc",
        "id_ed25519",
        "normal-link.txt",
    }

    with zipfile.ZipFile(output) as archive:
        names = set(archive.namelist())
        backslash_names = [name for name in names if "\\" in name]
        if backslash_names:
            raise SystemExit(f"Zip contains backslash paths: {backslash_names[:5]}")

        missing = sorted(required - names)
        if missing:
            raise SystemExit(f"Zip missing required files: {missing}")

        forbidden = sorted(forbidden_names & names)
        if forbidden:
            raise SystemExit(f"Zip included forbidden files: {forbidden}")

        bad = archive.testzip()
        if bad is not None:
            raise SystemExit(f"Zip integrity failure at: {bad}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a cross-platform Codex for Humans release zip.")
    parser.add_argument("--root", default=".", help="Repository root.")
    parser.add_argument("--output", required=True, help="Output zip path.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    output = Path(args.output).resolve()

    package(root, output)
    verify(output)
    print(output)


if __name__ == "__main__":
    main()
