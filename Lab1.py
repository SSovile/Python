class Puzzle:
    puzzle_count: int = 0


    def __init__(self, description ="", number_of_elements=0, width=0, height=0, difficulty="",weight=0,producer=""):
        self.description = description
        self.num_of_ele = number_of_elements
        self.width = width
        self.height = height
        self.difficulty = difficulty
        self.weight = weight
        self.producer = producer
        Puzzle.puzzle_count += 1

    def __str__(self) -> str:
        return f"Puzzle:\n  description: {self.description}\n  number of elements: {self.num_of_ele}\n  width: {self.width}  gramm\n  height: {self.height}\n  difficulty: {self.difficulty}\n  producer: {self.producer}"

    def __del__(self):
        del self

    @classmethod
    def get_count(cls) -> int:
        return cls.puzzle_count

def main():
    obj1 = Puzzle("game", 128, 28, 10, "hard", 300, "Hasbro")
    obj2 = Puzzle("game", 64, 14, 5, "easy", 150, "Hasbro")

    print(obj1)
    print(obj2)
    Puzzle.get_count()

if __name__ == "__main__":
    main()