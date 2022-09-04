export function DailyData({daily, days}){

    return(
        <div className="absolute 2xl:right-80 bottom-6 xl:bottom-40 xl:right-32 lg:right-48 md:right-20 sm:right-2 hidden sm:block">
            {daily?.slice(1, days).map((item, index) => {

                let time = new Date(item.dt * 1000)

                return(
                    <div key={index} className="flex text-white text-2xl border-t-2 border-white">
                        <div>
                            <p className="inline-block pr-2">{time.getDate() + " d"}</p>
                            <img className="inline-block sm:h-16 sm:w-16 h-8" src={'http://openweathermap.org/img/wn/' + item.weather[0].icon + '@2x.png'} alt="" />
                            <p className="inline-block pl-2">{item.temp.day}<span>&#8451;</span></p>
                            <p className="inline-block pl-4">{item.wind_speed + "m/s"}</p>
                        </div>
                    </div>
                )
            })}
        </div>
    )
}
