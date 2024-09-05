from __future__ import annotations

from collections import defaultdict

from datasets import Features, Value, load_dataset

from mteb.abstasks.TaskMetadata import TaskMetadata

from .....abstasks.AbsTaskRetrieval import AbsTaskRetrieval
from .....abstasks.MultilingualTask import MultilingualTask

_LANGUAGES = {
    "en-en": ["eng-Latn", "eng-Latn"],
    "es-en": ["spa-Latn", "eng-Latn"],
    "fr-en": ["fra-Latn", "eng-Latn"],
}


class HeMtebDermatologyRetrieval(AbsTaskRetrieval, MultilingualTask):
    metadata = TaskMetadata(
        dataset={
            "path": "clinia/hemteb-dermatology-bm25",
            "revision": "",
        },
        name="HeMtebDermatology",
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

    def _load_corpus(self, language: str, cache_dir: str | None = None):
        corpus_ds = load_dataset(
            path=self.metadata_dict["dataset"]["path"],
            name=f"{language}-corpus",
            revision=self.metadata_dict["dataset"]["revision"],
            cache_dir=cache_dir,
        )
        corpus_ds = next(iter(corpus_ds.values()))
        corpus_ds = corpus_ds.cast_column("_id", Value("string"))
        corpus_ds = corpus_ds.rename_column("_id", "id")
        corpus_ds = corpus_ds.remove_columns(
            [
                col
                for col in corpus_ds.column_names
                if col not in ["id", "text", "title"]
            ]
        )
        corpus = {
            doc["id"]: {"title": doc["title"], "text": doc["text"]} for doc in corpus_ds
        }
        return corpus

    def _load_queries(self, language: str, cache_dir: str | None = None):
        queries_ds = load_dataset(
            path=self.metadata_dict["dataset"]["path"],
            name=f"{language}-queries",
            revision=self.metadata_dict["dataset"]["revision"],
            cache_dir=cache_dir,
        )
        queries_ds = next(iter(queries_ds.values()))
        queries_ds = queries_ds.cast_column("_id", Value("string"))
        queries_ds = queries_ds.rename_column("_id", "id")
        queries_ds = queries_ds.remove_columns(
            [col for col in queries_ds.column_names if col not in ["id", "text"]]
        )
        queries = {query["id"]: query["text"] for query in queries_ds}
        return queries

    def _load_qrels(self, language: str, split: str, cache_dir: str | None = None):
        qrels_ds = load_dataset(
            path=self.metadata_dict["dataset"]["path"],
            name=f"{language}-qrels",
            revision=self.metadata_dict["dataset"]["revision"],
            cache_dir=cache_dir,
        )[split]
        features = Features(
            {
                "query-id": Value("string"),
                "corpus-id": Value("string"),
                "score": Value("float"),
            }
        )
        qrels_ds = qrels_ds.cast(features)
        qrels_dict = defaultdict(dict)

        def qrels_dict_init(row):
            qrels_dict[row["query-id"]][row["corpus-id"]] = int(row["score"])

        qrels_ds.map(qrels_dict_init)
        return qrels_dict

    def load_data(self, **kwargs):
        if self.data_loaded:
            return
        eval_splits = self.metadata_dict["eval_splits"]
        languages = self.metadata.eval_langs
        cache_dir = kwargs.get("cache_dir", None)
        self.corpus = {
            language: {split: None for split in eval_splits} for language in languages
        }
        self.queries = {
            language: {split: None for split in eval_splits} for language in languages
        }
        self.relevant_docs = {
            language: {split: None for split in eval_splits} for language in languages
        }
        for language in languages:
            for split in eval_splits:
                self.corpus[language][split] = self._load_corpus(
                    language=language, cache_dir=cache_dir
                )
                self.queries[language][split] = self._load_queries(
                    language=language, cache_dir=cache_dir
                )
                self.relevant_docs[language][split] = self._load_qrels(
                    language=language, split=split, cache_dir=cache_dir
                )
        self.data_loaded = True
