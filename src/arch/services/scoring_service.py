"""STUB (Arithmetik-Geruest steht). DETERMINISTISCH -- nie das LLM.
Vier Faktoren pro Befund plus Kettenwert aus dem Graphen."""
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.run import Run

WEIGHTS = {"discoverability": 0.25, "identifiability": 0.30,
           "sensitivity": 0.30, "persistence": 0.15}


def combine(discoverability: float, identifiability: float,
            sensitivity: float, persistence: float) -> float:
    return (WEIGHTS["discoverability"] * discoverability
            + WEIGHTS["identifiability"] * identifiability
            + WEIGHTS["sensitivity"] * sensitivity
            + WEIGHTS["persistence"] * persistence)


async def score_run(run: Run, session: AsyncSession) -> None:
    # TODO: je Finding die vier Faktoren bestimmen (Regeln/Lookup, kein LLM),
    #       combine() anwenden, chain_score aus correlation_service.shortest_chain,
    #       RiskItem-Zeilen schreiben.
    raise NotImplementedError
