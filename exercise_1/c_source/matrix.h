#pragma once

double get_random_value();

double *new_vector(int length);
double **new_matrix(int rows, int cols);
void free_matrix(double** matrix, int size);

double *generate_random_vector(int length);
double **generate_random_matrix(int rows, int cols);

void line_product_ij(double **matrix, double *vector, int size, int col_index, double *result);
void line_product_ji(double **matrix, double *vector, int size, int col_index, double *result);

void matrix_vector_product_ij(double **matrix, double *vector, int size, double *result);
void matrix_vector_product_ji(double **matrix, double *vector, int size, double *result);