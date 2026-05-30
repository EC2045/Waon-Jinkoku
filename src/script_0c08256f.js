function switchTab(tabId) {
    document.querySelectorAll('.tab-content').forEach(tab => tab.classList.remove('active'));
    document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
    document.getElementById(tabId).classList.add('active');
    document.getElementById('btn-' + tabId).classList.add('active');
    window.scrollTo({ top: 300, behavior: 'smooth' });
}

function handleEntrySubmission(event) {
    event.preventDefault();
    const name = document.getElementById('entryName').value;
    closeModal('entryModal');
    document.getElementById('msgIcon').innerText = "📋";
    showCustomMsg(`${name} 殿の入国申請を受理しました。審査完了までお待ちください。`);
    event.target.reset();
}

function handleCensusSubmission(event) {
    event.preventDefault();
    closeModal('censusModal');
    document.getElementById('msgIcon').innerText = "📊";
    showCustomMsg(`国勢調査への協力に感謝します。データは「安定」の維持に活用されます。`);
    event.target.reset();
}

function openModal(id) {
    document.getElementById(id).classList.remove('hidden');
    document.body.style.overflow = "hidden";
}
function closeModal(id) {
    document.getElementById(id).classList.add('hidden');
    document.body.style.overflow = "auto";
}
function showCustomMsg(text) {
    document.getElementById('msgText').innerText = text;
    document.getElementById('msgBox').classList.remove('hidden');
}
function hideMsg() {
    document.getElementById('msgBox').classList.add('hidden');
}
window.onclick = function (e) {
    if (e.target.classList.contains('modal')) closeModal(e.target.id);
}
