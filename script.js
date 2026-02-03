const player = videojs('my-video');
let allChannels = [];

async function loadChannels() {
    try {
        const res = await fetch('channels.json');
        allChannels = await res.json();
        renderChannels(allChannels);
    } catch (e) { console.error("خطأ في جلب القنوات"); }
}

function renderChannels(channels) {
    const list = document.getElementById('channelList');
    list.innerHTML = '';
    channels.forEach(ch => {
        const item = document.createElement('div');
        item.className = 'channel-item';
        item.innerHTML = `<img src="${ch.logo}"><span>${ch.name}</span>`;
        item.onclick = () => {
            player.src({ src: ch.url, type: 'application/x-mpegURL' });
            player.play();
            document.getElementById('currentChannelName').innerText = ch.name;
        };
        list.appendChild(item);
    });
}

// ميزة البحث
document.getElementById('searchInput').oninput = (e) => {
    const term = e.target.value.toLowerCase();
    const filtered = allChannels.filter(ch => ch.name.toLowerCase().includes(term));
    renderChannels(filtered);
};

loadChannels();
