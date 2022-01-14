"""Knews Dataset"""


import json
import pickle
import pandas as pd
import os

import datasets


_CITATION = """\
from AI HUB original. Extracted version.
}
"""

_DESCRIPTION = """\
 Knews Dataset from AI HUB open source 문서요약 텍스트.
 Extracted version for abstractive summary fine-tuning.
"""


class KnewsConfig(datasets.BuilderConfig):
    """BuilderConfig for Knews."""

    def __init__(self, **kwargs):
        """BuilderConfig for Knews.
        Args:
          **kwargs: keyword arguments forwarded to super.
        """
        super(KnewsConfig, self).__init__(**kwargs)


class KnewsDataset(datasets.GeneratorBasedBuilder):
    """Knews Dataset extracted from AI HUB."""


    BUILDER_CONFIGS = [
        KnewsConfig(
            name="Knews",
            version=datasets.Version("1.0.1"),
            description="Knews Dataset from AI HUB",
        ),
    ]

    def _info(self):
        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=datasets.Features(
                {
                    "article_original": datasets.Value("string"),
                    "abstractive": datasets.Value("string")
                }
            ),
            supervised_keys=None,
            homepage="https://aihub.or.kr/aidata/8054",
            citation=_CITATION
        )

    def _split_generators(self, dl_manager):
        # arch_path = dl_manager.download_and_extract(self._DOWNLOAD_URL) # 다운로드 된 파일의 경로
        data_dir = "/content/drive/Shareddrives/KLUE Summarization/문서요약 텍스트_unzip/1.Training/신문기사_1.train.jsonl/train.jsonl"

        return [
            datasets.SplitGenerator(
                name=datasets.Split.TRAIN, gen_kwargs={"filepath": data_dir, "split": "train"}
            )
        ]


    def _generate_examples(self, filepath, split):
        """Generate Knews examples."""
        with open(filepath, 'r') as json_file:
            json_list = list(json_file)
        trains = []
        for json_str in json_list:
            line = json.loads(json_str)
            trains.append(line)
        df = pd.DataFrame(trains)[:10]
        for id_, (org, abs) in enumerate(zip(df['article_original'], df['abstractive'])):
            yield id_, {"article_original": ' '.join(org), "abstractive": abs}