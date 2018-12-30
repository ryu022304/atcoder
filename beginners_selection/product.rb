a,b = gets.chomp.split(' ').map(&:to_i)
res = a * b
if res % 2 == 0
  puts 'Even'
else
  puts 'Odd'
end
