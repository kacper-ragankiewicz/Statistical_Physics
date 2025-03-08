program CalculatePi
  implicit none

  integer, parameter :: DP = selected_real_kind(15, 307)
  integer, parameter :: lmax = 10000
  real(DP) :: x, y, pi
  integer :: l, lk, i
  character(len=50) :: file_path
  logical :: file_exists
  real(DP), dimension(lmax) :: pi_values
  integer, dimension(lmax) :: seed_array
  integer(DP) :: start_time, stop_time, elapsed_time
  integer :: unit_number

  ! Check if the number of command line arguments is correct
  if (command_argument_count() /= 1) then
    print *, "Usage: ./program <value_of_l>"
    stop
  end if

  ! Read the value of l from the command line argument
  call get_command_argument(1, file_path)
  read(file_path, *) l

  ! Modify the file path to save the file in the "f" folder
  file_path = 'data/' // trim(file_path)

  ! Seed for random number generation
  call random_seed()
  call random_seed(size = i)
  do i = 1, size(seed_array)
     seed_array(i) = i
  end do
  call random_seed(put = seed_array)

  ! Measure the start time
  call system_clock(start_time)

  ! Check if the file exists
  inquire(file = trim(file_path), exist = file_exists)

  ! Open the file with truncation if it exists
  open(unit = 10, file = trim(file_path), action = 'write', status = 'replace', iostat = i)
  if (i /= 0) then
    print *, "Error: Unable to open the file for saving pi."
    stop
  end if

  lk = 0

  do i = 1, l
    call random_number(x)
    call random_number(y)

    if (x**2 + y**2 <= 1.0_DP) then
      lk = lk + 1
    end if

    pi = real(lk, DP) * 4.0_DP / real(i, DP) ! Calculate pi at each iteration
    pi_values(i) = pi

    ! Write the pi value to the file
    write(10, *) pi
  end do

  close(unit = 10)

  ! Measure the end time
  call system_clock(stop_time)
  elapsed_time = stop_time - start_time

  print *, "The values of pi have been written to '", trim(file_path), "'."
  print *, "Execution time: ", elapsed_time, " milliseconds."

end program CalculatePi
