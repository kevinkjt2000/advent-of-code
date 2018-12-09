defmodule Day9Test do
  use ExUnit.Case

  test "samples work" do
    assert(Day9.solve(9, 25) == 32)
    assert(Day9.solve(10, 1618) == 8317)
    assert(Day9.solve(13, 7999) == 146_373)
    assert(Day9.solve(17, 1104) == 2764)
    assert(Day9.solve(21, 6111) == 54718)
    assert(Day9.solve(30, 5807) == 37305)
  end
end
