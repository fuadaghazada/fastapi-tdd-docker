from typing import Optional, List

from app.models.tortoise import TextSummary
from app.models.pydantic import SummaryPayloadSchema


async def post(payload: SummaryPayloadSchema) -> int:
    summary = TextSummary(
        url=payload.url,
        summary="dummy summary",
    )

    await summary.save()

    return summary.id


async def get(summary_id: int) -> Optional[None]:
    summary = await TextSummary.filter(id=summary_id).first().values()
    if summary:
        return summary[0]
    return None


async def get_all() -> List:
    summaries = await TextSummary.all().values()
    return summaries
