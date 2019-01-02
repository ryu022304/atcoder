num_of_500yen = gets.chomp.to_i
num_of_100yen = gets.chomp.to_i
num_of_50yen = gets.chomp.to_i
total = gets.chomp.to_i

count = 0
0.upto num_of_500yen do |a|
  0.upto num_of_100yen do |b|
    0.upto num_of_50yen do |c|
      x = 500*a + 100*b + 50*c
      if x == total
        count += 1
      end
    end
  end
end

puts count
