import React, { useState } from "react";
import axios from "axios";

function App() {
  const [city, setCity] = useState("");
  const [weather, setWeather] = useState(null);
  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(false);
  const [days, setDays] = useState(1);
  const [inputError, setInputError] = useState('');

  const API_KEY = "89fe9adf35b6479799e63933252011";

  const validateDays = (value) => {
    const n = parseInt(value, 10);
    return !isNaN(n) && n >= 1 && n <= 14;
  };

  const getWeather = async (fromHistory = false, cityArg) => {
    const qCity = (typeof cityArg === 'string' && cityArg.trim() !== '') ? cityArg.trim() : city.trim();
    if (!qCity) return alert("Masukkan nama kota terlebih dahulu");

    if (!validateDays(days)) {
      setInputError('Masukkan jumlah hari antara 1 dan 14');
      return;
    }

    setInputError('');
    setLoading(true);
    try {
      const response = await axios.get(`http://api.weatherapi.com/v1/forecast.json?key=${API_KEY}&q=${encodeURIComponent(qCity)}&days=${days}&aqi=no`);
      setWeather(response.data);

      setHistory((prevHistory) => {
        const next = [qCity, ...prevHistory.filter(h => h.toLowerCase() !== qCity.toLowerCase())];
        return next.slice(0, 8);
      });

      if (!fromHistory) {
      }
    } catch (error) {
      alert("Kota tidak ditemukan atau ada masalah jaringan");
    } finally {
      setLoading(false);
    }
  };

  const getIcon = (condition) => {
    const lc = (condition || "").toLowerCase();
    if (lc.includes("sun") || lc.includes("clear")) return '☀️';
    if (lc.includes("cloud")) return '☁️';
    if (lc.includes("rain") || lc.includes("drizzle")) return '🌧️';
    if (lc.includes("snow")) return '❄️';
    if (lc.includes("thunder") || lc.includes("thundery")) return '⛈️';
    return '🌈';
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-sky-800 via-indigo-900 to-violet-900 text-slate-50 p-6 flex items-center justify-center">
      <div className="w-full max-w-4xl">
        <header className="mb-8 text-center">
          <h1 className="text-4xl font-extrabold tracking-tight">Aplikasi Cuaca</h1>
          <p className="text-slate-200/80 mt-2">Cepat dan sederhana — cari nama kota untuk melihat cuaca saat ini.</p>
        </header>

        <div className="bg-white/5 backdrop-blur-md rounded-2xl p-6 shadow-lg border border-white/10">
            <div className="flex flex-col md:flex-row gap-4 md:items-center">
            <div className="flex-1">
              <label className="text-sm text-slate-300">Kota</label>
                <input
                  value={city}
                  onChange={(e) => setCity(e.target.value)}
                  onKeyDown={(e) => e.key === 'Enter' && getWeather()}
                  placeholder="Masukkan nama kota, contoh: Jakarta"
                  className="mt-1 w-full px-4 py-3 rounded-lg bg-white placeholder-gray-400 text-black border border-white/6 focus:outline-none focus:ring-2 focus:ring-sky-400"
              />
            </div>

            <div className="w-40">
              <label className="text-sm text-slate-300">Hari (1-14)</label>
              <input
                type="number"
                min={1}
                max={14}
                value={days}
                onChange={(e) => {
                  const v = e.target.value;
                  setDays(v);
                  if (!validateDays(v)) setInputError('Masukkan jumlah hari antara 1 dan 14');
                  else setInputError('');
                }}
                 className="mt-1 w-full px-3 py-2 rounded-lg bg-white placeholder-gray-400 text-black border border-white/6 focus:outline-none"
              />
              {inputError && <div className="text-rose-300 text-sm mt-1">{inputError}</div>}
            </div>

            <div className="flex items-center gap-3">
              <button onClick={() => { setCity(''); setWeather(null); setHistory([]); setDays(1); setInputError(''); setLoading(false); }} className="px-4 py-2 rounded-lg bg-white/3 text-white/90">Reset</button>
              <button onClick={getWeather} disabled={loading || !!inputError} className="px-5 py-3 rounded-lg bg-gradient-to-r from-amber-400 to-pink-500 text-slate-900 font-semibold shadow flex items-center gap-3 disabled:opacity-60">
                {loading && (
                  <svg className="animate-spin h-5 w-5 text-slate-900" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="3" strokeOpacity="0.25"/><path d="M22 12a10 10 0 00-10-10" stroke="currentColor" strokeWidth="3" strokeLinecap="round"/></svg>
                )}
                <span>{loading ? 'Mencari...' : 'Cek Cuaca'}</span>
              </button>
            </div>
          </div>

          {weather ? (
            <div className="mt-6 grid grid-cols-1 md:grid-cols-3 gap-4 items-center">
              <div className="md:col-span-1 flex items-center gap-4">
                <div className="p-4 bg-white/6 rounded-lg">
                  {getIcon(weather.current.condition.text)}
                </div>
                <div>
                  <div className="text-lg font-semibold">{weather.location.name}</div>
                  <div className="text-sm text-slate-300">{weather.location.country}</div>
                </div>
              </div>

              <div className="md:col-span-2 bg-white/6 p-4 rounded-lg">
                <div className="flex items-baseline justify-between">
                  <div>
                    <div className="text-4xl font-bold">{weather.current.temp_c}°C</div>
                    <div className="text-sm text-slate-200/80">{weather.current.condition.text}</div>
                  </div>
                  <div className="text-sm text-slate-200/80 text-right">
                    <div>Feels like <span className="font-semibold">{weather.current.feelslike_c}°C</span></div>
                    <div>Humidity <span className="font-semibold">{weather.current.humidity}%</span></div>
                    <div>Wind <span className="font-semibold">{weather.current.wind_kph} km/h</span></div>
                  </div>
                </div>
              </div>
            </div>
          ) : (
            <div className="mt-6 text-slate-300">Hasil akan tampil di sini setelah pencarian.</div>
          )}

          {weather && weather.forecast && weather.forecast.forecastday && weather.forecast.forecastday.length > 0 && (
            <section className="mt-6">
              <h2 className="text-xl font-semibold mb-4">Prakiraan {days} Hari</h2>
              <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
                {weather.forecast.forecastday.map((d, idx) => (
                  <div key={idx} className="p-4 bg-white/6 rounded-lg">
                    <div className="text-sm text-slate-300">{new Date(d.date).toLocaleDateString('id-ID', { weekday: 'short', day: 'numeric', month: 'short' })}</div>
                    <div className="mt-2">{getIcon(d.day.condition.text)}</div>
                    <div className="font-semibold mt-2">{d.day.condition.text}</div>
                    <div className="flex justify-between mt-3 text-sm">
                      <div>Max <span className="font-semibold">{d.day.maxtemp_c}°C</span></div>
                      <div>Min <span className="font-semibold">{d.day.mintemp_c}°C</span></div>
                      <div>Rain <span className="font-semibold">{d.day.daily_chance_of_rain}%</span></div>
                    </div>
                  </div>
                ))}
              </div>
            </section>
          )}
        </div>

        {history.length > 0 && (
          <div className="mt-6 flex flex-wrap gap-3">
            {history.map((h, i) => (
              <button key={i} onClick={() => { setCity(h); getWeather(true, h); }} className="px-4 py-2 bg-white/6 rounded-full text-white/90 border border-white/10">{h}</button>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

export default App;




