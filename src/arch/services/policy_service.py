"""Die Policy-Naht. v1: LocalOwnerPolicy sagt immer ja. v2 tauscht die
Klasse gegen VerifiedOwnershipPolicy -- der Rest der Codebasis merkt nichts."""
from app.schemas.policy import SelectorPolicy, SelectorDecision
from app.schemas.selector import SelectorOut


class LocalOwnerPolicy:
    """Annahme: lokaler Betrieb, Subject == Betreiber."""
    def evaluate(self, selector: SelectorOut, subject_id: str) -> SelectorDecision:
        return SelectorDecision(allowed=True, may_pivot=True, reason="local_owner")


# v2-Skizze, bewusst noch nicht verdrahtet:
# class VerifiedOwnershipPolicy:
#     def evaluate(self, selector, subject_id):
#         proven = check_proof(selector, subject_id)   # DNS-TXT / Bio-String / Double-Opt-In
#         return SelectorDecision(allowed=proven, may_pivot=proven, reason=...)


def get_policy(name: str = "local_owner") -> SelectorPolicy:
    return {"local_owner": LocalOwnerPolicy()}[name]
