"""Typing capabilities of Python"""

from typing import List, Union


class Student:
    """Test class"""

    name: str
    studies: str
    friends: List[
        "Student"
    ]  # reference class in itself ; use List and not list for backwarda compat.
    grades: List[Union[int, str]]  # Union of types

    def __init__(self, name, studies, friends, grades):
        self.name = name
        self.studies = studies
        self.friends = friends
        self.grades = grades


if __name__ == "__main__":
    st = Student(
        name="yanice",
        studies="computer science",
        friends=[Student("bob", "math", [], [12, "B"])],
        grades=[13, 14, 15],
    )
    print(type(Student.grades))
