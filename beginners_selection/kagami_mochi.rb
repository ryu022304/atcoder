n = gets.chomp.to_i

mochi_list = []
n.times do
  mochi_list << gets.chomp.to_i
end

puts mochi_list.uniq.size
