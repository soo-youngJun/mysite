// 디지털 시계 구현
setInterval(myWatch, 1000) // 1초 간격으로 시간 설정

function myWatch(){
    var date = new Date()
    var now = date.toLocaleTimeString()
    document.getElementById("demo").innerHTML = now;
}