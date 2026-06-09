param(
  [string]$TargetPath = ""
)

$ErrorActionPreference = "Stop"

$RepoRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
$SourceSkills = Join-Path $RepoRoot "skills"
$RequiredSkills = @(
  "nontechnical-codex-project-controller",
  "nontechnical-project-readiness-auditor"
)

function Test-SkillSource {
  foreach ($skill in $RequiredSkills) {
    $skillPath = Join-Path $SourceSkills $skill
    $skillFile = Join-Path $skillPath "SKILL.md"
    $agentFile = Join-Path $skillPath "agents\openai.yaml"

    if (-not (Test-Path -LiteralPath $skillFile)) {
      throw "Missing required file: $skillFile"
    }

    if (-not (Test-Path -LiteralPath $agentFile)) {
      throw "Missing required file: $agentFile"
    }
  }
}

function Resolve-SkillsTarget {
  if ($TargetPath -ne "") {
    return $TargetPath
  }

  if ($env:CODEX_SKILLS_DIR -and $env:CODEX_SKILLS_DIR.Trim() -ne "") {
    return $env:CODEX_SKILLS_DIR
  }

  $candidates = @(
    (Join-Path $HOME ".agents\skills"),
    (Join-Path $HOME ".codex\skills")
  )

  foreach ($candidate in $candidates) {
    if (Test-Path -LiteralPath $candidate) {
      return $candidate
    }
  }

  return (Join-Path $HOME ".codex\skills")
}

Test-SkillSource

$ResolvedTarget = Resolve-SkillsTarget
New-Item -ItemType Directory -Force -Path $ResolvedTarget | Out-Null

foreach ($skill in $RequiredSkills) {
  $source = Join-Path $SourceSkills $skill
  $destination = Join-Path $ResolvedTarget $skill
  Copy-Item -Recurse -Force -LiteralPath $source -Destination $destination
}

Write-Host ""
Write-Host "Codex for Humans installed." -ForegroundColor Green
Write-Host "Target Skills folder: $ResolvedTarget"
Write-Host ""
Write-Host "Restart Codex, then verify these Skills are visible:"
foreach ($skill in $RequiredSkills) {
  Write-Host "- $skill"
}
Write-Host ""
Write-Host "Tip: try /skills or type `$ in Codex to view available Skills."
Write-Host "No secrets, logs, sessions, or private Codex data were copied."

