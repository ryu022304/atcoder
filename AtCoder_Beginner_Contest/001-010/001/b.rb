m = gets.to_i
res = 0
if m < 100
  res=0
elsif m.between?(100,5000)
  res=m/100
elsif m.between?(6000,30000)
  res=m/1000+50
elsif m.between?(35000,70000)
  res=(m/1000-30)/5+80
elsif 70000 < m
  res=89
end
puts sprintf("%02d",res)
