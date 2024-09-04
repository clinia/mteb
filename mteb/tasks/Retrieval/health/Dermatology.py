from __future__ import annotations

from mteb.abstasks.TaskMetadata import TaskMetadata

from ....abstasks.AbsTaskRetrieval import AbsTaskRetrieval


class HeMtebDermatologyRetrieval(AbsTaskRetrieval):
    metadata = TaskMetadata(
        dataset={
            "path": "clinia/health-information-retrieval-dermatology-en-bm25",
            "revision": "c0bbb31185a46b980e5092029772dc0fefaffb37",
        },
        name="HeMtebDermatology",
        description="",
        type="Retrieval",
        modalities=["text"],
        category="s2p",
        reference=None,
        eval_splits=["test"],
        eval_langs=["eng-Latn"],
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
