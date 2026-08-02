"""REFERENZ-CONNECTOR (lauffaehig). Deterministisch, kein Netz, keine Keys.
Liest Commit-Metadaten lokaler Repos und produziert Mail-Selektoren.
Nach diesem Muster werden alle weiteren Connectoren gebaut."""
import subprocess
from datetime import datetime, timezone
from decimal import Decimal
from app.connectors.base import BaseConnector
from app.core.registry import register_connector
from app.schemas.connector import ConnectorCapability
from app.schemas.enums import SelectorType, FindingType
from app.schemas.selector import SelectorOut
from app.schemas.connector import RunContext
from app.schemas.finding import RawFinding


class GitConnector(BaseConnector):
    capability = ConnectorCapability(
        name="git",
        version="0.1.0",
        accepts={SelectorType.URL},          # value = lokaler Repo-Pfad
        produces={FindingType.METADATA},
        requires_auth=False,
        cost_per_call_cents=Decimal("0"),
        reliability=1.0,                     # deterministisch
    )

    async def fetch(self, selector: SelectorOut, ctx: RunContext) -> list[RawFinding]:
        repo = selector.value
        try:
            out = subprocess.run(
                ["git", "-C", repo, "log", "--pretty=%an|%ae|%aI", "-n", "500"],
                capture_output=True, text=True, timeout=15, check=True,
            ).stdout
        except (subprocess.SubprocessError, FileNotFoundError):
            return []

        authors: dict[str, dict] = {}
        for line in out.splitlines():
            parts = line.split("|")
            if len(parts) != 3:
                continue
            name, email, iso = parts
            a = authors.setdefault(email, {"name": name, "email": email, "commits": 0, "times": []})
            a["commits"] += 1
            a["times"].append(iso)

        findings: list[RawFinding] = []
        for email, a in authors.items():
            findings.append(RawFinding(
                type=FindingType.METADATA,
                label=f"Git author {a['name']} <{email}>",
                attributes={"name": a["name"], "email": email, "commits": a["commits"]},
                raw={"sample_times": a["times"][:10]},
                produced_selectors=[(SelectorType.EMAIL, email)],   # <- Pivot-Material
            ))
        return findings


register_connector(GitConnector())
