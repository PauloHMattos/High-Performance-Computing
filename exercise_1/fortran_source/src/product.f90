program product
    implicit none
    
    external getarg
    character(len=32) :: arg
    integer :: size, order
    real(8) :: start, finish
    real(8), dimension(:,:), allocatable :: matrix
    real(8), dimension (:), allocatable :: vector
    real(8), dimension (:), allocatable :: result

    ! Getting argument for the size of the system
    call GET_COMMAND_ARGUMENT(1, arg)    
    read(arg, "(I10)") size

    ! Get argument with the order of the loops 
    call GET_COMMAND_ARGUMENT (2, arg)    
    read(arg, "(I1)") order

    ! Allocating variables
    allocate(matrix(size, size))
    allocate(vector(size))

    ! Allocate the result vector and clears it
    allocate(result(size))
    result = 0.0

    ! Seed the random number generator
    call random_seed()

    call generate_random_vector(size, vector)
    call generate_random_matrix(size, size, matrix)

    if (order == 0) then
        call cpu_time(start) 
        call matrix_vector_product_ij(matrix, vector, size, result)
        call cpu_time(finish) 
    else if (order == 1) then
        call cpu_time(start) 
        call matrix_vector_product_ji(matrix, vector, size, result)
        call cpu_time(finish) 
    end if

    ! Deallocating all the arrays
    deallocate(matrix)
    deallocate(vector)
    deallocate(result)

    ! Prints the system size and the elapsed time for the operation
    print *, size, ";", (finish - start)
end program product