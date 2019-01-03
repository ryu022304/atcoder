n,a,b = gets.chomp.split(' ').map(&:to_i)

total_list = []

1.upto n do |num|
  devided_num = num.to_s.split('')
  total = devided_num.map(&:to_i).inject(:+)
  if total >= a && total <= b
    total_list << num
  end
end

puts total_list.inject(:+)
