def round_scores(student_scores):
    """
    :param student_scores: list of student exam scores as float or int.
    :return: list of student scores *rounded* to nearest integer value.
    """

    rounded = []
    for i in student_scores:
        rounded.append(round(i))
    return rounded


def count_failed_students(student_scores):
    """
    :param student_scores: list of integer student scores.
    :return: integer count of student scores at or below 40.
    """

    fail_count = 0
    for i in student_scores:
        if i <= 40:
            fail_count+=1
    return fail_count

def above_threshold(student_scores, threshold):
    """
    :param student_scores: list of integer scores
    :param threshold :  integer
    :return: list of integer scores that are at or above the "best" threshold.
    """

    best_count = []
    for i in student_scores:
       if i >= threshold:
           best_count.append(i)
    return best_count


def letter_grades(highest):
    """
    :param highest: integer of highest exam score.
    :return: list of integer lower threshold scores for each D-A letter grade interval.
             For example, where the highest score is 100, and failing is <= 40,
             The result would be [41, 56, 71, 86]:

             41 <= "D" <= 55
             56 <= "C" <= 70
             71 <= "B" <= 85
             86 <= "A" <= 100
    """

    increment = round(highest - 40/ 4)
    scores = []
    for i in range(41, highest, increment):
        scores.append(i)
    return scores

def student_ranking(student_scores, student_names):
    """
     :param student_scores: list of scores in descending order.
     :param student_names: list of names in descending order by exam score.
     :return: list of strings in format ["<rank>. <student name>: <score>"].
     """

    results = []
    for index, name in enumerate(student_names):
        string = str(index+1) + '.' + name + ':' + str(student_names[index])
        results.append(string)
    return results

def perfect_score(student_info):
    """
    :param student_info: list of [<student name>, <score>] lists
    :return: first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    perfect_score = []
    for i in student_info:
        if i[1] == 100:
            perfect_score = i
            break
    return perfect_score