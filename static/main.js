fetch("/api/stations")
  .then(r => r.json())
  .then(stations => {
    stations.forEach(s => {
      console.log(`${s.name}: bikes=${s.bikes}, stands=${s.stands}`);
    });
  })
  .catch(err => console.error(err));