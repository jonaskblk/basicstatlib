from typing import List

@staticmethod
def add(vector_a: List, vector_b: List) -> List:
    assert len(vector_a) == len(vector_b), "Adding two vectors needs them to be of the same length"
    return [vector_a_i + vector_b_i for vector_a_i, vector_b_i in zip(vector_a, vector_b)]