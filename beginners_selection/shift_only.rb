n = gets.chomp.to_i
numbers = gets.chomp.split(' ').map(&:to_i)

count = 0
new_num = numbers
while true
  if new_num.map(&:odd?).include?(true)
    break
  else
    new_num = new_num.map{|num| num / 2}
    count += 1
  end
end

puts count
