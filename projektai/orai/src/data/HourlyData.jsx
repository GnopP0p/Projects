export function HourlyData({hourly, hours}){

    return(
        <div className="absolute 2xl:left-80 bottom-32 sm:bottom-6 xl:bottom-40 xl:left-32 lg:left-48 md:left-20 sm:left-2">
            {hourly?.slice(1, hours).map((item, index) => {

                const time = new Date(item.dt * 1000)

                return (
                    <div key={index} className="sm:flex text-white text-2xl sm:border-t-2 inline-block items-center content-center sm:border-white pr-2 pl-2 sm:pr-0 sm:pl-0">
                        <p className="sm:inline-block text-center sm:pr-2 pt-1">{time.getHours() + ":00"}</p>
                        <img className="sm:inline-block mx-auto sm:h-16 sm:w-16 h-12 pt-1" src={'http://openweathermap.org/img/wn/' + item.weather[0].icon + '@2x.png'} alt="" />
                        <p className="sm:inline-block text-center sm:pl-2 pt-1">{item.temp}<span>&#8451;</span></p>
                        <p className="sm:inline-block text-center sm:pl-4 pt-1">{item.wind_speed + "m/s"}</p>
                    </div>
                )
            })}
        </div>
    )
}
