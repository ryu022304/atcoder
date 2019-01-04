n = gets.chomp.to_i
cards = gets.chomp.split(' ').map(&:to_i).sort!

a = []
b = []
0.upto n do
  a << cards.pop
  b << cards.pop
  if cards.size == 0
    break
  end
end

puts a.compact.inject(:+) - b.compact.inject(:+)
