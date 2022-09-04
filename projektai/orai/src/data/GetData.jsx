import axios from 'axios';
import { useEffect, useState } from 'react';  
import { CurrentData } from './CurrentData';
import { DailyData } from './DailyData';
import { HourlyData } from './HourlyData';

export function GetData(){

    const weatherApiCode = '2afbc9e42303fe438728772af39dd1fc'

    const [temperatures, setTemperatures] = useState()
    const [error, setError] = useState(null)
    const [cityName, setCity] = useState('Kaunas')
    const [isLoaded, setIsLoaded] = useState(true)
    const hours = 5
    const days = 5

    const getdata = async (city) => {
        setError(null)
        try{
            setIsLoaded(true)
            const res1 = await axios.get('http://api.openweathermap.org/geo/1.0/direct?q=' + city + '&limit=1&appid=' + weatherApiCode)
            const res2 = await axios.get('http://api.openweathermap.org/data/2.5/onecall?lat=' + res1.data[0].lat + '&lon=' + res1.data[0].lon + '&units=metric&appid=' + weatherApiCode)
            
            setTemperatures(res2.data)
            setIsLoaded(false)
            console.log(res2.data)
        }catch(e){
            setError(e)
            console.log(e)
            setIsLoaded(false)
        }
         
    }

    useEffect(() => {
        getdata('kaunas')
    }, [])
    
    if(isLoaded){
        return(
            <svg role="status" className="mr-2 lg:w-12 lg:h-12 text-gray-200 animate-spin fill-blue-600" viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z" fill="currentColor"/>
                <path d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z" fill="currentFill"/>
            </svg>
        )
    }

    if(error){
        return(
            <div className='pt-10 pl-12'>
                <form action="" className=''>
                    <input className='bg-transparent border-solid border-white border rounded text-white' type="text" value={cityName} onChange={(e) => setCity(e.target.value)}/>
                    <button onClick={() => getdata(cityName)}>Get data</button>
                </form>
            </div>    
        )
    }

    return(
        <div className='h-screen w-screen relative'>
            <div className='flex sm:flex-wrap flex-row ml-12 pt-12'>
                <form action="" className='border-solid w-max'>
                    <input className='bg-transparent border-solid border-white border-2 rounded text-white text-2xl p-1' type="text" value={cityName} onChange={(e) => setCity(e.target.value)}/>
                    <button className='bg-transparent rounded text-slate-300 sm:ml-0 ml-24 text-2xl border-r-2 border-b-2 sm:border-t-2 border-l-2 sm:border-l-0 border-t-0 text-center p-1' onClick={() => getdata(cityName)}>Get data</button>
                </form>
            </div>
            <CurrentData current={temperatures.current} city={cityName} />
            <HourlyData hourly={temperatures.hourly} hours={hours}/>
            <DailyData daily={temperatures.daily} days={days} />
        </div>
    )

}
