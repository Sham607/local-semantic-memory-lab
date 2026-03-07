#!/usr/bin/env python3
"""
Build corpus manifests for split-index strategy:
- structured: concise fact logs / summaries
- transcript: long conversational dumps

Heuristic-only starter for handover.
"""

from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]
MEMORY_DIR = ROOT / "memory"
OUT_DIR = Path(__file__).resolve().parents[1] / "benchmarks"


def classify(path: Path, text: str) -> str:
    name = path.name.lower()
    if name in {"facts-config.md", "daily_news_log.md"}:
        return "structured"
    if "heartbeat" in name or ("-" in name and len(name) > 14):
        return "transcript"
    # simple heuristic: many json fences / metadata blocks => transcript-ish
    noisy_markers = text.count("```json") + text.count("sender_id")
    if noisy_markers >= 3:
        return "transcript"
    return "structured"


def main():
    structured, transcript = [], []
    if not MEMORY_DIR.exists():
        print(f"memory dir not found: {MEMORY_DIR}")
        return

    for p in sorted(MEMORY_DIR.glob("*.md")):
        text = p.read_text(errors="ignore")
        kind = classify(p, text)
        rec = {"path": str(p), "kind": kind}
        if kind == "structured":
            structured.append(rec)
        else:
            transcript.append(rec)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "manifest.structured.json").write_text(json.dumps(structured, indent=2))
    (OUT_DIR / "manifest.transcript.json").write_text(json.dumps(transcript, indent=2))
    print(f"structured={len(structured)} transcript={len(transcript)}")


if __name__ == "__main__":
    main()
