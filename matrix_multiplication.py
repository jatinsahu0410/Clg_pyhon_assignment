# implement matrix multiplication
def matrix_multiplication(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        print("Number of columns in Matrix 1 must be equal to the number of rows in Matrix 2 for multiplication.")
        return None

    result_matrix = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]

    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]

    return result_matrix

def print_matrix(matrix):
    for row in matrix:
        print(row)

def main():
    print("Matrix Multiplication")

    # Get the dimensions of the matrices
    rows1 = int(input("Enter the number of rows for Matrix 1: "))
    cols1 = int(input("Enter the number of columns for Matrix 1: "))
    rows2 = int(input("Enter the number of rows for Matrix 2: "))
    cols2 = int(input("Enter the number of columns for Matrix 2: "))

    # Get the elements of the first matrix
    print("Enter elements for Matrix 1:")
    matrix1 = [[int(input(f"Enter element at position ({i + 1}, {j + 1}): ")) for j in range(cols1)] for i in range(rows1)]

    # Get the elements of the second matrix
    print("Enter elements for Matrix 2:")
    matrix2 = [[int(input(f"Enter element at position ({i + 1}, {j + 1}): ")) for j in range(cols2)] for i in range(rows2)]

    # Perform matrix multiplication
    result = matrix_multiplication(matrix1, matrix2)

    if result:
        print("Matrix 1:")
        print_matrix(matrix1)

        print("\nMatrix 2:")
        print_matrix(matrix2)

        print("\nResultant Matrix (Matrix 1 * Matrix 2):")
        print_matrix(result)

if __name__ == "__main__":
    main()

