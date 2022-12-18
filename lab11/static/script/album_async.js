import sendData from "./sendAsync.js";

let sendBth = document.getElementById('add_al');
let songForm = document.getElementById('song');
let albumForm = document.getElementById('album');


albumForm.onsubmit = (e) => {
    e.preventDefault()
    let xhr = sendData(albumForm, 'add');
    let albumResponse = new Response(xhr.response).json();
    albumResponse.then((value) => {
        if (value['add'] === 'success') {
            songForm.style.display = 'flex';
        }
    });
}
songForm.onsubmit = (e) => {
    e.preventDefault();
    let songData = Object.fromEntries(new FormData(songForm));
    let albumData = Object.fromEntries(new FormData(albumForm));
    if (songData['song_name']) {
        sendData(songForm, '/song/add');
        sendData({
            'song_name': songData['song_name'],
            'album_name': albumData['name']
        }, 'entities/add', false);
    }
}
