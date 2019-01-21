n = gets.chomp.to_i
h = gets.chomp.to_i
w = gets.chomp.to_i

count = 0
1.upto n do |height|
  if h+height-1 <= n
    1.upto n do |width|
      if w+width-1 <= n
        count += 1
      else
        break
      end
    end
  else
    break
  end
end

puts count
