'''
Created on 17-Aug-2022

@author: HP
''' 


"""list_QA =[
                ("When was the first known use of the word 'quiz'","1781"),
                ("which python library is used for arrays","Numpy")
    ]"""

dict_QA = {
        "When was the first known use of the word 'quiz'":["1781","1780","1880","1881"],
        "which python library is used for arrays":["numpy","pandas","scikit","matplotlib"],
        "What's the name of Python's sorting algorithm": ["Timsort", "Quicksort", "Merge sort", "Bubble sort"]
    }

for ques,choices in dict_QA.items():
    correct_ans = choices[0]
    sorted_alternative = sorted(choices)
    for label,choice in enumerate(sorted_alternative,1):
        print(f" {label}) {choice}")
    
    
    user_label= int(input(f"{ques}?"))
    user_ans = sorted_alternative[user_label-1]
    if user_ans == correct_ans:
        print("Correct,nicely done")
    else:
        print(f"The correct answer is: {correct_ans!r},not {user_ans!r}")