var generateHanoiMovesIterative = function(numberOfDisks) {
    // direction of rotation of the smallest disk
    var dir = (numberOfDisks % 2 === 0) ? 1 : -1;
  
    var rods = [[], [], []];
    var i, rodMin;
  
    // push disks on our virtual rod's
    for (i = 0; i < numberOfDisks; i += 1) {
      rods[0].push(numberOfDisks - i);
    }
  
    // rodMin will point to rod with smallest disk
    rodMin = 0;
  
    // we need (2^numberOfDisks - 1) moves
    var numberOfMoves = (1 << numberOfDisks) - 1;
  
    // To avoid using % operator we precompute next and prev tables
    var next = [1, 2, 0];
    var prev = [2, 0, 1];
  
    var moves = [];
    var moveSmallest = true;
  
    for (i = 0; i < numberOfMoves; i++) {
        if (moveSmallest) {
          var oldRodMin = rodMin;
          // in JS -1 % 3 === -1, we add 3 to get positive result
          rodMin = (oldRodMin + dir + 3) % 3;
  
          moveDisk(oldRodMin, rodMin);
        }
        else {
          if (topDiskSize(next[rodMin]) > topDiskSize(prev[rodMin])) {
            moveDisk(prev[rodMin], next[rodMin]);
          }
          else {
            moveDisk(next[rodMin], prev[rodMin]);
          }
      }
      moveSmallest = !moveSmallest;
    }
  
    return moves;
  
    function topDiskSize(rodIndex) {
      if (rods[rodIndex].length === 0) return Number.MAX_VALUE;
  
      var rod = rods[rodIndex]
      return rod[rod.length-1];
    }
  
    function moveDisk(from, to) {
      // 1-FROM ROD, 2-USING ROD, 3-TO ROD
      moves.push([from+1, to+1].join(' -> '));
      rods[to].push(rods[from].pop());
    }
  };
  console.log(generateHanoiMovesIterative(3))