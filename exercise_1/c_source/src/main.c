#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "matrix.h"

int main(int argc, char *argv[])
{
    if (argc != 3 || (atoi(argv[2]) != 0 && atoi(argv[2]) != 1))
    {
        printf("Invalid arguments.\n");
        return 0;
    }

    // Read the inputs
    int size = atoi(argv[1]);
    int order = atoi(argv[2]);

    // Variables to store timming data
    clock_t start, end;

    // Seed the random number generator
    srand(time(NULL));

    // Initialize a random square matrix and vector 
    double **matrix = generate_random_matrix(size, size);
    double *vector = generate_random_vector(size);

    // Allocate a clear vector to be the result of the product
    double *result = new_vector(size);

    if (order == 1)
    {
        start = clock();
        matrix_vector_product_ij(matrix, vector, size, result);
        end = clock();
    }
    else
    {
        start = clock();
        matrix_vector_product_ji(matrix, vector, size, result);
        end = clock();
    }

    // Free the allocated resources
    free_matrix(matrix, size);
    free(vector);
    free(result);

    // Outputs the system size and ellapsed time in the product
    printf("%d;%.6f\n", size, ((double)(end - start)) / CLOCKS_PER_SEC);
    return 0;
}