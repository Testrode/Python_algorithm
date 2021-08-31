side_triangle_AB = int(input('Введите параметры стороны AB: '))
side_triangle_BC = int(input('Введите параметры стороны BC: '))
side_triangle_AC = int(input('Введите параметры стороны AC: ')) #Основание
if side_triangle_AB != side_triangle_BC != side_triangle_AC:
    print('Этот треугольник разносторонний')
if side_triangle_AB == side_triangle_BC == side_triangle_AC:
    print('Этот треугольник равносторонний')
if side_triangle_AB == side_triangle_BC != side_triangle_AC:
    print('Этот треугольник равнобедренный')