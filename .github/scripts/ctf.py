import hashlib, hmac, json, os, re, sys
from datetime import datetime, timezone
from pathlib import Path

TITLE = os.environ["TITLE"].strip()
SOLVER = os.environ["SOLVER"]          # GitHub login: [A-Za-z0-9-], safe for markdown
FLAG = os.environ["FLAG"]
DB = Path(".github/ctf/solvers.json")
README = Path("README.md")

def out(key, val):
    with open(os.environ["GITHUB_OUTPUT"], "a") as f:
        f.write(f"{key}={val}\n")

db = json.loads(DB.read_text()) if DB.exists() else {"solvers": []}

if any(s["user"] == SOLVER for s in db["solvers"]):
    out("result", "already"); sys.exit(0)

m = re.fullmatch(r"ctf:\s*([0-9a-fA-F]{16})", TITLE)
expected = hashlib.sha256(f"{FLAG}:{SOLVER}".encode()).hexdigest()[:16]

if not m or not hmac.compare_digest(m.group(1).lower(), expected):
    out("result", "wrong"); sys.exit(0)

db["solvers"].append({
    "user": SOLVER,
    "at": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M"),
})
DB.write_text(json.dumps(db, indent=2) + "\n")

rows = "\n".join(
    f"| {i} | [@{s['user']}](https://github.com/{s['user']}) | {s['at']} |"
    for i, s in enumerate(db["solvers"][:10], 1)
)
block = (
    f"| # | Solver | Solved (UTC) |\n|---|---|---|\n{rows}\n\n"
    f"_Total solves: {len(db['solvers'])}_"
)
text = README.read_text()
text = re.sub(
    r"(<!-- CTF:START -->).*?(<!-- CTF:END -->)",
    lambda mm: f"{mm.group(1)}\n{block}\n{mm.group(2)}",
    text, flags=re.S,
)
README.write_text(text)
out("result", "correct")
