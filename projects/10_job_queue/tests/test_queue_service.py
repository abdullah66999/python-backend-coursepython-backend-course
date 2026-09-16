import asyncio

from queue_service import run_demo


def test_run_demo_waits_for_job():
    assert asyncio.run(run_demo()) == [1]
