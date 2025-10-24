async function getFootballData() {
    try {
        const response = await fetch('https://www.thesportsdb.com/api/v1/json/123/searchteams.php?t=Arsenal');
        const data = await response.json();
        console.log(data);
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}

getFootballData();  