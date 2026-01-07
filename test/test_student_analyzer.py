from src.student_analyzer import StudentAnalyzer

def test_count_excellent_students():
    analyzer = StudentAnalyzer()
    assert analyzer.count_excellent_students([9.0, 8.5, 7.0, 11.0, -1.0]) == 2
    assert analyzer.count_excellent_students([]) == 0
    assert analyzer.count_excellent_students([0, 10, 8]) == 2

def test_calculate_valid_average():
    analyzer = StudentAnalyzer()
    avg = analyzer.calculate_valid_average([9.0, 8.5, 7.0, 11.0, -1.0])
    assert abs(avg - 8.17) < 0.01

    assert analyzer.calculate_valid_average([]) == 0
    assert analyzer.calculate_valid_average([-1, 11]) == 0
