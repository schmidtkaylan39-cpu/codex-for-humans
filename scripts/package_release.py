import argparse
import zipfile
from pathlib import Path


EXCLUDE_DIRS = {".git", "__pycache__"}
EXCLUDE_SUFFIXES = {".pyc"}


def should_include(path: Path, root: Path) -> bool:
    relative = path.relative_to(root)
    parts = set(relative.parts)
    if parts & EXCLUDE_DIRS:
        return False
    if path.suffix in EXCLUDE_SUFFIXES:
        return False
    return path.is_file()


def package(root: Path, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    if output.exists():
        output.unlink()

    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(root.rglob("*")):
            if not should_include(path, root):
                continue
            arcname = path.relative_to(root).as_posix()
            archive.write(path, arcname)


def verify(output: Path) -> None:
    required = {
        "README.md",
        "SECURITY.md",
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

    with zipfile.ZipFile(output) as archive:
        names = set(archive.namelist())
        backslash_names = [name for name in names if "\\" in name]
        if backslash_names:
            raise SystemExit(f"Zip contains backslash paths: {backslash_names[:5]}")

        missing = sorted(required - names)
        if missing:
            raise SystemExit(f"Zip missing required files: {missing}")

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

