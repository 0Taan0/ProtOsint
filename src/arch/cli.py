"""CLI-first Einstieg. python -m app.cli <command>"""
import asyncio
import sys
from app.core.registry import load_all, all_connectors
from app.core.db import init_db, SessionLocal
from app.core.logging import get_logger

log = get_logger("cli")


async def cmd_init():
    load_all()
    await init_db()
    log.info("DB initialisiert. Registrierte Connectoren: %s",
             [c.capability.name for c in all_connectors()])


async def cmd_run(seed_type: str, seed_value: str):
    load_all()
    # TODO: Subject + Run + Seed-Selektor + Tasks anlegen, dann:
    #   from app.services import orchestration_service
    #   async with SessionLocal() as s: await orchestration_service.run_audit(run, s)
    log.info("run: seed %s=%s (Orchestrator-Verdrahtung steht, Services ausbauen)",
             seed_type, seed_value)


async def cmd_report(run_id: str):
    # TODO: report_service aufrufen, HTML nach ./out schreiben
    log.info("report fuer %s (report_service ausbauen)", run_id)


def main():
    args = sys.argv[1:]
    if not args:
        print("usage: python -m app.cli [init|run <type> <value>|report <run_id>]"); return
    cmd, rest = args[0], args[1:]
    match cmd:
        case "init":   asyncio.run(cmd_init())
        case "run":    asyncio.run(cmd_run(*rest))
        case "report": asyncio.run(cmd_report(*rest))
        case _:        print(f"unknown command: {cmd}")


if __name__ == "__main__":
    main()
