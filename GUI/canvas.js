document.addEventListener('DOMContentLoaded', function initialize(e) {
    var map = [];
    for (i=0; i<20; i++){
        map[i]=[];
        for (j=0;j<15;j++){
            map[i][j]=0;
        }
    }
    var canvas = document.getElementById('myCanvas');
    var context = canvas.getContext('2d');
    context.save();
    context.strokeStyle = "#252a33";
    context.lineWidth = 3;
    for (var i = 0; i < 20; i++){
        for (var j = 0; j < 15; j++){
         context.beginPath();
         context.fillStyle = "#1a1e24";
         context.rect(30 * j, 30 * i, 30, 30);
         context.fill();
         context.stroke();
         context.closePath();
        }
       }
       context.restore();
});