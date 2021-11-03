from app.models.tortoise import TextSummary
from app.models.pydantic import SummaryPayloadSchema, SummaryResponseSchema


async def post(payload: SummaryPayloadSchema) -> int:
    summary = TextSummary(
        url=payload.url,
        summary="dummy summary",
    )

    await summary.save()

    return summary.id
