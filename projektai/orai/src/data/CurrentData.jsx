export function CurrentData({current, city}){

    const currentTime = new Date(current.dt * 1000)

    return(
        <div className="pt-16 text-white sm:text-5xl text-3xl text-center">
            <div className="">{currentTime.getDate()}d {currentTime.getHours() + ":" + currentTime.getMinutes()}</div>
            <div className="">{city && city + " city"}</div>
            <div className="text-7xl sm:text-9xl">{parseInt(current.temp)}<span>&#8451;</span><img className="inline-block align-top sm:h-auto sm:w-auto h-12" src={'http://openweathermap.org/img/wn/' + current.weather[0].icon + '@2x.png'} alt="" /></div>
            <div>{"Wind speed " + current.wind_speed + "m/s"}</div>
        </div>
    )
}