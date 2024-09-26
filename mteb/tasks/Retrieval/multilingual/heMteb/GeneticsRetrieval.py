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


class HeMtebGeneticsRetrieval(AbsTaskRetrieval, MultilingualTask, HeMtebTask):
    metadata = TaskMetadata(
        dataset={
            "path": "clinia/hemteb-genetics-bm25",
            "revision": "eb62be7f30b3ec0060af4c3aca2e6bc0f6177859",
        },
        name="HeMtebGenetics",
        description="",
        type="Retrieval",
        modalities=["text"],
        category="s2p",
        reference=None,
        eval_splits=["test"],
        eval_langs=_LANGUAGES,
        main_score="ndcg_at_10",
        date=None,
        domains=["CliniaHealth"],
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
       )
