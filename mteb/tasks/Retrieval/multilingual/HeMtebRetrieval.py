from __future__ import annotations

from collections import defaultdict
from enum import Enum

from datasets import Features, Value, load_dataset

from mteb.abstasks.TaskMetadata import TaskMetadata

from ....abstasks.AbsTaskRetrieval import AbsTaskRetrieval
from ....abstasks.MultilingualTask import MultilingualTask

_LANGUAGES = {
    "en-en": ["eng-Latn", "eng-Latn"],
    "es-en": ["spa-Latn", "eng-Latn"],
    "fr-en": ["fra-Latn", "eng-Latn"],
}


class HeMtebSplits(str, Enum):
    all = "All"
    dentistry_and_oral_health = "Dentistry and Oral Health"
    dermatology = "Dermatology"
    gastroenterology = "Gastroenterology"
    genetics = "Genetics"
    neuroscience_and_neurology = "Neuroscience and Neurology"
    orthopedic_surgery = "Orthopedic Surgery"
    otorhinolaryngology = "Otorhinolaryngology"
    plastic_surgery = "Plastic Surgery"
    pulmonology = "Pulmonology"
    psychiatry_and_psychology = "Pyschiatry and Pyschology"

    @classmethod
    def names(cls) -> list[str]:
        return sorted(cls._member_names_)


class HeMtebRetrieval(MultilingualTask, AbsTaskRetrieval):
    metadata = TaskMetadata(
        dataset={
            "path": "clinia/CURE-v1",
            "revision": "c879d98bc4c09e0ceb76b6713089dda8c7e113fd",
        },
        name="HeMtebRetrieval",
        description="",
        type="Retrieval",
        modalities=["text"],
        category="s2p",
        reference=None,
        eval_splits=HeMtebSplits.names(),
        eval_langs=_LANGUAGES,
        main_score="ndcg_at_10",
        date=None,
        domains=["Medical", "Academic"],
        task_subtypes=None,
        license=None,
        annotations_creators="expert-annotated",
        dialect=None,
        sample_creation=None,
        bibtex_citation=None,
        descriptive_stats={
            "n_samples": {
                "Dentistry and Oral Health": 200,
                "Dermatology": 200,
                "Gastroenterology": 200,
                "Genetics": 200,
                "Neuroscience and Neurology": 200,
                "Orthopedic Surgery": 200,
                "Otorhinolaryngology": 200,
                "Plastic Surgery": 200,
                "Pulmonology": 200,
                "Psychiatry and Psychology": 200,
            },
            "avg_character_length": {
                "dev": {
                    "num_documents": 123979,
                    "average_document_length": 328750.045,
                    "Dentistry and Oral Health": {
                        "average_query_length": {
                            "en-en": 75.89,
                            "es-en": 90.42,
                            "fr-en": 97.13,
                        },
                        "num_queries": 200,
                        "average_relevant_docs_per_query": 0,
                    },
                    "Dermatology": {
                        "average_query_length": {
                            "en-en": 59.32,
                            "es-en": 67.11,
                            "fr-en": 72.73,
                        },
                        "num_queries": 200,
                        "average_relevant_docs_per_query": 0,
                    },
                    "Gastroenterology": {
                        "average_query_length": {
                            "en-en": 81.03,
                            "es-en": 92.59,
                            "fr-en": 101.64,
                        },
                        "num_queries": 200,
                    },
                    "Genetics": {
                        "average_query_length": {
                            "en-en": 72.26,
                            "es-en": 83.14,
                            "fr-en": 91.5,
                        },
                        "num_queries": 200,
                    },
                    "Neuroscience and Neurology": {
                        "average_query_length": {
                            "en-en": 80.35,
                            "es-en": 92.2,
                            "fr-en": 111.0,
                        },
                        "num_queries": 200,
                    },
                    "Orthopedic Surgery": {
                        "average_query_length": {
                            "en-en": 86.44,
                            "es-en": 100.72,
                            "fr-en": 107.89,
                        },
                        "num_queries": 200,
                    },
                    "Otorhinolaryngology": {
                        "average_query_length": {
                            "en-en": 79.12,
                            "es-en": 90.83,
                            "fr-en": 98.45,
                        },
                        "num_queries": 200,
                        "average_relevant_docs_per_query": 0,
                    },
                    "Plastic Surgery": {
                        "average_query_length": {
                            "en-en": 88.91,
                            "es-en": 103.42,
                            "fr-en": 112.95,
                        },
                        "num_queries": 200,
                    },
                    "Pulmonology": {
                        "average_query_length": {
                            "en-en": 80.54,
                            "es-en": 97.04,
                            "fr-en": 102.73,
                        },
                        "num_queries": 200,
                    },
                    "Psychiatry and Psychology": {
                        "average_query_length": {
                            "en-en": 92.56,
                            "es-en": 105.57,
                            "fr-en": 114.17,
                        },
                        "num_queries": 200,
                    },
                }
            },
        },
    )

    def _load_corpus(self, split: str, cache_dir: str | None = None):
        ## NOTE: This is a cross-lingual dataset, so the corpus does not depend on the language
        corpus_ds = load_dataset(
            path=self.metadata_dict["dataset"]["path"],
            data_files=f"{split}/corpus.jsonl",
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

    def _load_queries(self, split: str, language: str, cache_dir: str | None = None):
        queries_ds = load_dataset(
            path=self.metadata_dict["dataset"]["path"],
            data_files=f"{split}/queries-{language}.jsonl",
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

    def _load_qrels(self, split: str, cache_dir: str | None = None):
        qrels_ds = load_dataset(
            path=self.metadata_dict["dataset"]["path"],
            data_files=f"{split}/qrels.jsonl",
            revision=self.metadata_dict["dataset"]["revision"],
            cache_dir=cache_dir,
        )
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
            qrels_dict[row["query-id"]][row["corpus-id"]] = 1

        qrels_ds.map(qrels_dict_init)
        return qrels_dict

    def load_data(self, **kwargs):
        if self.data_loaded:
            return

        eval_splits = kwargs.get("eval_splits", self.metadata.eval_splits)
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
                    split=split, cache_dir=cache_dir
                )
                self.queries[language][split] = self._load_queries(
                    split=split, language=language, cache_dir=cache_dir
                )
                self.relevant_docs[language][split] = self._load_qrels(
                    split=split, cache_dir=cache_dir
                )

        self.data_loaded = True
