import numpy as np
from stl import mesh
from parse_svg import get_heights
from get_svg_file import get_svg_code
import sys


def _get_to_file(file_name, data):
    open(file_name, 'w').close()
    file_object = open(file_name, 'a')
    num = 0
    for i in data:
        print(num)
        print(i)
        file_object.write(str(num) + "\n" + str(i) + "\n")
        num += 1

    file_object.close()


def compare_abs(value):
    value = abs(float(value))
    value = round(value, 3)
    return value


def compare(value):
    value = float(value)
    value = round(value, 3)
    return value


def make_upper_range(data_mesh, x_cord, y_cord, upper):
    points_to_move = []
    ins_lst = []
    x_range = 3.00
    y_range = 2.00
    for i in range(0, len(data_mesh['vectors'])):

        if upper:
            if compare(data_mesh['vectors'][i][0][0]) >= compare(x_cord - 0.2) \
                    and compare(data_mesh['vectors'][i][0][0]) - compare(x_cord) <= x_range \
                    and compare(data_mesh['vectors'][i][0][1]) >= compare(y_cord - 0.2) \
                    and compare(data_mesh['vectors'][i][0][1]) - compare(y_cord) <= y_range \
                    and (data_mesh['vectors'][i][0][2] == 1 or data_mesh['vectors'][i][0][2] == 0.5):
                ins_lst.append(i)
                ins_lst.append(0)
                ins_lst.append(data_mesh['vectors'][i])
                points_to_move.append(ins_lst)
                ins_lst = []

            if compare(data_mesh['vectors'][i][1][0]) >= compare(x_cord - 0.2) \
                    and compare(data_mesh['vectors'][i][1][0]) - compare(x_cord) <= x_range \
                    and compare(data_mesh['vectors'][i][1][1]) >= compare(y_cord - 0.2) \
                    and compare(data_mesh['vectors'][i][1][1]) - compare(y_cord) <= y_range \
                    and (data_mesh['vectors'][i][1][2] == 1 or data_mesh['vectors'][i][1][2] == 0.5):
                ins_lst.append(i)
                ins_lst.append(1)
                ins_lst.append(data_mesh['vectors'][i])
                points_to_move.append(ins_lst)
                ins_lst = []

            if compare(data_mesh['vectors'][i][2][0]) >= compare(x_cord - 0.2) \
                    and compare(data_mesh['vectors'][i][2][0]) - compare(x_cord) <= x_range \
                    and compare(data_mesh['vectors'][i][2][1]) >= compare(y_cord - 0.2) \
                    and compare(data_mesh['vectors'][i][2][1]) - compare(y_cord) <= y_range \
                    and (data_mesh['vectors'][i][2][2] == 1 or data_mesh['vectors'][i][2][2] == 0.5):
                ins_lst.append(i)
                ins_lst.append(2)
                ins_lst.append(data_mesh['vectors'][i])
                points_to_move.append(ins_lst)
                ins_lst = []

        else:
            if compare(data_mesh['vectors'][i][0][0]) >= compare(x_cord - 0.2) \
                    and compare(data_mesh['vectors'][i][0][0]) - compare(x_cord) <= x_range \
                    and compare(data_mesh['vectors'][i][0][1]) <= compare(y_cord + 0.2) \
                    and compare(compare(y_cord) - data_mesh['vectors'][i][0][1]) <= y_range \
                    and (data_mesh['vectors'][i][0][2] == 1 or data_mesh['vectors'][i][0][2] == 0.5):
                ins_lst.append(i)
                ins_lst.append(0)
                ins_lst.append(data_mesh['vectors'][i])
                points_to_move.append(ins_lst)
                ins_lst = []

            if compare(data_mesh['vectors'][i][1][0]) >= compare(x_cord - 0.2) \
                    and compare(data_mesh['vectors'][i][1][0]) - compare(x_cord) <= x_range \
                    and compare(data_mesh['vectors'][i][1][1]) <= compare(y_cord + 0.2) \
                    and compare(compare(y_cord) - data_mesh['vectors'][i][1][1]) <= y_range \
                    and (data_mesh['vectors'][i][1][2] == 1 or data_mesh['vectors'][i][1][2] == 0.5):
                ins_lst.append(i)
                ins_lst.append(1)
                ins_lst.append(data_mesh['vectors'][i])
                points_to_move.append(ins_lst)
                ins_lst = []

            if compare(data_mesh['vectors'][i][2][0]) >= compare(x_cord - 0.2) \
                    and compare(data_mesh['vectors'][i][2][0]) - compare(x_cord) <= x_range \
                    and compare(data_mesh['vectors'][i][2][1]) <= compare(y_cord + 0.2) \
                    and compare(compare(y_cord) - data_mesh['vectors'][i][2][1]) <= y_range \
                    and (data_mesh['vectors'][i][1][2] == 1 or data_mesh['vectors'][i][1][2] == 0.5):
                ins_lst.append(i)
                ins_lst.append(2)
                ins_lst.append(data_mesh['vectors'][i])

                points_to_move.append(ins_lst)
                ins_lst = []

    return points_to_move


def move(data_mesh0, points_to_move, move_value):
    for i in points_to_move:
        data_mesh0['vectors'][int(i[0])][int(i[1])][1] += move_value - 0.598906
        print(data_mesh0['vectors'][int(i[0])][int(i[1])][1])


def add_new_vectors(data_mesh, points_to_add):
    how_many = len(data_mesh['vectors']) + len(points_to_add)

    data_mesh_ret = np.zeros(how_many, dtype=mesh.Mesh.dtype)
    data_mesh_ret['vectors'] = np.concatenate((data_mesh['vectors'], points_to_add), axis=0)
    return data_mesh_ret


def main_loop(data_mesh0, values_to_change, lst):
    lst_of_points = []
    for i in range(0, len(lst)):
        p_upper = make_upper_range(data_mesh0, lst[i][0], lst[i][1], True)  # points upper
        lst_of_points.append(p_upper)
        move(data_mesh0, p_upper, float(values_to_change[i]))
        p_lower = make_upper_range(data_mesh0, lst[i][2], lst[i][3], False)
        lst_of_points.append(p_lower)
        move(data_mesh0, p_lower, -float(values_to_change[i]))
    return lst_of_points


def main():
    url = sys.argv[1]
    your_mesh0 = mesh.Mesh.from_file('template17.stl')
    data_mesh0 = your_mesh0.data

    svg_file_name = get_svg_code(url)
    values_to_change = get_heights(svg_file_name)

    list_of_first_points = [[-29.369, 0.598906, -29.3854, -0.407225],
                            [-26.2844, 0.598906, -26.3003, -0.423641],
                            [-23.1997, 0.598906, -23.2156, -0.423641],
                            [-20.1126, 0.598906, -20.1285, -0.423641],
                            [-17.0279, 0.598906, -17.0439, -0.423641],
                            [-13.9433, 0.598906, -13.9592, -0.423641],
                            [-10.8587, 0.598906, -10.8746, -0.423641],
                            [-7.77155, 0.598906, -7.78746, -0.423641],
                            [-4.68691, 0.598906, -4.70282, -0.423641],
                            [-1.60227, 0.598906, -1.61818, -0.423641],
                            [1.48237, 0.598906, 1.46597, -0.407225],
                            [4.56701, 0.598906, 4.55109, -0.423641],
                            [7.65413, 0.598906, 7.63822, -0.423641],
                            [10.7388, 0.598906, 10.7228, -0.423641],
                            [13.8234, 0.598906, 13.8075, -0.423641],
                            [16.908, 0.598906, 16.8921, -0.423641],
                            [19.9952, 0.598906, 19.9793, -0.423641],
                            [23.0798, 0.598906, 23.0639, -0.423641],
                            [26.1645, 0.598906, 26.1485, -0.423641],
                            [29.2491, 0.598906, 29.2332, -0.423641],
                            [32.3337, 0.598906, 32.3178, -0.423641],
                            [35.4208, 0.598906, 35.4049, -0.423641],
                            [38.5055, 0.598906, 38.4896, -0.423641]]

    main_loop(data_mesh0, values_to_change, list_of_first_points)

    your_mesh = mesh.Mesh(data_mesh0, remove_empty_areas=True)
    # show_stl.show('main.stl')

    your_mesh.save(fr'output\{svg_file_name[:-4]}.stl')
    print("DONE")
    print("You can check out my github at https://github.com/Silvesterrr")


if __name__ == '__main__':
    main()
