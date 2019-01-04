require 'set'
n = gets.chomp.to_i

mochi_set = Set.new

n.times do
  mochi_set.add(gets.chomp.to_i)
end

# 集合よりも重複を後で消す方が早かった
#mochi_list = []
#n.times do
#  mochi_list << gets.chomp.to_i
#end

#puts mochi_list.uniq.size
puts mochi_set.size
