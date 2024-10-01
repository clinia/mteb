from __future__ import annotations

from mteb.abstasks.TaskMetadata import TaskMetadata

from .....abstasks.AbsTaskRetrieval import AbsTaskRetrieval
from .....abstasks.MultilingualTask import MultilingualTask
from . import HeMtebTask

_LANGUAGES = {
    "en-en": ["eng-Latn", "eng-Latn"],
    "es-en": ["spa-Latn", "eng-Latn"],
    "fr-en": ["fra-Latn", "eng-Latn"],
}


class HeMtebPyschiatryAndPsychologyRetrieval(
    AbsTaskRetrieval, HeMtebTask, MultilingualTask
):
    metadata = TaskMetadata(
        dataset={
            "path": "clinia/hemteb-pyschiatry-and-pyschology-bm25",
            "revision": "29c18d5c598118f3fb9a942ea072127e14cadceb",
        },
        name="HeMtebPsychiatryAndPsychology",
        description="",
        type="Retrieval",
        modalities=["text"],
        category="s2p",
        reference=None,
        eval_splits=["test"],
        eval_langs=_LANGUAGES,
        main_score="ndcg_at_10",
        date=None,
        domains=["Medical"],
        task_subtypes=None,
        license=None,
        annotations_creators="expert-annotated",
        dialect=None,
        sample_creation=None,
        bibtex_citation=None,
        descriptive_stats={},
    )

    def load_data(self, **kwargs):
        HeMtebTask.load_data(self, **kwargs)
