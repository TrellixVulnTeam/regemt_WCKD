from typing import List

from comet.models import download_model

from .common import Judgements, Metric


class Comet(Metric):
    # https://unbabel.github.io/COMET/html/running.html
    # https://aclanthology.org/2020.emnlp-main.213.pdf#page=5

    label = "Comet"

    def __init__(self):
        self.model = download_model("wmt-large-da-estimator-1719", "comet_model/")

    def compute(self, judgements: Judgements) -> List[float]:
        data = {"src": judgements.src_texts,
                "mt": judgements.translations,
                "ref": [rs[0] for rs in judgements.references]}
        data = [dict(zip(data, t)) for t in zip(*data.values())]
        return self.model.predict(data, cuda=True, show_progress=True)
