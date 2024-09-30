from __future__ import annotations

from mteb.abstasks.TaskMetadata import TaskMetadata

from ....abstasks.AbsTaskRetrieval import AbsTaskRetrieval


class HeMtebGeneticsRetrieval(AbsTaskRetrieval):
    metadata = TaskMetadata(
        dataset={
            "path": "clinia/health-information-retrieval-genetics-en-bm25",
            "revision": "a2944ab333ba055f4a70e31823fc0bddcebe378e",
        },
        name="HeMtebGenetics",
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
