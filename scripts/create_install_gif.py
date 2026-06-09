from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "assets" / "install-demo.gif"


def font(size: int, bold: bool = False):
    candidates = [
        Path("C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf"),
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
    ]
    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size)
    return ImageFont.load_default()


TITLE = font(48, True)
SUBTITLE = font(28)
BODY = font(25)
SMALL = font(20)


frames_data = [
    (
        "Codex for Humans",
        "Install two Skills. Build with evidence, not code reading.",
        ["Download or clone the repo.", "Keep it separate from private Codex logs."],
        "Step 1 / 6",
    ),
    (
        "Find Your Skills Folder",
        "Codex paths may differ by version or environment.",
        ["Common: ~/.agents/skills", "Common: ~/.codex/skills", "Use the path your Codex shows."],
        "Step 2 / 6",
    ),
    (
        "Run One-Click Install",
        "The script copies only the two public Skill folders.",
        ["Windows: scripts/install.ps1", "macOS/Linux: scripts/install.sh", "No secrets, logs, or sessions are copied."],
        "Step 3 / 6",
    ),
    (
        "Restart Codex",
        "Verify both Skills are visible before using them.",
        ["nontechnical-codex-project-controller", "nontechnical-project-readiness-auditor", "Try /skills or type $ in Codex."],
        "Step 4 / 6",
    ),
    (
        "Choose The Right Skill",
        "Use the project stage to decide.",
        ["0-1: Project Controller", "70-100: Readiness Auditor", "Web GPT: outside review only."],
        "Step 5 / 6",
    ),
    (
        "Work Safely",
        "Local evidence decides whether something is ready.",
        ["Use fake data or sandbox first.", "Never paste secrets into chat.", "High-risk actions need approval."],
        "Step 6 / 6",
    ),
]


def draw_frame(title: str, subtitle: str, bullets: list[str], step: str) -> Image.Image:
    width, height = 1280, 720
    img = Image.new("RGB", (width, height), "#f7f7f2")
    d = ImageDraw.Draw(img)

    d.rounded_rectangle((52, 52, width - 52, height - 52), radius=28, fill="#ffffff", outline="#1f2933", width=4)
    d.rounded_rectangle((90, 90, 310, 142), radius=18, fill="#226f54")
    d.text((112, 105), step, fill="#ffffff", font=SMALL)

    d.text((90, 185), title, fill="#1f2933", font=TITLE)
    d.text((90, 252), subtitle, fill="#3b4652", font=SUBTITLE)

    y = 338
    for bullet in bullets:
        d.ellipse((100, y + 8, 118, y + 26), fill="#f4a261")
        d.text((140, y), bullet, fill="#1f2933", font=BODY)
        y += 58

    d.line((90, 610, width - 90, 610), fill="#d9ded8", width=3)
    d.text((90, 636), "Codex executes locally. Web GPT reviews only. Tests and evidence decide delivery.", fill="#5f6c76", font=SMALL)
    return img


frames = [draw_frame(*frame) for frame in frames_data]
OUT.parent.mkdir(parents=True, exist_ok=True)
frames[0].save(
    OUT,
    save_all=True,
    append_images=frames[1:],
    duration=[3500, 4500, 4500, 4500, 4500, 4500],
    loop=0,
)
print(OUT)

