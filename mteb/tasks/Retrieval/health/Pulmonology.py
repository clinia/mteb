from __future__ import annotations

from mteb.abstasks.TaskMetadata import TaskMetadata

from ....abstasks.AbsTaskRetrieval import AbsTaskRetrieval


class HeMtebPulmonologyRetrieval(AbsTaskRetrieval):
    metadata = TaskMetadata(
        dataset={
            "path": "clinia/health-information-retrieval-pulmonology-en-bm25",
            "revision": "0ea22c47cf202c94c4f6eddec19337bdf37784b6",
        },
        name="HeMtebPulmonology",
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
