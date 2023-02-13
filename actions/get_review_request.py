from lib.base import BaseReviewBoardAction

__all__ = [
    'GetReviewById'
]


class GetReviewById(BaseReviewBoardAction):
    def run(self, review):
        review_request = \
            self._client.get_review_request(
                review_request_id=review)

        return review_request.rsp
