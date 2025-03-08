program random_jump
  implicit none
  integer, parameter :: dp = kind(1.0d0)
  integer :: t, K, i, j, percent_done
  real(dp) :: p, u
  real(dp), allocatable :: s(:), Na(:), Nb(:)
  character(len=32) :: filename
  open(10, file='output.txt', status='replace')

  ! Initialize parameters
  t = 10000
  p = 0.8
  K = 1000000

  ! Allocate arrays
  allocate(s(t))
  allocate(Na(t))
  allocate(Nb(t))

  ! Initialize arrays
  s = 0.0_dp
  Na = K
  Nb = 0.0_dp
  s(1) = 1.0_dp

  ! Seed the random number generator
  call random_seed()

  ! Main loop
  do j = 1, K
     if (mod(j, K/100) == 0) then
        percent_done = j * 100 / K
        write(*,'(A,I3,A)', advance='no') 'Progress: ', percent_done, '%'
        if (percent_done < 100) then
           write(*, '(A)', advance='no') char(13)  ! Carriage return for updating the same line
        else
           write(*, *)  ! New line at 100%
        end if
     end if
     do i = 2, t
        call random_number(u)
        if (u >= p) then
           s(i) = 0.0_dp
           if (Na(i-1) > 0) then
              Na(i) = Na(i-1) - 1
           else
              Na(i) = Na(i-1)
           end if
           if (Nb(i-1) < K) then
              Nb(i) = Nb(i-1) + 1
           else
              Nb(i) = Nb(i-1)
           end if
        else
           s(i) = 1.0_dp
           Na(i) = Na(i-1)
           Nb(i) = Nb(i-1)
        end if
     end do
  end do

  ! Write results to file
  do i = 1, t
     write(10, '(F6.2,1x,I6,1x,I6)') s(i), Na(i), Nb(i)
  end do
  close(10)

  ! Deallocate arrays
  deallocate(s)
  deallocate(Na)
  deallocate(Nb)

end program random_jump
