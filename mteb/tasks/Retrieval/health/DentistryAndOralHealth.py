from __future__ import annotations

from mteb.abstasks.TaskMetadata import TaskMetadata

from ....abstasks.AbsTaskRetrieval import AbsTaskRetrieval


class HeMtebDentistryAndOralRetrieval(AbsTaskRetrieval):
    metadata = TaskMetadata(
        dataset={
            "path": "clinia/health-information-retrieval-dentistry-and-oral-health-en-bm25",
            "revision": "282723268448f1878452c8c2a335dd22d31d8f78",
        },
        name="HeMtebDentistryAndOralHealth",
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
