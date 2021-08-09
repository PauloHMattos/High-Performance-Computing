#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include "matrix.h"

double get_random_value()
{
   return ((double)rand() / (double)RAND_MAX);
}

double *new_vector(int length)
{
   int size = length * sizeof(double);
   double *vector = (double *)malloc(size);
   memset(vector, 0, size);
   return vector;
}

double **new_matrix(int rows, int cols)
{
   double **matrix = (double **)malloc(rows * sizeof(double *));
   for (int i = 0; i < rows; i++)
   {
      matrix[i] = new_vector(cols);
   }
   return matrix;
}

void free_matrix(double **matrix, int size)
{
   for (int i = 0; i < size; i++)
   {
      free(matrix[i]);
   }
   free(matrix);
}

double *generate_random_vector(int length)
{
   double *vector = new_vector(length);
   for (int i = 0; i < length; i++)
   {
      vector[i] = get_random_value();
   }
   return vector;
}

double **generate_random_matrix(int rows, int cols)
{
   double **matrix = new_matrix(rows, cols);
   for (int i = 0; i < rows; i++)
   {
      for (int j = 0; j < cols; j++)
      {
         matrix[i][j] = get_random_value();
      }
   }
   return matrix;
}

void line_product_ij(double **matrix, double *vector, int size, int row_index, double *result)
{
   for (int j = 0; j < size; j++)
   {
      result[row_index] += matrix[row_index][j] * vector[j];
   }
}

void line_product_ji(double **matrix, double *vector, int size, int row_index, double *result)
{
   for (int i = 0; i < size; i++)
   {
      result[row_index] += matrix[i][row_index] * vector[i];
   }
}

void matrix_vector_product_ij(double **matrix, double *vector, int size, double *result)
{
   for (int i = 0; i < size; i++)
   {
      line_product_ij(matrix, vector, size, i, result);
   }
}

void matrix_vector_product_ji(double **matrix, double *vector, int size, double *result)
{
   for (int j = 0; j < size; j++)
   {
      line_product_ji(matrix, vector, size, j, result);
   }
}