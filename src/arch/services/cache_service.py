"""STUB. Connector-Cache. Macht --offline und deterministische Tests moeglich."""
import hashlib
from sqlalchemy.ext.asyncio import AsyncSession


def cache_key(connector_name: str, version: str, sel_type: str, value: str) -> str:
    return hashlib.sha256(f"{connector_name}|{version}|{sel_type}|{value}".encode()).hexdigest()

# TODO: async get(key, session) -> dict | None   (None => Miss => Netz)
# TODO: async set(key, payload, ttl, session)
