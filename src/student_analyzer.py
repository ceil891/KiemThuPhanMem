from typing import List

class StudentAnalyzer:
    def count_excellent_students(self, scores: List[float]) -> int:
        if not scores:
            return 0

        count = 0
        for score in scores:
            if 0 <= score <= 10 and score >= 8.0:
                count += 1
        return count

    def calculate_valid_average(self, scores: List[float]) -> float:
        if not scores:
            return 0

        total = 0
        valid_count = 0

        for score in scores:
            if 0 <= score <= 10:
                total += score
                valid_count += 1

        return total / valid_count if valid_count > 0 else 0
