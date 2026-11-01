const supportedLanguages = ['ja', 'en', 'eo'];
let messages = {};
let modalTrigger = null;
let activeModal = null;
let languageRequest = 0;
function readPreference(key) { try { return localStorage.getItem(key); } catch { return null; } }
function writePreference(key, value) { try { localStorage.setItem(key, value); } catch {} }
function t(key) { return messages[key] || key; }
function switchTab(tabId, focus = false) {
    const target = document.getElementById(tabId);
    if (!target?.classList.contains('tab-content')) return;
    document.querySelectorAll('.tab-content').forEach(tab => tab.classList.toggle('active', tab === target));
    document.querySelectorAll('.tab-btn').forEach(btn => {
        const active = btn.id === 'btn-' + tabId;
        btn.classList.toggle('active', active);
        if (active) btn.setAttribute('aria-current', 'page'); else btn.removeAttribute('aria-current');
    });
    if (focus) {
        document.getElementById('main-content').focus({ preventScroll: true });
        window.scrollTo({ top: document.getElementById('main-content').offsetTop, behavior: 'smooth' });
    }
}
window.addEventListener('hashchange', () => switchTab(location.hash.slice(1), true));
document.addEventListener('click', event => {
    const link = event.target.closest('a[href^="#tab-"]');
    if (link && link.hash === location.hash) switchTab(link.hash.slice(1), true);
});
function handleEntrySubmission(event) {
    event.preventDefault();
    const name = document.getElementById('entryName').value;
    closeModal('entryModal', false);
    showCustomMsg(t('portal.entry.result').replace('{name}', name));
    event.target.reset();
}
function handleCensusSubmission(event) {
    event.preventDefault();
    closeModal('censusModal', false);
    showCustomMsg(t('portal.census.result'));
    event.target.reset();
}
function openModal(id) {
    modalTrigger = document.activeElement;
    const modal = document.getElementById(id);
    modal.classList.remove('hidden');
    activeModal = modal;
    document.body.style.overflow = 'hidden';
    modal.querySelector('button,input,select,textarea')?.focus();
}
function closeModal(id, restore = true) {
    document.getElementById(id).classList.add('hidden');
    activeModal = null;
    document.body.style.overflow = '';
    if (restore) modalTrigger?.focus();
}
function showCustomMsg(text) {
    document.getElementById('msgText').textContent = text;
    const box = document.getElementById('msgBox');
    box.classList.remove('hidden');
    activeModal = box;
    document.body.style.overflow = 'hidden';
    box.querySelector('button').focus();
}
function hideMsg() { closeModal('msgBox'); }
document.addEventListener('click', event => {
    if (event.target.classList.contains('modal')) closeModal(event.target.id);
});
document.addEventListener('keydown', event => {
    if (!activeModal) return;
    if (event.key === 'Escape') closeModal(activeModal.id);
    if (event.key === 'Tab') {
        const items = [...activeModal.querySelectorAll('button,input,select,textarea,a[href]')].filter(el => !el.disabled);
        const first = items[0], last = items[items.length - 1];
        if (event.shiftKey && document.activeElement === first) { event.preventDefault(); last.focus(); }
        else if (!event.shiftKey && document.activeElement === last) { event.preventDefault(); first.focus(); }
    }
});
function parseLanguage(text) {
    return Object.fromEntries(text.split('\n').filter(line => line.trim() && !line.trim().startsWith('#') && line.includes('=')).map(line => {
        const i = line.indexOf('='); return [line.slice(0, i).trim(), line.slice(i + 1).trim()];
    }));
}
async function setPortalLanguage(language, remember = true) {
    const request = ++languageRequest;
    if (!supportedLanguages.includes(language)) language = 'ja';
    try {
        const response = await fetch(`${language}.lang`);
        if (!response.ok) throw new Error('Language unavailable');
        const data = parseLanguage(await response.text());
        if (request !== languageRequest) return;
        messages = data;
        document.querySelectorAll('[data-lang-key]').forEach(el => {
            const value = data[el.dataset.langKey];
            if (value !== undefined) el.innerHTML = value;
        });
        document.querySelectorAll('[data-lang-alt]').forEach(el => el.alt = t(el.dataset.langAlt));
        document.querySelectorAll('[data-lang-aria]').forEach(el => el.setAttribute('aria-label', t(el.dataset.langAria)));
        document.documentElement.lang = language;
        document.getElementById('portal-language').value = language;
        if (remember) writePreference('user-lang-setting', language);
    } catch (error) {
        console.warn(error);
        if (request === languageRequest && language !== 'ja') await setPortalLanguage('ja', false);
    }
}
const preferred = readPreference('user-lang-setting');
const browserLanguage = (navigator.languages || [navigator.language]).map(code => code.split('-')[0]).find(code => supportedLanguages.includes(code));
setPortalLanguage(supportedLanguages.includes(preferred) ? preferred : browserLanguage || 'ja', false);
document.getElementById('portal-language').addEventListener('change', event => setPortalLanguage(event.target.value));
switchTab(location.hash.slice(1) || 'tab-home');
