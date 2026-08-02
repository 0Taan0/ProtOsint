"""In-Memory Token-Bucket pro Connector. v2: Redis, prozessuebergreifend."""
import asyncio
import time
from dataclasses import dataclass, field


@dataclass
class TokenBucket:
    calls: int
    per_seconds: int
    _tokens: float = field(init=False)
    _last: float = field(init=False)

    def __post_init__(self):
        self._tokens = float(self.calls)
        self._last = time.monotonic()

    async def acquire(self) -> None:
        while True:
            now = time.monotonic()
            self._tokens = min(
                self.calls,
                self._tokens + (now - self._last) * self.calls / self.per_seconds,
            )
            self._last = now
            if self._tokens >= 1:
                self._tokens -= 1
                return
            await asyncio.sleep(0.05)
