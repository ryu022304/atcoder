n, total = gets.chomp.split(' ').map(&:to_i)

example = []
0.upto n do |card_of_10000|
  0.upto n do |card_of_5000|
    card_of_1000 = n - card_of_10000 - card_of_5000
    x = 10000*card_of_10000 + 5000*card_of_5000 + 1000*card_of_1000
    if x == total && card_of_1000 >= 0
      example << [card_of_10000,card_of_5000,card_of_1000]
    end
  end
end

if example.size == 0
  example << ['-1']*3
end

puts example.pop.join(' ').strip
