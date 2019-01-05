s = gets.chomp

t = ['dreamer','eraser','erase','dream']
t_list = t.permutation(4).to_a

s_size = s.size
count = 0

t_list.each do |l|
  new_s = s
  l.each do |str|
    new_s = new_s.gsub(/#{str}/,'')
  end
  if new_s.size == 0
    count += 1
    break
  end
end

if count != 0
  puts 'YES'
else
  puts 'NO'
end
