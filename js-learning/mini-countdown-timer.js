setInterval(() => {
    let date = Math.floor((new Date("2026-12-31").getTime()-Date.now())/1000)
    let days = 0
    let hours = 0
    let minutes = 0
    let seconds = 0
    while(date>(24*60*60)) {
    days++
    date-=(24*60*60)
}
while(date>(60*60)) {
    hours++
    date-=(60*60)
}
while(date>(60)) {
    minutes++
    date-=60
}
seconds=date
console.log(days,hours,minutes,seconds)
},1000)