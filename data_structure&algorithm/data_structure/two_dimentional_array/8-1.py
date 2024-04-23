N = int(input())
T = input()



num_students_who_like_this_color = dict()


for student_i in range(N):

    num_of_colors_student_i_likes_M = int(input())
    names_of_color_S = list(input().split())
    for color in names_of_color_S:
        num_students_who_like_this_color[color] = num_students_who_like_this_color.get(color,0) + 1



print(num_students_who_like_this_color.get(T,0))