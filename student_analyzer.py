from typing import List

class StudentAnalyzer:
    """
    Phân tích điểm số sinh viên
    """

    def count_excellent_students(self, scores: List[float]) -> int:
        """
        Đếm số học sinh đạt loại Giỏi (>= 8.0)
        - Bỏ qua điểm < 0 hoặc > 10
        - Nếu danh sách rỗng hoặc None, trả về 0
        """
        if not scores:
            return 0

        count = 0
        for score in scores:
            if 0 <= score <= 10:
                if score >= 8.0:
                    count += 1
        return count

    def calculate_valid_average(self, scores: List[float]) -> float:
        """
        Tính điểm trung bình của các điểm hợp lệ (0–10)
        - Nếu không có điểm hợp lệ, trả về 0
        """
        if not scores:
            return 0

        total = 0
        valid_count = 0

        for score in scores:
            if 0 <= score <= 10:
                total += score
                valid_count += 1

        if valid_count == 0:
            return 0

        return total / valid_count


# ===== PHẦN CHẠY CHƯƠNG TRÌNH =====
if __name__ == "__main__":
    analyzer = StudentAnalyzer()

    scores = [9.0, 8.5, 7.0, 11.0, -1.0]

    excellent_count = analyzer.count_excellent_students(scores)
    average_score = analyzer.calculate_valid_average(scores)

    print("Danh sách điểm:", scores)
    print("Số học sinh giỏi:", excellent_count)
    print("Điểm trung bình hợp lệ:", round(average_score, 2))
