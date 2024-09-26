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


class HeMtebDentistryAndOralHealthTertiaryRelevanceJudgmentRetrieval(
    HeMtebTask, AbsTaskRetrieval, MultilingualTask
):
    metadata = TaskMetadata(
        dataset={
            "path": "clinia/hemteb-dentistry-and-oral-health-bm25-tertiary-relevance-judgments",
            "revision": "b4a18cb92e38bf6f6e636f8a2bd7d32f9faeac35",
        },
        name="HeMtebDentistryAndOralHealthTertiaryRelevanceJudgment",
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
