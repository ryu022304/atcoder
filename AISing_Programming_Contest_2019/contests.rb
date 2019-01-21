n = gets.chomp.to_i
a,b = gets.chomp.split().map(&:to_i)
points = gets.chomp.split().map(&:to_i)

a_list = []
b_list = []
c_list = []

points.each do |point|
  if point <= a
    a_list << point
  elsif point <= b
    b_list << point
  else
    c_list << point
  end
end

max_size = [a_list.size, b_list.size, c_list.size].max
count = 0

max_size.times do
  if a_list.size == 0 || b_list.size == 0 || c_list.size == 0
    break
  else
    a_list.pop
    b_list.pop
    c_list.pop
    count += 1
  end
end

puts count
