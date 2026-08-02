"""STUB. Verifikationsschicht -- das Differenzierungsmerkmal.
Existenz pruefen, Negativkontrolle, Attribution (via Attribution-Agent)."""
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.run import Run
from app.services.apply_service import ApplyOutcome
from app.services import agent_service   # noqa
from app.schemas.enums import Phase


async def verify_new_findings(run: Run, session: AsyncSession) -> ApplyOutcome:
    # TODO:
    #  1. Existenzpruefung: Profil wirklich abrufen, nicht nur Statuscode
    #  2. Negativkontrolle: Zufalls-Username -- "gefunden" => Connector kaputt, Treffer verwerfen
    #  3. Attribution: agent_service.run_phase(Phase.VERIFY, ...) -> ENTITY_LINK + NEW_SELECTOR
    # ApplyOutcome zurueckgeben, dessen new_selectors_count() den Loop steuert.
    raise NotImplementedError("verification_service ausbauen")
