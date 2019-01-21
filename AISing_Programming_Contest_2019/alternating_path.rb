$h,$w = gets.chomp.split().map(&:to_i)
$cells = []
$cells_bool = []
$cells_res = []
$direction = [[-1,-1],[-1,1],[1,-1],[1,1]]
$h.times do
  $cells << gets.chomp
  $cells_bool << [0]*$w
end

def searchCell(x,y,state)
  p $cells_bool
  return false if $cells_bool[x][y] != 0
  $direction.each do |tate,yoko|
    next if x+tate<0 || y+yoko<0 || x+tate>=$h || y+yoko>=$w
    if $cells[x+tate][y+yoko] != state
      puts x+tate
      puts y+yoko
      $cells_res << [x+tate,y+yoko]
      $cells_bool[x+tate][y+yoko] = 1
      searchCell(x+tate, y+yoko, $cells[x+tate][y+yoko])
    end
  end
end

$h.times do |height|
  $w.times do |width|
    searchCell(height, width,$cells[height][width])
  end
end

p $cells
p $cells_bool
p $cells_res
