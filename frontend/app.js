document.getElementById('drawCard').addEventListener('click', async () => {
    const playerAddress = prompt("Enter your Ethereum address:");
    const response = await fetch('/draw_card', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ player_address: playerAddress })
    });
    const result = await response.json();
    if(result.status === 'Card drawn') {
        alert('Card successfully drawn!');
        // Update the interface and display the new card here
    } else {
        alert('Error drawing card.');
    }
});
