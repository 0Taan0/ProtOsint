# Footprint Self-Audit

Skelett fuer ein OSINT-basiertes **Selbst**-Audit: systematische Erhebung und
Bewertung der eigenen oeffentlich auffindbaren digitalen Spuren, um sie zu
entfernen, bevor jemand anderes sie findet.

> Vorgesehener Einsatz: Analyse der **eigenen** oder nachweislich zugehoerigen
> Identitaeten. Kein Werkzeug zur Ermittlung ueber Dritte.

## Status

Durchverdrahtetes Geruest, keine fertige Software. Steht bereits:

- Vertraege: `Connector`, `Agent`, `SelectorPolicy`, `Proposal`
- Datenmodell (Graph in Postgres)
- Registry als zentrale Verdrahtung
- Orchestrator (Zustandsautomat + Pivot-Loop)
- Applier (Evidenz-/Confidence-/Policy-Gates) -- lauffaehig
- `git_connector` -- lauffaehige Referenz
- alles andere: strukturierte Stubs mit `TODO` / `NotImplementedError`

## Los

```bash
docker compose up -d
python -m app.cli init          # Schema + registrierte Connectoren anzeigen
```

## Erweitern

- **Neue Quelle** -> neuer Connector in `app/connectors/` nach dem Muster von
  `git_connector.py`, `register_connector(...)`. Sonst nichts.
- **Neue Urteilsart** -> neuer Agent in `app/agents/`, `register_agent(...)`.
- Faustregel: neue Quelle = Connector, neue Urteilsart = Agent.

## Reihenfolge des Ausbaus

1. Walking Skeleton: `git_connector` -> normalization -> collection -> report
2. `attribution_agent` (groesster Qualitaetssprung)
3. weitere Connectoren (crtsh, hibp, sherlock)
4. scoring + correlation (Kettenwert)
5. FastAPI-Routes fuer die Web-Version
