from app.schemas.submission import SubmissionResult
from app.services.inquest import InQuest
from app.submitters.abstract import AbstractSubmitter


class InQuestSubmitter(AbstractSubmitter):
    async def submit(self) -> SubmissionResult:
        client = InQuest()
        file_ = self.attachment_as_file()
        res = await client.dfi_upload(file_)

        data = res.get("data", "")
        return SubmissionResult(
            reference_url=f"https://labs.inquest.net/dfi/sha256/{data}"
        )
