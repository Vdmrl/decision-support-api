from sentence_transformers import SentenceTransformer, util
from typing import Callable, Dict, List
from services.text_preprocessing import Preprocessing


# this module can not be tested because it use non-deterministic SentenceTransformer model
class ProjectRanker:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2") -> None:
        """
        initialization with ml model initialization
        :param model_name: model name. default: "all-MiniLM-L6-v2"
        """
        self.id_to_texts_function = None
        self.model = SentenceTransformer(model_name)  # initialize model

    def bind_to(self, get_id_to_texts_function: Callable[[], Dict]) -> None:
        """
        Bind function which return id to texts to get latest data every request (callback).
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
        if self.id_to_texts_function is None:
            return None

        it_to_text = await self.id_to_texts_function()

        # transform dict id: text to dict id: embedding
        id_to_embedding = dict()
        for ind, support_text in it_to_text.items():
            # text preprocessing
            preprocessed_text = Preprocessing.lowercase(support_text)
            preprocessed_text = Preprocessing.delete_not_letters(preprocessed_text)
            preprocessed_text = Preprocessing.delete_stop_words(preprocessed_text)
            id_to_embedding[ind] = self.model.encode(preprocessed_text, convert_to_tensor=True)

        # transform compared text
        preprocessed_project_text = Preprocessing.lowercase(text)
        preprocessed_project_text = Preprocessing.delete_not_letters(preprocessed_project_text)
        preprocessed_project_text = Preprocessing.delete_stop_words(preprocessed_project_text)
        project_embedding = self.model.encode(preprocessed_project_text)

        # sort dictionary values by cos similarity with argument text embedding
        id_to_embedding = dict(sorted(id_to_embedding.items(),
                                      key=lambda x: util.cos_sim(x[1], project_embedding)))
        return id_to_embedding.keys()
