grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(scores):
    total = 0
    for score in scores:
        total += score
    print total
    return total
    
grades_sum(grades)

def grades_average(grades):
    total = 0
    for grade in grades:
        total += grade
    average = total / float(len(grades))
    print average
    return average
    
grades_average(grades)
