
subroutine generate_random_vector(size, vector)
    implicit none

    integer, intent(in) :: size
    real(8), dimension(size), intent(inout) :: vector

    integer :: i
    real(8) :: number

    do i = 1, size
        call random_number(number)
        vector(i) = number
    end do
end subroutine generate_random_vector

subroutine generate_random_matrix(rows, cols, matrix)
    implicit none

    integer, intent(in)                           :: rows, cols
    real(8), dimension(rows, cols), intent(inout) :: matrix

    integer :: i, j
    real(8) :: number

    do i = 1, rows
        do j = 1, cols
            call random_number(number)
            matrix(i, j) = number
        end do
    end do
end subroutine generate_random_matrix


subroutine matrix_vector_product_ij(matrix, vector, size, result)
    implicit none
    
    integer, intent(in)                 :: size
    real(8), dimension(size,size), intent(in) :: matrix
    real(8), dimension(size), intent(in)   :: vector
    real(8), dimension(size)  :: result

    integer :: i, j
    
    result = 0.0
    do i = 1, size
        do j = 1, size
            result(i) = result(i) +  matrix(i, j) * vector(j);
        end do
    end do
end subroutine matrix_vector_product_ij

subroutine matrix_vector_product_ji(matrix, vector, size, result)
    implicit none
    integer, intent(in)                 :: size
    real(8), dimension(size,size), intent(in) :: matrix
    real(8), dimension(size), intent(in)   :: vector
    real(8), dimension(size)  :: result

    integer :: i, j

    result = 0.0
    do j = 1, size
        do i = 1, size
            result(i) = result(i) +  matrix(i, j) * vector(j);
        end do
    end do
end subroutine matrix_vector_product_ji

