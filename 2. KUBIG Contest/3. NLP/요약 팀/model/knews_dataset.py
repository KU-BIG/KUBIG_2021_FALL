"""Knews Dataset"""

import json
import pandas as pd
import os
import datasets


_CITATION = """\
from AI HUB original. Extracted version.
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
        data_dir = os.path.join(os.path.dirname(__file__), "datas/train.jsonl")
        if not os.path.exists(data_dir):
            print('You should prepare for train.jsonl in ../datas')
            raise FileNotFoundError

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
        df = pd.DataFrame(trains)
        for id_, (org, abs) in enumerate(zip(df['article_original'], df['abstractive'])):
            yield id_, {"article_original": ' '.join(org), "abstractive": abs}
