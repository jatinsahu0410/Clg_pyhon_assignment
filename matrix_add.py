# implement matrix addition
def matrix_addition(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Matrices must have the same dimensions for addition.")
        return None

    result_matrix = [[0 for _ in range(len(matrix1[0]))] for _ in range(len(matrix1))]

    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result_matrix[i][j] = matrix1[i][j] + matrix2[i][j]

    return result_matrix

def print_matrix(matrix):
    for row in matrix:
        print(row)

def main():
    print("Matrix Addition")

    # Get the dimensions of the matrices
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    # Get the elements of the first matrix
    print("Enter elements for Matrix 1:")
    matrix1 = [[int(input(f"Enter element at position ({i + 1}, {j + 1}): ")) for j in range(cols)] for i in range(rows)]

    # Get the elements of the second matrix
    print("Enter elements for Matrix 2:")
    matrix2 = [[int(input(f"Enter element at position ({i + 1}, {j + 1}): ")) for j in range(cols)] for i in range(rows)]

    # Perform matrix addition
    result = matrix_addition(matrix1, matrix2)

    if result:
        print("Matrix 1:")
        print_matrix(matrix1)

        print("\nMatrix 2:")
        print_matrix(matrix2)

        print("\nResultant Matrix (Matrix 1 + Matrix 2):")
        print_matrix(result)

if __name__ == "__main__":
    main()
