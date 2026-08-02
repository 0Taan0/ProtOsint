"""Zentrale Enums. Alles, was mehr als ein Modul betrifft, lebt hier,
damit Connectoren, Agenten und Services dieselbe Sprache sprechen."""
from enum import StrEnum


class SelectorType(StrEnum):
    USERNAME = "username"
    EMAIL = "email"
    PHONE = "phone"
    DOMAIN = "domain"
    REAL_NAME = "real_name"
    IMAGE_HASH = "image_hash"
    URL = "url"


class FindingType(StrEnum):
    ACCOUNT = "account"          # Profil auf einer Plattform
    BREACH = "breach"            # Vorkommen in einem Datenleck
    DOMAIN_RECORD = "domain_record"
    PUBLIC_RECORD = "public_record"   # Impressum, Handelsregister, Rezension
    METADATA = "metadata"        # EXIF, Git-Commit, Dokument-Properties
    CONTENT = "content"          # Post, Kommentar, Text


class EdgeType(StrEnum):
    SAME_USERNAME = "same_username"
    SAME_EMAIL = "same_email"
    SAME_AVATAR = "same_avatar"       # identischer perceptual hash
    SAME_STYLE = "same_style"         # Stilometrie, spätere Ausbaustufe
    STATED = "stated"                 # explizit verlinkt/angegeben
    CO_OCCURRENCE = "co_occurrence"


class ProposalKind(StrEnum):
    NEW_SELECTOR = "new_selector"
    ENTITY_LINK = "entity_link"
    CLASSIFICATION = "classification"
    RISK_NOTE = "risk_note"


class RunStatus(StrEnum):
    QUEUED = "queued"
    RUNNING = "running"
    DONE = "done"
    FAILED = "failed"


class TaskStatus(StrEnum):
    PENDING = "pending"
    RUNNING = "running"
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    SKIPPED = "skipped"


class Phase(StrEnum):
    """Die festen Phasen des Supervisors. Reihenfolge = Kontrollfluss."""
    SCOPING = "scoping"
    DISCOVER = "discover"
    COLLECT = "collect"
    VERIFY = "verify"
    ANALYZE = "analyze"
    CORRELATE = "correlate"
    SCORE = "score"
    REPORT = "report"
