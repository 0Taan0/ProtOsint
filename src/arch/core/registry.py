"""Die zentrale Verdrahtung. Connectoren und Agenten registrieren sich hier;
der Orchestrator fragt nur die Registry, kennt keine konkrete Klasse.
Erweitern = eine Klasse plus ein register()-Aufruf. Kein Eingriff sonst."""
from app.schemas.connector import Connector
from app.schemas.agent import Agent
from app.schemas.enums import SelectorType, Phase

_CONNECTORS: dict[str, Connector] = {}
_AGENTS: dict[str, Agent] = {}


def register_connector(instance: Connector) -> Connector:
    _CONNECTORS[instance.capability.name] = instance
    return instance


def register_agent(instance: Agent) -> Agent:
    _AGENTS[instance.name] = instance
    return instance


def connectors_for(selector_type: SelectorType) -> list[Connector]:
    """Alle Connectoren, die diesen Selektortyp verarbeiten koennen."""
    return [c for c in _CONNECTORS.values() if selector_type in c.capability.accepts]


def agents_for(phase: Phase) -> list[Agent]:
    return [a for a in _AGENTS.values() if a.phase == phase]


def all_connectors() -> list[Connector]:
    return list(_CONNECTORS.values())


def load_all() -> None:
    """Import mit Seiteneffekt: die Module registrieren sich beim Import.
    Hier zentral aufrufen (CLI, FastAPI-Startup)."""
    from app.connectors import git_connector, hibp_connector, crtsh_connector, sherlock_connector  # noqa
    from app.agents import discovery_agent, attribution_agent, analysis_agent, risk_agent  # noqa
