import itertools
from typing import Iterator, Tuple


class BaseTextListProduct:
    def __init__(self):
        pass

    def join_filtered_lists(self, separator, *lists) -> Iterator[str]:
        return map(separator.join, self.get_filtered_product(*lists))

    def get_filtered_product(self, *lists) -> Iterator[Tuple[str, ...]]:
        # itertools.productは空文字列を含むと、空文字列との組み合わせも生成する。例えば("","a")。
        # それをjoinすると、", a"のような文字列が生成されてしまう。
        # そのためまず、すべてが空文字列である組み合わせを除外して、
        # 次にmap filter(None, x)で空文字を除外したタプルのイテレータに変換する
        non_empty_combinations = filter(any, itertools.product(*lists))
        return map(lambda x: filter(None, x), non_empty_combinations)
