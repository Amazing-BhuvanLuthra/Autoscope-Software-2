document.getElementById('toggleButton').addEventListener('click', function () {
    var header = document.getElementById('header');
    var footer = document.getElementById('footer');
    header.style.display = (header.style.display === 'none') ? 'block' : 'none';
    footer.style.display = (footer.style.display === 'none') ? 'block' : 'none';

    // Optional: You can send a request to the server if you need to keep track of the state
    fetch('/toggle_header_footer', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(response => response.json())
        .then(data => console.log(data));
});

document.querySelector('.camera-button').addEventListener('click', function () {
    alert('Camera button clicked!');
});

document.querySelector('.video-start-button').addEventListener('click', function () {
    alert('Video start button clicked!');
});

document.querySelector('.video-stop-button').addEventListener('click', function () {
    alert('Video stop button clicked!');
});

document.querySelector('.motor-reset-button').addEventListener('click', function () {
    alert('Motor reset button clicked!');
});

