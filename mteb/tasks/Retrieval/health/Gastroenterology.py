from __future__ import annotations

from mteb.abstasks.TaskMetadata import TaskMetadata

from ....abstasks.AbsTaskRetrieval import AbsTaskRetrieval


class HeMtebGastroenterologyRetrieval(AbsTaskRetrieval):
    metadata = TaskMetadata(
        dataset={
            "path": "clinia/health-information-retrieval-gastroenterology-en-bm25",
            "revision": "cb7b759d62d0440aa8f295f5151f8a1b1bf5a70a",
        },
        name="HeMtebGastroenterology",
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
