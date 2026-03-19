import itertools
from itertools import islice
from typing import Iterator, Optional, Tuple


class BaseTextListProduct:
    @staticmethod
    def get_common_input_types():
        return {
            "separator": ("STRING", {"default": ", "}),
            "max_results": (
                "INT",
                {"default": 0, "min": 0, "step": 1},
            ),
        }

    @staticmethod
    def get_max_results_limit(max_results: int) -> Optional[int]:
        return None if max_results <= 0 else max_results

    def join_filtered_lists(self, separator, *lists, max_results=0) -> Iterator[str]:
        joined_results = map(separator.join, self.get_filtered_product(*lists))
        limit = self.get_max_results_limit(max_results)
        if limit is None:
            return joined_results
        return islice(joined_results, limit)

    def collect_joined_lists(self, separator, *lists, max_results=0) -> list[str]:
        return list(
            self.join_filtered_lists(separator, *lists, max_results=max_results)
        )

    def get_filtered_product(self, *lists) -> Iterator[Tuple[str, ...]]:
        # itertools.productは空文字列を含むと、空文字列との組み合わせも生成する。例えば("","a")。
        # それをjoinすると、", a"のような文字列が生成されてしまう。
        # そのためまず、すべてが空文字列である組み合わせを除外して、
        # 次にmap filter(None, x)で空文字を除外したタプルのイテレータに変換する
        non_empty_combinations = filter(any, itertools.product(*lists))
        return map(lambda x: filter(None, x), non_empty_combinations)
