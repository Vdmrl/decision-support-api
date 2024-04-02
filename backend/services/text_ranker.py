from sentence_transformers import SentenceTransformer, util
from typing import Callable, Dict, List

model = SentenceTransformer("all-MiniLM-L6-v2")  # initialize model


class ProjectRanker:
    def __init__(self) -> None:
        self.id_to_texts_function = None

    def bind_to(self, get_id_to_texts_function: Callable[[], Dict]) -> None:
        """
        Bind function which return id to texts to get latest data every request.
        It is impossible to save embeddings because data could be changed
        and I do not have access to check it changes in time.
        :param get_id_to_texts_function: function which return all id: support text
        :return: None
        """
        self.id_to_texts_function = get_id_to_texts_function

    async def sort_for(self, text: str) -> List[int]:
        """
        get current text data, transform it to embeddings
        and sort embeddings by cos similarity with argument text embedding
        :param text: text to be compared with pinned function texts
        :return: list of ids sorted by cos sim
        """

        it_to_text = await self.id_to_texts_function()

        # transform dict id: text to dict id: embedding
        id_to_embedding = dict()
        for ind, val in it_to_text.items():
            id_to_embedding[ind] = model.encode(val, convert_to_tensor=True)

        # transform compared text
        project_embedding = model.encode(text)

        # sort dictionary values by cos similarity with argument text embedding
        id_to_embedding = dict(sorted(id_to_embedding.items(),
                                      key=lambda x: util.cos_sim(x[1], project_embedding)))
        return id_to_embedding.keys()
