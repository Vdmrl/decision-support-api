import pytest

from services.text_preprocessing import Preprocessing


class TestPreprocessing:

    @pytest.mark.parametrize(
        "text, ans",
        [
            (
                "ТекскЕтск 123132 vluin204@gnauil.com ntrcn Тавы теквт 89228115 +791215 конц Ц2Ц",
                "текскетск 123132 vluin204@gnauil.com ntrcn тавы теквт 89228115 +791215 конц ц2ц",
            ),
            ("Ц", "ц"),
            ("", ""),
        ],
    )
    def test_lowercase(self, text, ans):
        assert Preprocessing.lowercase(text) == ans

    @pytest.mark.parametrize(
        "text, ans",
        [
            (
                "ТекскЕтск 123132 vluin204@gnauil.com ntrcn Тавы теквт 89228115 +791215 конц Ц2Ц",
                "екск тск авы теквт конц",
            ),
            ("Ц", ""),
            ("ц", "ц"),
            ("", ""),
        ],
    )
    def test_delete_not_letters(self, text, ans):
        assert Preprocessing.delete_not_letters(text) == ans

    @pytest.mark.parametrize(
        "text, ans",
        [
            ("текст ни тест слово важное слово ж жена теквт конц", "текст тест слово важное слово жена теквт конц"),
            ("Ц", "Ц"),
            ("же", ""),
            ("", ""),
        ],
    )
    def test_delete_stop_words(self, text, ans):
        assert Preprocessing.delete_stop_words(text) == ans
