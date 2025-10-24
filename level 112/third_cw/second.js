export async function fetchData() {
    try {
        const response = await fetch('https://www.youtube.com/');
        const data = await response.json();
        console.log(data);
        return data;
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}
